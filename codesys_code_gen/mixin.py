"""Codesys attrs mixin and helper functions."""

from datetime import datetime
from typing import Any, Dict, List

import attrs
from boltons.iterutils import default_visit, flatten, remap


def get_leaf_paths(obj: Dict[str, Any]) -> List[Any]:
    paths = []

    def visit_collect_leaves(p, k, v):
        ret = default_visit(p, k, v)
        if not isinstance(v, dict):
            paths.append((p, k, v))
        return ret

    remap(obj, visit_collect_leaves)
    return [flatten(x) for x in paths]


def null_value(val: Any, member: str) -> str:
    if val is not None:
        return f"{val!s}"
    if member.startswith("rl"):
        return "gConst.gc_rlNULL"
    elif member.startswith("dt"):
        return "gConst.gc_dtNULL"
    elif member.startswith("s"):
        return "''"
    else:
        return "0"


def assign_member(path: List[Any], var_name: str, indent_level: int) -> str:
    val = path.pop()
    sVal = null_value(val, path[-1])
    # Check if it is a TIME prefix
    if path[-1].startswith("t"):
        sVal = f"T#{val if val is not None else 0}S"
    elif path[-1].startswith("dt"):
        # DT#1970-1-1-0:0:0
        if type(val) is datetime:
            sVal = f"DT#{val.year}-{val.month}-{val.day}-{val.hour}:{val.minute}:{val.second}"
        if val is None:
            sVal = "gConst.gc_dtNULL"
    if isinstance(val, str):
        sVal = f"'{val}'"
    level = "\t" * indent_level
    full_path = ".".join(path)
    return f"{level}{var_name}.{full_path} := {sVal};\n"


def max_member_str_length(
    path_parts: List[str], var_name: str, indent_level: int
) -> str:
    sVal = ""
    path = path_parts[-1]
    full_path = ".".join(path_parts)
    if path.startswith("rl"):
        sVal = "gConst.gc_rlLongStr"
    elif path.startswith("ix"):
        sVal = "gConst.gc_diMax"
    elif path.startswith("t"):
        sVal = "gConst.gc_tMax"
    elif path.startswith("dt"):
        sVal = "gConst.gc_dtLongest"
    # this needs to be after "ix" prefix
    elif path.startswith("i"):
        sVal = "gConst.gc_iMax"
    elif path.startswith("s"):
        sVal = "gConst.gc_sLorem"
    elif path.startswith("x"):
        sVal = "TRUE"
    level = "\t" * indent_level
    return f"{level}{var_name}.{full_path} := {sVal};\n"


def dot_join_identifiers(path_leaf: List[List[str | int | float | None]]) -> List[str]:
    # get_leaf_paths returns a list of elements. The elements contain a list of
    # the identifier path with the last element in that list being the object
    # value. We strip out the value and then join the identifiers with a `.`
    paths: List[List[str]] = [x[:-1] for x in path_leaf]
    return [".".join(x) for x in paths]


class AsCodesysMixin:
    def to_codesys(self, var_name: str, indent_level: int = 0) -> List[str]:
        """Convert to codesys code"""

        code = [
            assign_member(path, var_name, indent_level)
            for path in get_leaf_paths(attrs.asdict(self))
        ]
        return code

    def to_assert(self, expected: str, actual: str, indent_level: int = 0) -> List[str]:
        """Convert to AssertEquals"""
        level = "\t" * indent_level
        paths = get_leaf_paths(attrs.asdict(self))
        paths = dot_join_identifiers(paths)
        code = []
        for key in paths:
            if key.startswith("rl") or ".rl" in key:
                code.append(
                    f"{level}AssertEquals_REAL({expected}.{key}, {actual}.{key}, 0.0001, '{key} should match');\n"
                )
            else:
                code.append(
                    f"{level}AssertEquals({expected}.{key}, {actual}.{key}, '{key} should match');\n"
                )
        return code

    def to_assert_indexed(
        self, expected: str, actual: str, indent_level: int = 0
    ) -> List[str]:
        """Convert to AssertEquals"""
        level = "\t" * indent_level
        paths = get_leaf_paths(attrs.asdict(self))
        paths = dot_join_identifiers(paths)
        code = []
        for key in paths:
            if key.startswith("rl") or ".rl" in key:
                code.append(
                    f"{level}AssertEquals_REAL({expected}[ix].{key}, {actual}[ix].{key}, 0.0001, "
                    f"CONCAT('ix: ', CONCAT(TO_STRING(ix), ' {key} should match')));\n"
                )

            else:
                code.append(
                    f"{level}AssertEquals({expected}[ix].{key}, {actual}[ix].{key}, "
                    f"CONCAT('ix: ', CONCAT(TO_STRING(ix), ' {key} should match')));\n"
                )

        return code

    def to_codesys_max(self, var_name: str, indent_level: int = 0) -> List[str]:
        """Convert to codesys code"""

        code = [
            max_member_str_length(key[:-1], var_name, indent_level)
            for key in get_leaf_paths(attrs.asdict(self))
        ]
        return code

    def to_structured_data(self, var_name: str, indent_level: int = 0) -> List[str]:
        """Generate appending STU code for each struct"""
        level = "\t" * indent_level
        paths = get_leaf_paths(attrs.asdict(self))
        paths = dot_join_identifiers(paths)
        code = []
        for key in paths:
            code.append(
                f"{level}sd := Syslog.Make_SdParam2('{key}', TO_STRING({var_name}.{key}));\n"
            )
            code.append(
                f"{level}Stu.StrConcatA(pstFrom:=ADR(sd), pstTo:=ADR(AsStructuredData), iSize);\n"
            )
            code.append(
                f"{level}Stu.StrConcatA(pstFrom:=ADR(SyslogItfs.gc_sSP), pstTo:=ADR(AsStructuredData), iSize);\n"
            )
            code.append("\n")
        return code
