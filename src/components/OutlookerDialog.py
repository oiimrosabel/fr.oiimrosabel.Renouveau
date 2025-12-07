from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/outlooker.ui")
class OutlookerDialog(Adw.Dialog):
    __gtype_name__ = "OutlookerDialog"
