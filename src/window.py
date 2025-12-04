from gi.repository import Adw
from gi.repository import Gtk

from .StartPage import StartPage
from .UpdatePage import UpdatePage
from .FinishPage import FinishPage


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/main.ui")
class UpdaterWindow(Adw.ApplicationWindow):
    __gtype_name__ = "UpdaterWindow"

    stack = Gtk.Template.Child()
    startPage = Gtk.Template.Child()
    updatePage = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def onUpdateClicked(self, *args):
        self.updatePage.setRecords(*(args[1:]))
        self.stack.push_by_tag("update")
        self.updatePage.start()

        # TODO : canClose

        # TODO : keepState in pref
