from gi.repository import Adw
from gi.repository import Gtk, GObject

from .enums import UpdateState


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/updextrow.ui")
class UpdateExpanderRow(Adw.ExpanderRow):
    __gtype_name__ = "UpdateExpanderRow"

    isVisible = GObject.Property(type=bool, default=False)
    isScheduled = GObject.Property(type=bool, default=False)
    isOngoing = GObject.Property(type=bool, default=False)
    isSuccess = GObject.Property(type=bool, default=False)
    isError = GObject.Property(type=bool, default=False)

    def getRows(self):
        rowsList = self.get_first_child().get_last_child().get_first_child()
        res = []
        x = 0
        while (value := rowsList.get_row_at_index(x)) is not None:
            res.append(value)
            x += 1
        return res

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setState(UpdateState.SCHEDULED)

    def setState(self, state: UpdateState):
        self.isVisible = state != UpdateState.HIDDEN
        self.isScheduled = state != UpdateState.SCHEDULED
        self.isOngoing = state == UpdateState.ONGOING
        self.isSuccess = state == UpdateState.SUCCESS
        self._setFailed(state == UpdateState.FAIL)

    def _setFailed(self, failed: bool):
        self.isError = failed
        if failed:
            self.add_css_class("failed")
        else:
            self.remove_css_class("failed")
