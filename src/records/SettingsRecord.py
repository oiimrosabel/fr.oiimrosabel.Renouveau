from gi.repository import GObject


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
