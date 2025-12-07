import html

from gi.repository import Gtk

from .enums import TerminalStyle


@Gtk.Template(resource_path="/fr/oiimrosabel/Renouveau/terminal.ui")
class Terminal(Gtk.ScrolledWindow):
    __gtype_name__ = "Terminal"

    textView = Gtk.Template.Child()
    buffer: Gtk.TextBuffer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buffer = self.textView.get_buffer()

    def scrollDown(self, *_):
        scroll = self.get_vadjustment()
        if scroll is None:
            return
        scroll.set_value(scroll.get_upper())

    def write(
        self, data: str, style: TerminalStyle = TerminalStyle.DEF, separate=False
    ):
        data = html.escape(data)
        match style:
            case TerminalStyle.ERR:
                data = f'<span color="#FF8080" weight="bold">{data}</span>'
            case TerminalStyle.COM:
                data = f'<span color="#808080">{data}</span>'
            case TerminalStyle.SUC:
                data = f'<span color="#40FF40" weight="bold">{data}</span>'
            case TerminalStyle.INF:
                data = f'<span color="#B0B0FF" weight="bold">{data}</span>'
            case _:
                pass

        if separate:
            data = f"\n{data}\n\n"

        self.buffer.insert_markup(self.buffer.get_end_iter(), data, len(data))
        self.scrollDown()
