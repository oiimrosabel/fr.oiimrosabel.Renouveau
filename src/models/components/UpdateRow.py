from gi.repository import Adw
from gi.repository import Gtk, GObject

from .UpdateState import UpdateState

@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/updrow.ui")
class UpdateRow(Adw.ActionRow):
    __gtype_name__ = "UpdateRow"
    
    isVisible = GObject.Property(type=bool, default=True)
    isScheduled = GObject.Property(type=bool, default=False)
    isOngoing = GObject.Property(type=bool, default=False)
    isSuccess = GObject.Property(type=bool, default=False)
    isError = GObject.Property(type=bool, default=False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def setState(self, state: UpdateState):
        self.isVisible = state != UpdateState.HIDDEN
        self.isScheduled = state == UpdateState.SCHEDULED
        self.isOngoing = state == UpdateState.ONGOING
        self.isSuccess = state == UpdateState.SUCCESS
        self.setFailed(state == UpdateState.FAIL)
                
    def setFailed(self, failed: bool):
        self.isError = failed
        if failed:
            self.add_css_class("failed-sub")
        else:
            self.remove_css_class("failed-sub")
