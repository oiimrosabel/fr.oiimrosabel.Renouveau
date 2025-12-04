from .PackageManager import PackageManager
from .CommandType import UpdateCommandType

from gi.repository import GObject


class SystemRecord(GObject.Object):
    __gtype_name__ = "SystemRecord"
    systemEnabled: bool
    refreshPackages: bool
    updatePackages: bool
    deleteUnused: bool

    packageManager: PackageManager
    upgradeCommand: UpdateCommandType

    def __init__(
        self,
        systemEnabled: bool,
        refreshPackages: bool,
        updatePackages: bool,
        deleteUnused: bool,
        packageManager: PackageManager,
        upgradeCommand: UpdateCommandType,
    ):
        super().__init__()
        self.systemEnabled = systemEnabled
        self.refreshPackages = refreshPackages
        self.updatePackages = updatePackages
        self.deleteUnused = deleteUnused

        self.packageManager = packageManager
        self.upgradeCommand = upgradeCommand
