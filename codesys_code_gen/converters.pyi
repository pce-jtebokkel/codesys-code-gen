"""
This type stub file was generated by pyright.
"""

from typing import Any

"""Converter functions."""

def try_float(val: str | int | float | None) -> float | None:
    """Try to convert `val` to float other wise return None."""
    ...

def empty_str(val: Any) -> str:
    """Empty String for `None` else ``str(val)``"""
    ...