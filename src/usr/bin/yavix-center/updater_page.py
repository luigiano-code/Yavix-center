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
		subprocess.run(["pkexec", "/usr/bin/get_update_files.sh"])	
		subprocess.run(["sudo", "chmod", "+x", "/usr/bin/update.sh"])	
		subprocess.run(["pkexec", "/usr/bin/update.sh"])	

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

