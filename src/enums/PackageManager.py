from gi.repository import GObject


class PackageManager(GObject.GEnum):
    __gtype_name__ = "PackageManager"

    APT = 0
    RPM = 1
    PACMAN = 2
