import subprocess
import threading
from gi.repository import Gtk, GLib

class UpdaterPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(50)
        self.set_margin_bottom(50)
        self.set_margin_start(50)
        self.set_margin_end(50)

        self.update_btn = Gtk.Button(label="Update")
        self.update_btn.set_halign(Gtk.Align.CENTER)
        self.update_btn.connect("clicked", self.on_update_clicked)
        self.update_btn.set_size_request(200, 50)
        self.update_btn.add_css_class("suggested-action")
        self.append(self.update_btn)


        self.system_update_btn = Gtk.Button(label="Update YavixOS")
        self.system_update_btn.set_halign(Gtk.Align.CENTER)
        self.system_update_btn.connect("clicked", self.on_system_update_clicked)
        self.system_update_btn.set_size_request(200, 50)
        self.append(self.system_update_btn)

        self.back_btn = Gtk.Button(label="Back")
        self.back_btn.set_halign(Gtk.Align.CENTER)
        self.back_btn.set_size_request(200, 50)
        self.append(self.back_btn)


    def on_system_update_clicked(self, button):
        self.system_update_btn.set_sensitive(False)
        threading.Thread(target=self.run_system_update, daemon=True).start()

    def on_update_clicked(self, button):
        self.update_btn.set_sensitive(False)
        threading.Thread(target=self.run_update, daemon=True).start()

    def run_system_update(self):
        self.system_update_btn.set_label("Checking for update")

        subprocess.run(["cp", "/etc/version.txt", "./system-version.txt"])
        subprocess.run(["curl", "-O", "https://raw.githubusercontent.com/luigiano-code/Yavix-repository/main/version.txt"])

        with open("system-version.txt", 'r') as reader:
            system_version = reader.read()

        with open("version.txt", 'r') as reader:
            version = reader.read()

        if version == system_version:
            self.system_update_btn.set_label("System is up to date")
        else:
            self.system_update_btn.set_label("Updating - Do not close the app!")
            subprocess.run(["pkexec", "/usr/bin/get_update_files.sh"])
            subprocess.run(["pkexec", "chmod", "+x", "/usr/bin/update.sh"])
            subprocess.run(["pkexec", "/usr/bin/update.sh"])

            self.system_update_btn.set_label("Updating - Do not close the app!")

        subprocess.run(["rm", "system-version.txt", "version.txt"])

    def run_update(self):
        try:
            GLib.idle_add(self.update_btn.set_label, "Updating - Do not close the app!")

            result = subprocess.run(
                ["pkexec", "pacman", "-Syu", "--noconfirm"],
                check=True,
                capture_output=True,
                text=True
            )

            result = subprocess.run(
                ["flatpak", "update", "-y"],
                check=True,
                capture_output=True,
                text=True
            )

            GLib.idle_add(self.update_btn.set_label, "Updated")

        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.strip()

            short_error = error_msg.split("\n")[-1][:100]

            GLib.idle_add(
                self.update_btn.set_label,
                f"Error: {short_error}"
            )

        finally:
            GLib.idle_add(self.update_btn.set_sensitive, True)

"""
    def run_update(self):
        try:
            self.update_btn.set_label("Updating - Do not close the app!")
            process = subprocess.run(
                ["pkexec", "pacman", "-Syu", "--noconfirm"],
            )
            process = subprocess.run(
                ["flatpak", "update"]
            )
        finally:
            self.update_btn.set_label("Updated")
            GLib.idle_add(self.update_btn.set_sensitive, True)
"""
