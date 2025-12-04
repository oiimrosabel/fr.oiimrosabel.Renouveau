import html
from .CommandType import CommandType, UpdateCommandType
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
