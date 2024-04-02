"""Converter functions."""

from typing import Any


def try_float(val: str | int | float | None) -> float | None:
    """Try to convert `val` to float other wise return None."""
    try:
        return float(val)
    except Exception:
        return None


def empty_str(val: Any) -> str:
    """Empty String for `None` else ``str(val)``"""
    if val is None:
        return ""
    return str(val)
