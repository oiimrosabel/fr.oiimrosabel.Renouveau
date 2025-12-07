from gi.repository import Adw
from gi.repository import Gtk, GObject

from .enums import PackageManager, CommandType, UpdateCommandType, ExtendedCommandType
from .commands import CommandRepository, RpmCommands, PacmanCommands, AptCommands
from .records import SystemRecord


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/system.ui")
class SystemComponent(Adw.ExpanderRow):
    __gtype_name__ = "SystemComponent"

    systemEnabled = GObject.Property(type=bool, default=False)
    refreshPackages = GObject.Property(type=bool, default=True)
    updatePackages = GObject.Property(type=bool, default=True)
    deleteUnused = GObject.Property(type=bool, default=False)

    systemPresent = GObject.Property(type=bool, default=True)
    systemTitle = GObject.Property(type=str, default="System packages")
    systemSubtitle = GObject.Property(type=str, default="")

    packageManager = PackageManager.APT
    upgradeCommand = UpdateCommandType.REG

    refreshRow = Gtk.Template.Child()
    commandRow = Gtk.Template.Child()
    updateRow = Gtk.Template.Child()
    unusedRow = Gtk.Template.Child()
    commandFilter = Gtk.Template.Child()

    _commandsList = {
        PackageManager.APT: AptCommands(),
        PackageManager.RPM: RpmCommands(),
        PackageManager.PACMAN: PacmanCommands(),
    }

    _currentCommands: CommandRepository
    _currentTypes: list[CommandType] = []

    def __init__(self, **kwargs):
        self.setPackageManager(PackageManager.APT)
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def isCommandAvailable(self, item: Adw.EnumListItem):
        return item.props.value in self._currentTypes

    @Gtk.Template.Callback()
    def commandTypeLabel(self, item: Adw.EnumListItem) -> str:
        match item.props.value:
            case UpdateCommandType.REG:
                return _("Regular")
            case UpdateCommandType.EVO:
                return _("Evolutive")
            case UpdateCommandType.FULL:
                return _("Full")
            case _:
                return ""

    def setPackageManager(self, manager: PackageManager):
        self._currentCommands = self._commandsList.get(manager)
        self.packageManager = manager
        self.systemTitle = f"{self._currentCommands.getName()} packages"

        self._currentTypes = self._currentCommands.availableUpdateCommands()
        self.commandFilter.changed(Gtk.FilterChange.DIFFERENT)
        self.commandRow.set_selected(0)
        self._setCommandType(UpdateCommandType.REG)

    @Gtk.Template.Callback()
    def onCommandChange(self, e: Adw.ComboRow, *_):
        selected = self._currentTypes[e.get_selected()]
        self._setCommandType(selected)

    def _setCommandType(self, cmd: UpdateCommandType):
        self._currentType = cmd
        self._updateRefreshRow()
        self._updateUpdateRow()
        self._updateUnusedRow()

    def _updateRefreshRow(self):
        subtitle = self._currentCommands.getCommand(ExtendedCommandType.REFR)
        self.refreshPackages = self.refreshPackages and subtitle != ""
        self.refreshRow.set_subtitle(subtitle)
        self.refreshRow.set_sensitive(subtitle != "")

    def _updateUpdateRow(self):
        subtitle = self._currentCommands.getCommand(self._currentType)
        self.updatePackages = self.updatePackages and subtitle != ""
        self.updateRow.set_subtitle(subtitle)
        self.updateRow.set_sensitive(subtitle != "")

    def _updateUnusedRow(self):
        subtitle = self._currentCommands.getCommand(ExtendedCommandType.AUTO)
        self.deleteUnused = self.deleteUnused and subtitle != ""
        self.unusedRow.set_subtitle(subtitle)
        self.unusedRow.set_sensitive(subtitle != "")

    def getRecord(self):
        return SystemRecord(
            self.systemEnabled,
            self.refreshPackages,
            self.updatePackages,
            self.deleteUnused,
            self.packageManager,
            self.upgradeCommand,
        )

    def disable(self):
        self.systemEnabled = False
        self.systemPresent = False
        self.systemSubtitle = "No compatible package manager found."
