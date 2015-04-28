#!/usr/bin/python
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drive Backup")
	
	self.box = Gtk.Box(spacing=5)
	self.set_border_width(10)
	self.add(self.box)
	
	listbox = Gtk.ListBox()
	listbox.set_selection_mode(Gtk.SelectionMode.NONE)
	
	row = Gtk.ListBox()
	
	self.box.pack_start(listbox, True,True,0)
	self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        
	row.add(self.box)
	
	
	vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	self.box.pack_start(vbox, True, True, 0)
	
	homeButton = Gtk.CheckButton("Backup /home")
	vbox.pack_start(homeButton,True, True, 1)
	
	systemButton = Gtk.CheckButton("Backup /")
	vbox.pack_start(systemButton,True,True,2)
		
	self.start_button = Gtk.Button(label="Backup")
        self.start_button.connect("clicked", self.on_button_clicked)
        
	vbox.pack_start(self.start_button,True, True, 1)
	
	listbox.add(row)

	
    def on_button_clicked(self, widget):
      self.start_backup() 
    def start_backup(self):
       print("starting backup")

#init shit

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


