from gi.repository import GObject
from .enums import PackageManager, UpdateCommandType

class FlatpakRecord(GObject.Object):
    __gtype_name__ = "FlatpakRecord"

    flatpakEnabled: bool
    updateFlatpak: bool
    cleanUnused: bool
    cleanOrphan: bool

    def __init__(
        self,
        flatpakEnabled: bool,
        updateFlatpak: bool,
        cleanUnused: bool,
        cleanOrphan: bool,
    ):
        super().__init__()
        self.flatpakEnabled = flatpakEnabled
        self.updateFlatpak = updateFlatpak
        self.cleanUnused = cleanUnused
        self.cleanOrphan = cleanOrphan


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


class SettingsRecord(GObject.Object):
    __gtype_name__ = "SettingsRecord"

    canAutoReboot: bool
    canKeepLogs: bool
    canKeepAwake: bool
    ignoreErrors: bool

    def __init__(
        self,
        canAutoReboot: bool,
        canKeepLogs: bool,
        canKeepAwake: bool,
        ignoreErrors: bool,
    ):
        super().__init__()
        self.canAutoReboot = canAutoReboot
        self.canKeepLogs = canKeepLogs
        self.canKeepAwake = canKeepAwake
        self.ignoreErrors = ignoreErrors

class SnapRecord(GObject.Object):
    __gtype_name__ = "SnapRecord"
    snapEnabled: bool
    forceUpdate: bool

    def __init__(self, snapEnabled: bool, forceUpdate: bool):
        super().__init__()
        self.snapEnabled = snapEnabled
        self.forceUpdate = forceUpdate

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
