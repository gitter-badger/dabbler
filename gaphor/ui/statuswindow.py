#!/usr/bin/env python

# Copyright (C) 2010-2017 Adam Boduch <adam.boduch@gmail.com>
#                         Arjan Molenaar <gaphor@gmail.com>
#                         Dan Yeaw <dan@yeaw.me>
#
# This file is part of Gaphor.
#
# Gaphor is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# Gaphor is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaphor.  If not, see <http://www.gnu.org/licenses/>.
"""Defines a status window class for displaying the progress of
a queue."""

from __future__ import absolute_import
from gi.repository import GObject
from gi.repository import Pango
from gi.repository import Gtk

from gaphor.misc.gidlethread import QueueEmpty

class StatusWindow(object):
    """Create a borderless window on the parent, usually the main window, 
    with a label and a progress bar.  The progress bar is updated as the 
    queue is updated."""
    
    def __init__(self, title, message, parent=None, queue=None, display=True):
        """Create the status window.  The title parameter is the title of the
        window.  The message parameter is a string displayed near the progress
        bar to indicate what is happening.  The parent parameter is the
        parent window to display the window in.  The queue parameter is a
        queue that is used to update the progress bar.  The display parameter
        will display the window if true.  This is the default."""
        
        self.title = title
        self.message = message
        self.parent = parent
        self.queue = queue
        
        self.init_window()
        
        if display:
            self.display()
        
    def init_window(self):
        """Create the window GUI component.  This will set the window and
        progress bar attributes so they can be referenced later."""
        
        frame = Gtk.Frame()
        vbox = Gtk.VBox(spacing=12)
        label = Gtk.Label(label=self.message)
        
        self.progress_bar = Gtk.ProgressBar()
        self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        
        self.window.set_title(self.title)
        self.window.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
        self.set_transient_for(self.parent)
        self.window.set_modal(True)
        self.window.set_resizable(False)
        self.window.set_decorated(False)
        self.set_type_hint(Gdk.WindowTypeHint.SPLASHSCREEN)
        self.window.add(frame)
        
        self.progress_bar.set_size_request(400, -1)
        
        frame.set_shadow_type(Gtk.ShadowType.IN)
        frame.add(vbox)
        
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        
        vbox.set_border_width(12)
        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(self.progress_bar, expand=False, fill=False, padding=0)
        
    def display(self):
        """Display the status window.  If a queue has been supplied to the
        StatusWindow instance, a new gobject idle handle is created.  Once
        the window is destroyed, this handler is removed."""
        
        self.window.show_all()

        if self.queue:
            self.idle_id = GObject.idle_add(progress_idle_handler,\
                                            self.progress_bar,\
                                            self.queue,\
                                            priority=GObject.PRIORITY_LOW)
            self.window.connect('destroy', remove_idle_handler, self.idle_id)
                                            
    def destroy(self):
        """Destroy the status window.  This will also remove the gobject
        handler."""
        
        self.window.destroy()

def progress_idle_handler(progress_bar, queue):
    """This is a gobject idle handler that updates the supplied progress bar.
    The percentage is retrieved from the queue until it is empty.  The progress
    bar is then updated with the current percentage."""
    
    percentage = 0
    try:
        while True:
            percentage = queue.get()
    except QueueEmpty:
        pass
    if percentage:
        progress_bar.set_fraction(min(percentage / 100.0, 100.0))
    return True

def remove_idle_handler(window, idle_id):
    """This removes the supplied gobject idle id.  This handle is required
    by StatusWindow when it is destroyed."""
    
    GObject.source_remove(idle_id)
