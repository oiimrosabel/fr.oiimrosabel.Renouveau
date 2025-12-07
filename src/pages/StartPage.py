from gi.repository import Adw
from gi.repository import Gtk, GObject
import threading
import asyncio

from .FlatpakComponent import FlatpakComponent
from .SnapComponent import SnapComponent
from .SystemComponent import SystemComponent
from .SettingsComponent import SettingsComponent

from .records import FlatpakRecord, SettingsRecord, SnapRecord, SystemRecord

from .tools import Outlooker
from .OutlookerDialog import OutlookerDialog


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/start.ui")
class StartPage(Adw.NavigationPage):
    __gtype_name__ = "StartPage"

    updateClicked = GObject.Signal(
        flags=GObject.SIGNAL_RUN_FIRST,
        return_type=None,
        arg_types=(FlatpakRecord, SnapRecord, SystemRecord, SettingsRecord),
    )

    flatpakComp = Gtk.Template.Child()
    snapComp = Gtk.Template.Child()
    systemComp = Gtk.Template.Child()
    settingsComp = Gtk.Template.Child()

    toaster = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def onUpdateClicked(self, *_):
        if not self._isOneSourceSelected():
            self.toastBread("Please select at least one element to update.")
            return
        self.emit(
            "updateClicked",
            self.flatpakComp.getRecord(),
            self.snapComp.getRecord(),
            self.systemComp.getRecord(),
            self.settingsComp.getRecord(),
        )

    def _isOneSourceSelected(self):
        return (
            self.flatpakComp.flatpakEnabled
            or self.snapComp.snapEnabled
            or self.systemComp.systemEnabled
        )

    def toastBread(self, toast):
        bread = Adw.Toast()
        bread.set_title(toast)
        bread.set_timeout(2)
        self.toaster.add_toast(bread)

    @Gtk.Template.Callback()
    def initSources(self, *_):
        async def proc():
            outlooker = OutlookerDialog()
            outlooker.present(self.get_root())
            res = await Outlooker().outlook()
            outlooker.force_close()
            if not res.hasFlatpak:
                self.flatpakComp.disable()
            if not res.hasSnap:
                self.snapComp.disable()
            if res.packageManager is None:
                self.systemComp.disable()
            else:
                self.systemComp.setPackageManager(res.packageManager)

        thread = threading.Thread(target=lambda: asyncio.run(proc()))
        thread.start()
