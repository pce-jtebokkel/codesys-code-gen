"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, List

"""Codesys attrs mixin and helper functions."""

def get_leaf_paths(obj: Dict[str, Any]) -> List[Any]: ...
def null_value(val: Any, member: str) -> str: ...
def assign_member(path: List[Any], var_name: str, indent_level: int) -> str: ...
def max_member_str_length(
    path_parts: List[str], var_name: str, indent_level: int
) -> str: ...
def dot_join_identifiers(
    path_leaf: List[List[str | int | float | None]],
) -> List[str]: ...

class AsCodesysMixin:
    def to_codesys(self, var_name: str, indent_level: int = ...) -> List[str]:
        """Convert to codesys code"""
        ...

    def to_assert(
        self, expected: str, actual: str, indent_level: int = ...
    ) -> List[str]:
        """Convert to AssertEquals"""
        ...

    def to_assert_indexed(
        self, expected: str, actual: str, indent_level: int = ...
    ) -> List[str]:
        """Convert to AssertEquals"""
        ...

    def to_codesys_max(self, var_name: str, indent_level: int = ...) -> List[str]:
        """Convert to codesys code"""
        ...

    def to_structured_data(self, var_name: str, indent_level: int = ...) -> List[str]:
        """Generate appending STU code for each struct"""
        ...