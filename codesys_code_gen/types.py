"""Codesys data types/type aliases"""
from typing import Optional
from datetime import datetime


REAL = Optional[float]
LREAL = Optional[float]
DATE_AND_TIME = Optional[datetime]
DT = DATE_AND_TIME
TIME = Optional[int]
LTIME = Optional[int]
STRING = Optional[str]
WSTRING = Optional[str]
TIME = Optional[int]
LTIME = Optional[int]
BOOL = Optional[bool]

# Integer Types
BYTE = Optional[int]
WORD = Optional[int]
DWORD = Optional[int]
LWORD = Optional[int]
SINT = Optional[int]
USINT = Optional[int]
INT = Optional[int]
UINT = Optional[int]
DINT = Optional[int]
UDINT = Optional[int]
LINT = Optional[int]
ULINT = Optional[int]
UXINT = Optional[int]
XINT = Optional[int]
XWORD = Optional[int]
