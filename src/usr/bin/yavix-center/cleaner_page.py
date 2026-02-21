import subprocess
from gi.repository import Gtk


class CleanerPage(Gtk.Box):

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.cleaner_btn = Gtk.Button(label="Clean System")
        self.cleaner_btn.connect("clicked", self.on_cleaner_clicked)
        self.append(self.cleaner_btn)

        self.log_buffer = Gtk.TextBuffer()
        self.text_view = Gtk.TextView(buffer=self.log_buffer)
        self.text_view.set_editable(False)
        self.text_view.set_wrap_mode(Gtk.WrapMode.WORD)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_min_content_height(300)
        scrolled.set_child(self.text_view)

        self.append(scrolled)

    # ✅ TERAZ JEST DOBRZE
    def on_cleaner_clicked(self, button):
        subprocess.run(["pkexec", "/usr/bin/clear.sh"])
