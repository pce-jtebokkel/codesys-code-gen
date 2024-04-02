"""
This type stub file was generated by pyright.
"""

from typing import Optional

import attrs

from .types import REAL

@attrs.define
class VibTriAxisSimple:
    rlAxial: REAL = ...
    rlHorz: REAL = ...
    rlVert: REAL = ...

@attrs.define
class VibGroupSimple:
    de: VibTriAxisSimple = ...
    nd: VibTriAxisSimple = ...

@attrs.define
class AlarmElement:
    alarm: str = ...
    xLatch: str = ...
    iPriority: int = ...
    iGroup: int = ...
    AeClass: str = ...
    sMessage: str = ...
    reLine = ...
    reDecl = ...
    def as_declaration(self, ae_number: int = ...) -> str: ...
    @classmethod
    def from_line(cls, line):  # -> Self | None:
        ...
    @classmethod
    def from_declaration(
        cls, line: str, comment: Optional[str] = ..., gvl=...
    ):  # -> Self | None:
        ...
