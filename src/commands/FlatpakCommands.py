from .CommandRepository import CommandRepository
from .CommandType import UpdateCommandType, ExtendedCommandType


class FlatpakCommands(CommandRepository):
    _name = "Flatpak"
    _y = "--noninteractive"
    _sudo = ""

    _cmds = {
        UpdateCommandType.REG: "flatpak update",
        ExtendedCommandType.AUTO: "flatpak uninstall --unused",
        ExtendedCommandType.ORPHAN: "flatpak remove --delete-data --unused",
    }
