from .CommandRepository import CommandRepository
from .CommandType import UpdateCommandType


class SnapCommands(CommandRepository):
    _name = "Snap"
    _y = "--yes"
    _sudo = "pkexec"

    _cmds = {UpdateCommandType.REG: "snap-store --quit && snap refresh"}
