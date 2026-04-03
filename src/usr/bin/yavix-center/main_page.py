import gi
import sys
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib

class MainPage(Gtk.Box):
	def __init__(self):
		super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
		self.set_margin_top(50)
		self.set_margin_bottom(50)
		self.set_margin_start(50)
		self.set_margin_end(50)

		welcome_label = Gtk.Label(label="Yavix Center")
		welcome_label.set_wrap(True)
		welcome_label.set_wrap_mode(Gtk.WrapMode.WORD)
		welcome_label.set_halign(Gtk.Align.CENTER)
		welcome_label.add_css_class("title-1")
		self.append(welcome_label)

		self.updater_button = Gtk.Button(label="updater")
		self.updater_button.set_halign(Gtk.Align.CENTER)
		self.updater_button.set_size_request(200, 50)
		self.append(self.updater_button)

		self.cleaner_button = Gtk.Button(label="cleaner")
		self.cleaner_button.set_halign(Gtk.Align.CENTER)
		self.cleaner_button.set_size_request(200, 50)
		self.append(self.cleaner_button)

		self.driver_button = Gtk.Button(label="install nvidia drivers")
		self.driver_button.set_halign(Gtk.Align.CENTER)
		self.driver_button.set_size_request(200, 50)
		self.append(self.driver_button)

		self.productivity_button = Gtk.Button(label="Productivity mode")
		self.productivity_button.set_halign(Gtk.Align.CENTER)
		self.productivity_button.set_size_request(200, 50)
		self.append(self.productivity_button)


