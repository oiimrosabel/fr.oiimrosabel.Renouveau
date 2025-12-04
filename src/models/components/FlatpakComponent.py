from gi.repository import Adw
from gi.repository import Gtk, GObject

from .FlatpakCommands import FlatpakCommands
from .CommandType import UpdateCommandType, ExtendedCommandType

from .FlatpakRecord import FlatpakRecord


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/flatpak.ui")
class FlatpakComponent(Adw.ExpanderRow):
    __gtype_name__ = "FlatpakComponent"

    flatpakEnabled = GObject.Property(type=bool, default=False)
    updateFlatpak = GObject.Property(type=bool, default=True)
    cleanUnused = GObject.Property(type=bool, default=False)
    cleanOrphan = GObject.Property(type=bool, default=False)

    flatpakPresent = GObject.Property(type=bool, default=True)
    flatpakSubtitle = GObject.Property(type=str, default="")

    updateSubtitle = GObject.Property(type=str)
    unusedSubtitle = GObject.Property(type=str)
    orphanSubtitle = GObject.Property(type=str)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        flatpakCmds = FlatpakCommands()
        self.updateSubtitle = flatpakCmds.getCommand(UpdateCommandType.REG)
        self.unusedSubtitle = flatpakCmds.getCommand(ExtendedCommandType.AUTO)
        self.orphanSubtitle = flatpakCmds.getCommand(ExtendedCommandType.ORPHAN)

    def getRecord(self):
        return FlatpakRecord(
            self.flatpakEnabled, self.updateFlatpak, self.cleanUnused, self.cleanOrphan
        )

    def disable(self):
        self.flatpakEnabled = False
        self.flatpakPresent = False
        self.flatpakSubtitle = "Flatpak isn't installed."
