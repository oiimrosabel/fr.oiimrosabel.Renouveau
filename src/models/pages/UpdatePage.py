from gi.repository import Adw
from gi.repository import Gtk, GObject

from .Terminal import Terminal
from .UpdateExpanderRow import UpdateExpanderRow
from .UpdateRow import UpdateRow

from .FlatpakRecord import FlatpakRecord
from .SettingsRecord import SettingsRecord
from .SnapRecord import SnapRecord
from .SystemRecord import SystemRecord

from .FlatpakEngine import FlatpakEngine

import threading
import asyncio


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/update.ui")
class UpdatePage(Adw.NavigationPage):
    __gtype_name__ = "UpdatePage"

    _flatpakRecord: FlatpakRecord = None
    _snapRecord: SnapRecord = None
    _systemRecord: SystemRecord = None
    _settingsRecord: SettingsRecord = None

    # _writer: LogProcessor

    showTerminal = GObject.Property(type=bool, default=False)

    terminal = Gtk.Template.Child()
    
    flatpakRow = Gtk.Template.Child()

    def setRecords(
        self,
        flatpak: FlatpakRecord,
        snap: SnapRecord,
        system: SystemRecord,
        settings: SettingsRecord,
    ):
        self._flatpakRecord = flatpak
        self._snapRecord = snap
        self._systemRecord = system
        self._settingsRecord = settings

    def _canStart(self):
        return (
            self._flatpakRecord is not None
            and self._snapRecord is not None
            and self._systemRecord is not None
            and self._settingsRecord is not None
        )

    def start(self):
        async def proc():
            try:
                await self._processFlatpak()
            except Exception as e:
                print(e)

        assert self._canStart()
        thread = threading.Thread(target=lambda: asyncio.run(proc()))
        thread.start()

    async def _processFlatpak(self):
        engine = FlatpakEngine(self._flatpakRecord, self.terminal, self.flatpakRow)
        await engine.run()

    # async def _processSnap(self):
    #     engine = SnapEngine(self._snapRecord, self.terminal)
    #     await engine.run()

    # async def _processSystem(self):
    #     engine = SystemEngine(self._systemRecord, self.terminal)
    #     await engine.run()
    
    # async def _processSettings(self):
    #     pass

    @Gtk.Template.Callback()
    def onTerminalButtonClicked(self, *_):
        self.showTerminal = not self.showTerminal
