from gi.repository import Adw
from gi.repository import Gtk, GObject


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/finish.ui")
class FinishPage(Adw.NavigationPage):
    __gtype_name__ = "FinishPage"
