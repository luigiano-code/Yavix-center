import subprocess
import threading
from gi.repository import Gtk


class ProductivityPage(Gtk.Box):

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(50)
        self.set_margin_bottom(50)
        self.set_margin_start(50)
        self.set_margin_end(50
)
        self.enter_mode_btn = Gtk.Button(label="Enter productivity mode")
        self.enter_mode_btn.set_halign(Gtk.Align.CENTER)
        self.enter_mode_btn.set_size_request(200, 50)
        self.enter_mode_btn.connect("clicked", self.on_enter_mode_clicked)
        self.append(self.enter_mode_btn)

        self.exit_mode_btn = Gtk.Button(label="Exit productivity mode")
        self.exit_mode_btn.set_halign(Gtk.Align.CENTER)
        self.exit_mode_btn.set_size_request(200, 50)
        self.exit_mode_btn.connect("clicked", self.on_exit_mode_clicked)
        self.append(self.exit_mode_btn)


        self.back_btn = Gtk.Button(label="Back")
        self.back_btn.set_halign(Gtk.Align.CENTER)
        self.back_btn.set_size_request(200, 50)
        self.append(self.back_btn)

    def on_enter_mode_clicked(self, button):
        subprocess.run(["sudo", "/usr/bin/yavix-center/set_hyprland.sh"])

    def on_exit_mode_clicked(self, button):
        subprocess.run(["sudo", "/usr/bin/yavix-center/set_gnome.sh"])

