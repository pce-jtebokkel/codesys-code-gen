"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Converter functions."""

def try_float(val) -> Optional[float]:
    """Try to convert `val` to float other wise return None."""
    ...

def empty_str(val: Any) -> str:
    """Empty String for `None` else ``str(val)``"""
    ...
