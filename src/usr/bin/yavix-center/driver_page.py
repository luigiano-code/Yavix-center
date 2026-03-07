import subprocess
from gi.repository import Gtk


class DriverPage(Gtk.Box):
	def __init__(self):
		super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
		self.set_margin_top(50)
		self.set_margin_bottom(50)
		self.set_margin_start(50)
		self.set_margin_end(50
)
		self.driver_btn = Gtk.Button(label="Install NVIDIA drivers")
		self.driver_btn.set_halign(Gtk.Align.CENTER)
		self.driver_btn.set_size_request(200, 50)
		self.driver_btn.connect("clicked", self.on_driver_clicked)
		self.append(self.driver_btn)

		self.back_btn = Gtk.Button(label="Back")
		self.back_btn.set_halign(Gtk.Align.CENTER)
		self.back_btn.set_size_request(200, 50)
		self.append(self.back_btn)

	def open_gpu_detected(self):
		dialog = Gtk.Dialog(title="Dialog")
		dialog.set_transient_for(self.get_root())

		box = dialog.get_content_area()
		label = Gtk.Label(label="Installing NVIDIA drivers...")
		box.append(label)

		dialog.show()


	def open_no_gpu_detected(self):
		dialog = Gtk.Dialog(title="Dialog")
		dialog.set_transient_for(self.get_root())

		dialog.add_button("OK", Gtk.ResponseType.OK)

		box = dialog.get_content_area()
		label = Gtk.Label(label="No NVIDIA GPU detected")
		box.append(label)

		dialog.connect("response", self.on_response)
		dialog.show()
		subprocess.run(["sudo", "pacman", "-S", "nvidia-dkms", "nvidia-utils", "nvidia-settings", "--noconfirm"])
		dialog.close()

	def on_response(self, dialog, response):
		dialog.close()

	def on_driver_clicked(self, button):
		output = subprocess.check_output(["lspci"], text=True)

		if not("NVIDIA" in output):
			self.open_gpu_detected()
		else:
			self.open_no_gpu_detected()



