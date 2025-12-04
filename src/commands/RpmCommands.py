from .CommandRepository import CommandRepository
from .CommandType import UpdateCommandType, ExtendedCommandType


class RpmCommands(CommandRepository):
    _name = "RPM"
    _y = "-y"
    _sudo = "pkexec"

    _cmds = {
        ExtendedCommandType.REFR: "dnf check-update",
        UpdateCommandType.REG: "dnf upgrade",
        UpdateCommandType.FULL: "dnf distro-sync",
        ExtendedCommandType.AUTO: "dnf autoremove",
    }
