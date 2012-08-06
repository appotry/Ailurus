#!/usr/bin/env python
#coding: utf-8
#
# Ailurus is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ailurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ailurus; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

from __future__ import with_statement
import gtk, os, sys
from lib import *
from libu import *
from loader import *

sys.excepthook = exception_happened

class MainView:
    def __init__(self):
        self.window = window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title('Ailurus')
        window.connect("delete_event", self.terminate_program)
        from snapshot_pane import SnapshotPane
        window.add(SnapshotPane())
        window.show_all()

    def terminate_program(self, *w):
        gtk.main_quit()
        sys.exit()
        
MainView()

gtk.gdk.threads_init()
gtk.gdk.threads_enter()
gtk.main()
gtk.gdk.threads_leave()
