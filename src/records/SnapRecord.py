from gi.repository import GObject


class SnapRecord(GObject.Object):
    __gtype_name__ = "SnapRecord"
    snapEnabled: bool
    forceUpdate: bool

    def __init__(self, snapEnabled: bool, forceUpdate: bool):
        super().__init__()
        self.snapEnabled = snapEnabled
        self.forceUpdate = forceUpdate
