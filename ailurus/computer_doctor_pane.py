#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Ailurus - make Linux easier to use
#
# Copyright (C) 2007-2010, Trusted Digital Technology Laboratory, Shanghai Jiao Tong University, China.
# Copyright (C) 2009-2010, Ailurus Developers Team
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
import gtk, gobject, sys, os
from lib import *
from libu import *

class ComputerDoctorPane(gtk.VBox):
    def render_type_func(self, column, cell, model, iter):
        cure_obj = model.get_value(iter, 1)
        pixbuf = [self.icon_must_fix, self.icon_suggestion][cure_obj.type]
        cell.set_property('pixbuf', pixbuf)
    def render_text_func(self, column, cell, model, iter):
        cure_obj = model.get_value(iter, 1)
        markup = '<b>%s</b>' % cure_obj.__doc__
        if cure_obj.detail: markup += '\n' + cure_obj.detail
        cell.set_property('markup', markup)
    def toggled(self, render_toggle, path, sortedstore):
        path = sortedstore.convert_path_to_child_path(path)
        self.liststore[path][0] = not self.liststore[path][0]
        sensitive = False
        for row in self.liststore:
            to_apply = row[0]
            sensitive = sensitive or to_apply
        self.button_apply.set_sensitive(sensitive)
    def sort_by_type(self, model, iter1, iter2):
        obj1 = model.get_value(iter1, 1)
        obj2 = model.get_value(iter2, 1)
        if obj1 and obj2:
            return cmp(obj1.type, obj2.type) or cmp(obj1.__doc__, obj2.__doc__)
        else:
            return 0
    def sort_by_text(self, model, iter1, iter2):
        obj1 = model.get_value(iter1, 1)
        obj2 = model.get_value(iter2, 1)
        if obj1 and obj2:
            return cmp(obj1.__doc__, obj2.__doc__)
        else:
            return 0
    def refresh(self):
        self.liststore.clear()
        for obj in self.cure_objs:
            if obj.exists():
                self.liststore.append([False, obj])
        self.sortedstore.set_sort_column_id(1000, gtk.SORT_ASCENDING)
        self.button_apply.set_sensitive(False)
    def __init__(self, cure_objs):
        self.cure_objs = cure_objs
        self.icon_must_fix = get_pixbuf(D+'sora_icons/c_must_fix.png', 24, 24)
        self.icon_suggestion = get_pixbuf(D+'sora_icons/c_suggestion.png', 24, 24)
        self.liststore = liststore = gtk.ListStore(bool, gobject.TYPE_PYOBJECT) # apply?, cure_object
        self.sortedstore = sortedstore = gtk.TreeModelSort(liststore)
        sortedstore.set_sort_func(1000, self.sort_by_type)
        sortedstore.set_sort_func(1001, self.sort_by_text)
        render_toggle = gtk.CellRendererToggle()
        render_toggle.connect('toggled', self.toggled, sortedstore)
        render_type = gtk.CellRendererPixbuf()
        render_text = gtk.CellRendererText()
        column_toggle = gtk.TreeViewColumn()
        column_toggle.pack_start(render_toggle, False)
        column_toggle.add_attribute(render_toggle, 'active', 0)
        column_toggle.set_sort_column_id(0)
        column_type = gtk.TreeViewColumn()
        column_type.pack_start(render_type, False)
        column_type.set_cell_data_func(render_type, self.render_type_func)
        column_type.set_sort_column_id(1000)
        column_text = gtk.TreeViewColumn()
        column_text.pack_start(render_text)
        column_text.set_cell_data_func(render_text, self.render_text_func)
        column_text.set_sort_column_id(1001)
        view = gtk.TreeView(sortedstore)
        view.set_rules_hint(True)
        view.append_column(column_toggle)
        view.append_column(column_type)
        view.append_column(column_text)
        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scroll.set_shadow_type(gtk.SHADOW_IN)
        scroll.add(view)
        button_refresh = image_stock_button(gtk.STOCK_REFRESH, _('Refresh'))
        button_refresh.connect('clicked', lambda *w: self.refresh())
        self.button_apply = button_apply = image_stock_button(gtk.STOCK_APPLY, _('Apply'))
        button_apply.connect('clicked', lambda *w: self.apply())
        button_apply.set_sensitive(False)
        button_box = gtk.HBox(False, 10)
        button_box.pack_start(button_refresh, False)
        button_box.pack_start(button_apply, False)
        gtk.VBox.__init__(self, False, 10)
        self.set_border_width(5)
        self.pack_start(button_box, False)
        self.pack_start(scroll)
        self.refresh()
        