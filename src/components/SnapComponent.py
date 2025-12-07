from gi.repository import Adw
from gi.repository import Gtk, GObject

from .commands import SnapCommands
from .enums import UpdateCommandType
from .records import SnapRecord


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/snap.ui")
class SnapComponent(Adw.ExpanderRow):
    __gtype_name__ = "SnapComponent"

    snapEnabled = GObject.Property(type=bool, default=False)
    forceUpdate = GObject.Property(type=bool, default=False)

    snapPresent = GObject.Property(type=bool, default=True)
    snapSubtitle = GObject.Property(type=str, default="")

    updateSubtitle = GObject.Property(type=str)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        snapCmds = SnapCommands()
        self.updateSubtitle = snapCmds.getCommand(UpdateCommandType.REG, True)

    def getRecord(self):
        return SnapRecord(self.snapEnabled, self.forceUpdate)

    def disable(self):
        self.snapEnabled = False
        self.snapPresent = False
        self.snapSubtitle = "Snap isn't installed."
