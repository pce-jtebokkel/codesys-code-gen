import re

import attrs

from .converters import try_float
from .types import REAL


@attrs.define
class VibTriAxisSimple:
    rlAxial: REAL = attrs.field(default=0.0, converter=try_float)
    rlHorz: REAL = attrs.field(default=0.0, converter=try_float)
    rlVert: REAL = attrs.field(default=0.0, converter=try_float)


@attrs.define
class VibGroupSimple:
    de: VibTriAxisSimple = attrs.field(default=VibTriAxisSimple(None))
    nd: VibTriAxisSimple = attrs.field(default=VibTriAxisSimple())


@attrs.define
class AlarmElement:
    alarm: str = attrs.field(default="")
    xLatch: str = attrs.field(default="TRUE")
    iPriority: int = attrs.field(default=1, converter=int)
    iGroup: int = attrs.field(default=1, converter=int)
    AeClass: str = attrs.field(default="")
    sMessage: str = attrs.field(default="")

    reLine: re.Pattern[str] = re.compile(
        (
            r"^.*alarm *:= *(?P<alarm>[^, ]*)[, ]*xLatch *:= *(?P<xLatch>(TRUE|FALSE))"
            r".*iPriority *:= *(?P<iPriority>[0-9]+).*iGroup *:= *(?P<iGroup>[0-9]+).*"
            r"AeClass *:= *(?P<AeClass>[^, ]*)[, ]*sMessage *:= *'(?P<sMessage>[^']*)'.*$"
        )
    )
    reDecl: re.Pattern[str] = re.compile(
        (r"^[ \t]*(?P<pre>x[tew]|lim)(?P<alarm>[^ :]+)[^/]*(//)*(?P<comment>.*)?$")
    )

    def as_declaration(self, ae_number: int = 0) -> str:
        return (
            f"ae{ae_number:03d} : PceAlarms.AlarmElement(ITFAlarmManager:=Manager, "
            f"alarm:={self.alarm}, xLatch:={self.xLatch}, pLogger:=ADR(gLog.ilogger), "
            f"iPriority:={self.iPriority}, iGroup:={self.iGroup}, AeClass:={self.AeClass}, "
            f"sMessage:='{self.sMessage}');"
        )

    @classmethod
    def from_line(cls, line: str):
        m = cls.reLine.match(line)
        if m is not None:
            return cls(**m.groupdict())
        pass

    @classmethod
    def from_declaration(
        cls, line: str, comment: str | None = None, gvl: str = "gAlarm"
    ):
        m = cls.reDecl.match(line.strip())
        if m is not None:
            if m.group("alarm") == "NULL":
                return cls(
                    alarm=f"{gvl}.{m.group('pre')}{m.group('alarm')}",
                    xLatch="FALSE",
                    iPriority=0,
                    iGroup=0,
                    AeClass="PceAlarms.AlarmClass.EMPTY",
                )
            if comment is None:
                if (c := m.group("comment")) is not None:
                    comment = c.strip()
                if comment == "":
                    comment = " ".join(
                        re.findall("^[a-z]+|[A-Z][^A-Z]*", m.group("alarm"))
                    )
            aec = "PceAlarms.AlarmClass."
            pre = m.group("pre")
            pri = 1
            grp = 1
            if pre == "xt":
                aec = f"{aec}FAULT"
                grp = 1
            elif pre == "xe":
                aec = f"{aec}ERROR"
                grp = 2
            elif pre == "xw":
                aec = f"{aec}WARNING"
                grp = 3
            else:
                aec = f"{aec}FAULT"
                grp = 4

            return cls(
                alarm=f"{gvl}.{m.group('pre')}{m.group('alarm')}",
                AeClass=aec,
                sMessage=comment or "",
                iGroup=grp,
                iPriority=pri,
            )
