import subprocess
import threading
from gi.repository import Gtk


class ThemePage(Gtk.Box):

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(50)
        self.set_margin_bottom(50)
        self.set_margin_start(50)
        self.set_margin_end(50)

        self.back_btn = Gtk.Button(label="Back")
        self.back_btn.set_halign(Gtk.Align.CENTER)
        self.back_btn.set_size_request(200, 50)
        self.append(self.back_btn)


