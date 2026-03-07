#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib
import sys


from main_page import MainPage
from updater_page import UpdaterPage
from cleaner_page import CleanerPage
from driver_page import DriverPage

class MainWindow(Gtk.ApplicationWindow):
	def __init__(self, app):
		super().__init__(application=app)
		self.stack = Gtk.Stack()
		self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		self.stack.set_transition_duration(200)

		self.set_default_size(400, 500)

		self.set_child(self.stack)

		self.main_page = MainPage()	
		self.updater_page = UpdaterPage()
		self.cleaner_page = CleanerPage()
		self.driver_page = DriverPage()

		self.stack.add_named(self.updater_page, "updater")		
		self.stack.add_named(self.cleaner_page, "cleaner")	
		self.stack.add_named(self.driver_page, "driver")
		self.stack.add_named(self.main_page, "main_page")

		self.main_page.updater_button.connect("clicked", self.show_updater_page)
		self.updater_page.back_btn.connect("clicked", self.show_main_page)

		self.main_page.cleaner_button.connect("clicked", self.show_cleaner_page)
		self.cleaner_page.back_btn.connect("clicked", self.show_main_page)

		self.main_page.driver_button.connect("clicked", self.show_driver_page)
		self.driver_page.back_btn.connect("clicked", self.show_main_page)

		self.stack.set_visible_child_name("main_page")
		
	def show_main_page(self, button):
		self.stack.set_visible_child_name("main_page")
	
	def show_updater_page(self, button):
		self.stack.set_visible_child_name("updater")
		
	def show_cleaner_page(self, button):
		self.stack.set_visible_child_name("cleaner")
		
	def show_driver_page(self, button):
		self.stack.set_visible_child_name("driver")
		
	def show_cleaner_page(self, button):
		self.stack.set_visible_child_name("cleaner")	
	def show_cleaner_page(self, button):
		self.stack.set_visible_child_name("cleaner")
class CenterApp(Adw.Application):
	def __init__(self):
		super().__init__(application_id="com.luigiano-code.Yavix-center")

	def do_activate(self):
		win = MainWindow(self)
		win.present()

if __name__ == "__main__":
	app = CenterApp()
	app.run(sys.argv)
