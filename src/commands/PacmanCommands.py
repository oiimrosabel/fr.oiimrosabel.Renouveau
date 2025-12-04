from .CommandRepository import CommandRepository
from .CommandType import UpdateCommandType, ExtendedCommandType


class PacmanCommands(CommandRepository):
    _name = "Pacman"
    _y = "--noconfirm"
    _sudo = "pkexec"

    _cmds = {
        UpdateCommandType.REG: "pacman -Syu",
        ExtendedCommandType.AUTO: "pacman -Qdtq | sudo pacman -Rs -",
    }
