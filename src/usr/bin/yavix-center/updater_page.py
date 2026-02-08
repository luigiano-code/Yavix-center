import subprocess
import threading
from gi.repository import Gtk, GLib

class UpdaterPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.update_btn = Gtk.Button(label="Update System")
        self.update_btn.connect("clicked", self.on_update_clicked)
        self.append(self.update_btn)

        self.log_buffer = Gtk.TextBuffer()
        text_view = Gtk.TextView(buffer=self.log_buffer)
        text_view.set_editable(False)
        text_view.set_wrap_mode(Gtk.WrapMode.WORD)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled.set_vexpand(True)
        scrolled.set_min_content_height(300)
        scrolled.set_child(text_view)

        self.append(scrolled)

    def append_log(self, text):
        GLib.idle_add(lambda: self._append(text))

    def _append(self, text):
        end_iter = self.log_buffer.get_end_iter()
        self.log_buffer.insert(end_iter, text + "\n")
        mark = self.log_buffer.create_mark("end", self.log_buffer.get_end_iter(), False)
        text_view = self.get_child_by_name("log_view") 
        return False

    def on_update_clicked(self, button):
        self.update_btn.set_sensitive(False)
        self.append_log("Running: sudo pacman -Syu ...")
        threading.Thread(target=self.run_update, daemon=True).start()

    def run_update(self):
        try:
            process = subprocess.Popen(
                ["sudo", "pacman", "-Syu", "--noconfirm"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            for line in iter(process.stdout.readline, ""):
                self.append_log(line.rstrip())

            process.stdout.close()
            process.wait()

            if process.returncode == 0:
                self.append_log("Update finished successfully!")
            else:
                self.append_log(f"Update failed with code {process.returncode}")

        except Exception as e:
            self.append_log(f"Update failed: {e}")

        finally:
            GLib.idle_add(self.update_btn.set_sensitive, True)

