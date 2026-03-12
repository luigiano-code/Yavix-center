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
		self.append(self.update_btn)


		self.system_update_btn = Gtk.Button(label="Update System")
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
		subprocess.run(["pkexec", "/usr/bin/get_update_files.sh"])
		subprocess.run(["pkexec", "chmod", "+x", "/usr/bin/update.sh"])
		subprocess.run(["pkexec", "/usr/bin/update.sh"])


	def run_update(self):
		try:
			process = subprocess.run(
				["pkexec", "pacman", "-Syu", "--noconfirm"],
			)
			process = subprocess.run(
				["flatpak", "update"]
			)
			process.wait()

		finally:
			GLib.idle_add(self.update_btn.set_sensitive, True)
