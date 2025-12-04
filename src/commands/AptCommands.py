from .CommandRepository import CommandRepository
from .CommandType import UpdateCommandType, ExtendedCommandType


class AptCommands(CommandRepository):
    _name = "APT"
    _y = "-y"
    _sudo = "pkexec"

    _cmds = {
        ExtendedCommandType.REFR: "apt update",
        UpdateCommandType.REG: "apt upgrade",
        UpdateCommandType.EVO: "apt dist-upgrade",
        UpdateCommandType.FULL: "apt full-upgrade",
        ExtendedCommandType.AUTO: "apt autoremove",
    }
