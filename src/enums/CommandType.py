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
