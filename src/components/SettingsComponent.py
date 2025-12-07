from gi.repository import Adw
from gi.repository import Gtk, GObject

from .records import SettingsRecord


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/settings.ui")
class SettingsComponent(Adw.PreferencesGroup):
    __gtype_name__ = "SettingsComponent"

    canAutoReboot = GObject.Property(type=bool, default=False)
    canKeepLogs = GObject.Property(type=bool, default=False)
    canKeepAwake = GObject.Property(type=bool, default=False)
    ignoreErrors = GObject.Property(type=bool, default=False)

    def getRecord(self):
        return SettingsRecord(
            self.canAutoReboot, self.canKeepLogs, self.canKeepAwake, self.ignoreErrors
        )
