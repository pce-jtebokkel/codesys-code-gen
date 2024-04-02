"""Codesys data types/type aliases"""

from datetime import datetime
from typing import TypeAlias

REAL: TypeAlias = float | None
LREAL: TypeAlias = float | None
DATE_AND_TIME: TypeAlias = datetime | None
DT: TypeAlias = DATE_AND_TIME
TIME: TypeAlias = int | None
LTIME: TypeAlias = int | None
STRING: TypeAlias = str | None
WSTRING: TypeAlias = str | None
BOOL: TypeAlias = bool | None

# Integer Types
BYTE: TypeAlias = int | None
WORD: TypeAlias = int | None
DWORD: TypeAlias = int | None
LWORD: TypeAlias = int | None
SINT: TypeAlias = int | None
USINT: TypeAlias = int | None
INT: TypeAlias = int | None
UINT: TypeAlias = int | None
DINT: TypeAlias = int | None
UDINT: TypeAlias = int | None
LINT: TypeAlias = int | None
ULINT: TypeAlias = int | None
UXINT: TypeAlias = int | None
XINT: TypeAlias = int | None
XWORD: TypeAlias = int | None
