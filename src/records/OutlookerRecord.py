from gi.repository import GObject
from .PackageManager import PackageManager


class OutlookerRecord(GObject.Object):
    __gtype_name__ = "OutlookerRecord"

    hasFlatpak: bool
    hasSnap: bool
    packageManager: PackageManager

    def __init__(self, hasFlatpak: bool, hasSnap: bool, packageManager: PackageManager):
        super().__init__()
        self.hasFlatpak = hasFlatpak
        self.hasSnap = hasSnap
        self.packageManager = packageManager
