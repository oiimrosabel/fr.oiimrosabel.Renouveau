from gi.repository import GObject


class UpdateCommandType(GObject.GEnum):
    __gtype_name__ = "UpdateCommandType"

    REG = 0
    EVO = 1
    FULL = 2


class ExtendedCommandType(GObject.GEnum):
    __gtype_name__ = "ExtendedCommandType"

    REFR = 3
    AUTO = 4
    UNUSED = 4
    ORPHAN = 5


type CommandType = UpdateCommandType | ExtendedCommandType

class PackageManager(GObject.GEnum):
    __gtype_name__ = "PackageManager"

    APT = 0
    RPM = 1
    PACMAN = 2

class TerminalStyle(GObject.GEnum):
    __gtype_name__ = "TerminalStyle"

    DEF = 0
    ERR = 1
    COM = 2
    SUC = 3
    INF = 4

class UpdateState(GObject.GEnum):
    __gtype_name__ = "UpdateState"

    HIDDEN = 0
    SCHEDULED = 1
    ONGOING = 2
    SUCCESS = 3
    FAIL = 4
