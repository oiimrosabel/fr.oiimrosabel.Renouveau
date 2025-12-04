import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio, GObject
from datetime import datetime

from .window import UpdaterWindow


class UpdaterApplication(Adw.Application):
    def __init__(self):
        super().__init__(
            application_id="fr.oiimrosabel.Renouveau",
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
            resource_base_path="/fr/oiimrosabel/Renouveau",
        )

        self.create_action("preferences", self.on_preferences_action, ["<primary>p"])
        self.create_action("logs", lambda *_: print("Folder open :3"), ["<primary>l"])
        self.create_action("quit", lambda *_: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = UpdaterWindow(application=self)
        win.present()

    def on_about_action(self, *args):
        createAboutWindow().present(self.props.active_window)

    def on_preferences_action(self, widget, _):
        print("app.preferences action activated")

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def createAboutWindow():
    appName = "Renouveau"
    appIcon = "fr.oiimrosabel.Renouveau"
    appDev = "Mirabelle SALLES"
    appVer = "0.1.0"
    year = datetime.now().year

    instance = Adw.AboutDialog(
        application_name=appName,
        application_icon=appIcon,
        developer_name=appDev,
        version=appVer,
        developers=[appDev],
        designers=[appDev],
        license_type="GTK_LICENSE_GPL_3_0",
        copyright=f"© {year} {appDev}",
    )
    instance.set_translator_credits(_("translator-credits"))
    return instance


def main(version):
    app = UpdaterApplication()
    return app.run(sys.argv)
