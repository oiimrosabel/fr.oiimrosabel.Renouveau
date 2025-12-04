from gi.repository import GObject


class TerminalStyle(GObject.GEnum):
    __gtype_name__ = "TerminalStyle"

    DEF = 0
    ERR = 1
    COM = 2
    SUC = 3
    INF = 4
