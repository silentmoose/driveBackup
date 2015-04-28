#!/usr/bin/python
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drive Backup")
	self.start_button = Gtk.Button(label="Backup")
        self.start_button.connect("clicked", self.on_button_clicked)
        self.add(self.start_button)
	
    def on_button_clicked(self, widget):
      self.start_backup() 
    def start_backup(self):
       print("starting backup")
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


