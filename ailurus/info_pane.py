#coding: utf-8
#
# Ailurus - a tool for changing hidden GNOME configuration
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
import gtk, sys, os
from lib import *
from libu import *

class InfoPane(gtk.VBox):
    text = _('Information')

    def __init__(self, main_view, infos):
        assert isinstance(infos, tuple) and len(infos) == 2
        assert isinstance(infos[0], list)
        assert isinstance(infos[1], list)
        hardware_functions, os_functions = infos
        self.hardware_functions = hardware_functions
        self.os_functions = os_functions
        for func in hardware_functions:
            func.result = func()
        for func in os_functions:
            func.result = func()
        
        self.hardware_subtree_text = _('Hardware Information')
        self.os_subtree_text = _('Linux Information')
        
        gtk.VBox.__init__(self, False, 10)
        
        self.treestore = gtk.TreeStore(gtk.gdk.Pixbuf, str, str)
        self.treeview = treeview = gtk.TreeView(self.treestore)
        column = gtk.TreeViewColumn()
        treeview.append_column(column)
        treeview.set_headers_visible(False)
        text_render = gtk.CellRendererText()
        value_render = gtk.CellRendererText()
        column.pack_start(text_render, False)
        column.add_attribute(text_render, 'text', 1)
        column.pack_start(value_render, False)
        column.add_attribute(value_render, 'text', 2)
        
        scrollwindow = gtk.ScrolledWindow ()
        scrollwindow.add (treeview)
        scrollwindow.set_policy (gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scrollwindow.set_shadow_type (gtk.SHADOW_IN)
        
        self.pack_start(scrollwindow)

        subtree_root = self.treestore.append(None, [None, self.hardware_subtree_text, None])
        for func in self.hardware_functions:
            for row in func.result:
                self.treestore.append(subtree_root, [None, row[0], row[1]])
                
        subtree_root = self.treestore.append(None, [None, self.os_subtree_text, None])
        for func in self.os_functions:
            for row in func.result:
                self.treestore.append(subtree_root, [None, row[0], row[1]])

        self.treeview.expand_all()
