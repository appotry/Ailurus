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

import sys, os
import gtk, gobject
from lib import *

class _snapshot_store(gtk.ListStore):
    def __init__(self):
        gtk.ListStore.__init__(self, gobject.TYPE_PYOBJECT)
        self.set_sort_func(1000, self.sort)
        for s in Snapshot.all_snapshots():
            self.append([s])

    def sort(self, model, iter1, iter2):
        s1 = model.get_value(iter1, 0)
        s2 = model.get_value(iter2, 0)
        return cmp(s1.time(), s2.time())

    def create_snapshot_now(self):
        backend.load()
        s = Snapshot.new(now(), backend.installed)
        self.append([s])

class _snapshot_list(gtk.VBox):
    __gsignals__ = { 'snapshot_selected': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, [gobject.TYPE_PYOBJECT]), }
    
    def __init__(self, store):
        self.store = store
        
        r_date = gtk.CellRendererText()
        c_date = gtk.TreeViewColumn()
        c_date.set_title(_('Date'))
        c_date.pack_start(r_date, True)
        c_date.set_cell_data_func(r_date, self.r_time_cell_function)
        c_date.set_sort_column_id(1000)

        view = self.view = gtk.TreeView(self.store)
        view.set_rules_hint(True)
        view.append_column(c_date)
        view.get_selection().set_mode(gtk.SELECTION_SINGLE)
        view.get_selection().connect('changed', self.row_selected, view)

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.add(view)
        scroll.set_size_request(300, -1)
        
        gtk.VBox.__init__(self, False, 5)
        self.pack_start(gtk.Label(_('Existed snapshots')), False)
        self.pack_start(scroll)

    def row_selected(self, selection, treeview):
        store, itr = selection.get_selected()
        if itr == None:
            self.emit('snapshot_selected', None)
        else:
            s = store.get_value(itr, 0)
            self.emit('snapshot_selected', s)
    
    def r_time_cell_function(self, column, cell, model, itr):
        s = model.get_value(itr, 0)
        if s:
            cell.set_property('text', time_string(s.time()))

class _diff_list(gtk.VBox):
    def r_status1_cell_func(self, column, cell, model, iter):
        installed = model.get_value(iter, 1)
        if installed:
            cell.set_property('text', _('was installed'))
        else:
            cell.set_property('text', _('was removed'))

    def r_action_cell_func(self, column, cell, model, iter):
        action = model.get_value(iter, 1)
        if action:
            cell.set_property('text', _('will remove'))
        else:
            cell.set_property('text', _('will install'))

    def get_todo(self):
        return self.store2

    def __init__(self):
        from multidragview import MultiDragTreeView
        
        self.store1 = gtk.ListStore(str, bool) #package name, currently installed?
        self.store2 = gtk.ListStore(str, bool) #package name, action
                
        r_name1 = gtk.CellRendererText()
        c_name1 = gtk.TreeViewColumn(_('Software name'))
        c_name1.pack_start(r_name1)
        c_name1.add_attribute(r_name1, 'text', 0)
        c_name1.set_sort_column_id(0)
        
        r_status1 = gtk.CellRendererText()
        c_status1 = gtk.TreeViewColumn(_('Status'))
        c_status1.pack_start(r_status1)
        c_status1.set_cell_data_func(r_status1, self.r_status1_cell_func)
        c_status1.set_sort_column_id(1)
        
        self.view1 = view1 = MultiDragTreeView(self.store1)
        view1.append_column(c_name1)
        view1.append_column(c_status1)
        view1.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        scroll1 = gtk.ScrolledWindow()
        scroll1.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scroll1.set_shadow_type(gtk.SHADOW_IN)
        scroll1.add(view1)

        r_name2 = gtk.CellRendererText()
        c_name2 = gtk.TreeViewColumn(_('Software name'))
        c_name2.pack_start(r_name2)
        c_name2.add_attribute(r_name2, 'text', 0)
        c_name2.set_sort_column_id(0)

        r_action2 = gtk.CellRendererText()
        c_action2 = gtk.TreeViewColumn(_('Action'))
        c_action2.pack_start(r_action2)
        c_action2.set_cell_data_func(r_action2, self.r_action_cell_func)
        c_action2.set_sort_column_id(1)

        self.view2 = view2 = MultiDragTreeView(self.store2)
        view2.append_column(c_name2)
        view2.append_column(c_action2)
        view2.get_selection().set_mode(gtk.SELECTION_MULTIPLE)

        scroll2 = gtk.ScrolledWindow()
        scroll2.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scroll2.set_shadow_type(gtk.SHADOW_IN)
        scroll2.add(view2)
        
        TARGETS = [('treeview_row', gtk.TARGET_SAME_APP, 0)]
        view1.enable_model_drag_source(gtk.gdk.BUTTON1_MASK, TARGETS, gtk.gdk.ACTION_COPY)
        view1.enable_model_drag_dest(TARGETS, gtk.gdk.ACTION_DEFAULT)
        view1.connect('drag_data_get', self.drag_data_get_data)
        view1.connect('drag_data_received', self.drag_data_received_data_dummy)
        view2.enable_model_drag_source(gtk.gdk.BUTTON1_MASK, TARGETS, gtk.gdk.ACTION_MOVE)
        view2.enable_model_drag_dest(TARGETS, gtk.gdk.ACTION_DEFAULT)
        view2.connect('drag_data_get', self.drag_data_get_data)
        view2.connect('drag_data_received', self.drag_data_received_data)

        table = gtk.Table()
        table.set_col_spacings(30)
        table.set_row_spacings(5)
        table.attach(gtk.Label(_('Diff between now and the snapshot')), 0, 1, 0, 1, gtk.FILL, gtk.FILL)
        table.attach(gtk.Label(_('Your plan')), 1, 2, 0, 1, gtk.FILL, gtk.FILL)
        table.attach(scroll1, 0, 1, 1, 2, gtk.FILL)
        table.attach(scroll2, 1, 2, 1, 2, gtk.FILL)
        
        gtk.VBox.__init__(self, False, 5)
        self.pack_start(table)
        self.set_tooltip_text(_('Drag from left to right'))

    def show_difference(self, snapshot):
        self.store1.clear()
        if snapshot:
            try:
                backend.installed
            except:
                backend.load()
            new_installed, new_removed = snapshot.diff(backend.installed)
            for p in new_installed:
                self.store1.append([p, True])
            for p in new_removed:
                self.store1.append([p, False])
        
    def drag_data_get_data(self, treeview, context, selection, target_id, etime):
        treeselection = treeview.get_selection()
        model, pathlist = treeselection.get_selected_rows()
        import StringIO
        stream = StringIO.StringIO()
        for path in pathlist:
            pkg = model[path][0]
            print >>stream, pkg
        selection.set(selection.target, 8, stream.getvalue())

    def drag_data_received_data_dummy(self, treeview, context, x, y, selection, info, etime):
        treeselection = self.view2.get_selection()
        model, pathlist = treeselection.get_selected_rows()
        pathlist.sort()
        for path in reversed(pathlist):
            iter = model.get_iter(path)
            model.remove(iter)

    def drag_data_received_data(self, treeview, context, x, y, selection, info, etime):
        model = treeview.get_model()
        packed_value = selection.data
        data = packed_value.split('\n')[:-1]
        for name in data:
            for r in model:
                if r[0] == name: break
            else:
                for r in self.store1:
                    if name == r[0]:
                        value = r[1]; break
                model.append([name, value])

class ui(gtk.VBox):
    def apply_change(self):
        to_remove = []
        to_install = []
        for r in self.diff_list.get_todo():
            if r[1]: 
                to_remove.append(r[0])
            else: 
                to_install.append(r[0])
        backend.change(' '.join(to_install), ' '.join(to_remove))
    
    def __init__(self):
        gtk.VBox.__init__(self, False, 20)

        self.store = _snapshot_store()
        self.snapshot_list = _snapshot_list(self.store)
        self.diff_list = _diff_list()
        self.snapshot_list.connect('snapshot_selected', lambda w, sn: self.diff_list.show_difference(sn))
        
        paned = gtk.HBox(False, 20)
        paned.pack_start(self.snapshot_list, False)
        paned.pack_start(self.diff_list, False)
        
        b_add = gtk.Button(_('Make a new snapshot'))
        b_add.connect('clicked', lambda *w: self.store.create_snapshot_now())
        b_apply = gtk.Button(_('Revert back!'))
        b_apply.connect('clicked', lambda *w: self.apply_change())
        b_box = gtk.HBox(False, 10)
        b_box.pack_start(b_add, False)
        b_box.pack_end(b_apply, False)
        
        self.pack_start(paned)
        self.pack_start(b_box, False)
