from gi.repository import GObject


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
