import html
from .enums import CommandType, UpdateCommandType, ExtendedCommandType
from abc import ABC

class CommandRepository(ABC):
    _cmds: dict[CommandType, list[str]]
    _y: str
    _name: str
    _sudo: str

    def getName(self) -> str:
        return self._name

    def getCommand(self, typ: CommandType, escaped=False) -> str:
        res = self._cmds.get(typ, None)
        if res is None:
            return ""
        text = f"{self._sudo} {res} {self._y}".strip()
        if escaped:
            text = html.escape(text)
        return text

    def availableUpdateCommands(self) -> list[CommandType]:
        res = []
        for typ in UpdateCommandType:
            if self.getCommand(typ) is not None:
                res.append(typ)
        return res

    def availableCommands(self) -> list[CommandType]:
        return list(self._cmds.keys())


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


class FlatpakCommands(CommandRepository):
    _name = "Flatpak"
    _y = "--noninteractive"
    _sudo = ""

    _cmds = {
        UpdateCommandType.REG: "flatpak update",
        ExtendedCommandType.AUTO: "flatpak uninstall --unused",
        ExtendedCommandType.ORPHAN: "flatpak remove --delete-data --unused",
    }


class PacmanCommands(CommandRepository):
    _name = "Pacman"
    _y = "--noconfirm"
    _sudo = "pkexec"

    _cmds = {
        UpdateCommandType.REG: "pacman -Syu",
        ExtendedCommandType.AUTO: "pacman -Qdtq | sudo pacman -Rs -",
    }

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

class SnapCommands(CommandRepository):
    _name = "Snap"
    _y = "--yes"
    _sudo = "pkexec"

    _cmds = {UpdateCommandType.REG: "snap-store --quit && snap refresh"}
