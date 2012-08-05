#!/usr/bin/env python
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
import gtk, os, sys
from lib import *
from libu import *
from loader import *

def detect_running_instances():
    string = get_output('pgrep -u $USER ailurus', True)
    if string!='':
        notify(_('Warning!'), 
           _('Another instance of Ailurus is running. '
              'It is not recommended to run multiple instance concurrently.') )

def change_task_name():
    import ctypes
    libc = ctypes.CDLL('libc.so.6')
    libc.prctl(15, 'ailurus', 0, 0, 0)

def set_default_window_icon():
    pass

def with_same_content(file1, file2):
    import os
    if not os.path.exists(file1) or not os.path.exists(file2):
        return False
    with open(file1) as f:
        content1 = f.read()
    with open(file2) as f:
        content2 = f.read()
    return content1 == content2

def check_required_packages():
    debian_missing = []
    ubuntu_missing = []
    fedora_missing = []
    archlinux_missing = []

    try: import pynotify
    except: 
        debian_missing.append('python-notify')
        ubuntu_missing.append('python-notify')
        fedora_missing.append('notify-python')
        archlinux_missing.append('python-notify')
#    try: import vte
#    except: 
#        debian_missing.append('python-vte')
#        ubuntu_missing.append('python-vte')
#        fedora_missing.append('vte')
#        archlinux_missing.append('vte')
    try: import apt
    except: 
        debian_missing.append('python-apt')
        ubuntu_missing.append('python-apt')
    try: import rpm
    except: 
        fedora_missing.append('rpm-python')
    try: import gnomekeyring
    except:
        debian_missing.append('python-gnomekeyring')
        ubuntu_missing.append('python-gnomekeyring')
        fedora_missing.append('gnome-python2-gnomekeyring')
        archlinux_missing.append('python-gnomekeyring') # I am not sure. python-gnomekeyring is on AUR. get nothing from pacman -Ss python*keyring 
#    if not os.path.exists('/usr/bin/unzip'):
#        debian_missing.append('unzip')
#        ubuntu_missing.append('unzip')
#        fedora_missing.append('unzip')
#        archlinux_missing.append('unzip')
#    if not os.path.exists('/usr/bin/wget'):
#        debian_missing.append('wget')
#        ubuntu_missing.append('wget')
#        fedora_missing.append('wget')
#        archlinux_missing.append('wget')
        
    error = (
             (DEBIAN and debian_missing)
             or ((UBUNTU or UBUNTU_DERIV) and ubuntu_missing)
             or (FEDORA and fedora_missing)
             or (ARCHLINUX and archlinux_missing)
            )
    if error:
        import StringIO
        message = StringIO.StringIO()
        print >>message, _('Necessary packages are not installed. Ailurus cannot work.')
        print >>message, ''
        print >>message, _('Please install these packages:')
        print >>message, ''
        if DEBIAN:
            print >>message, '<span color="blue">', ', '.join(debian_missing), '</span>'
        elif UBUNTU or UBUNTU_DERIV:
            print >>message, '<span color="blue">', ', '.join(ubuntu_missing), '</span>'
        elif FEDORA:
            print >>message, '<span color="blue">', ', '.join(fedora_missing), '</span>'
        elif ARCHLINUX:
            print >>message, '<span color="blue">', ', '.join(archlinux_missing), '</span>'
        dialog = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK)
        dialog.set_title('Ailurus ' + AILURUS_VERSION)
        dialog.set_markup(message.getvalue())
        dialog.run()
        dialog.destroy()

def check_home_dir_permission():
    try: Config.check_permission()
    except: pass
    else: return

    import StringIO
    msg = StringIO.StringIO()
    print >>msg, _('Your home folder is not owned by yourself.\n'
                   'Please run the following command to fix the error.')
    user = os.environ['USER']
    home = os.environ['HOME']
    command = 'sudo chown -R %s:%s %s' % (user, user, home)
    print >>msg, '<span color="blue">%s</span>' % command,
    
    dialog = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK)
    dialog.set_title(_('Fatal error'))
    dialog.set_markup(msg.getvalue())
    dialog.run()
    dialog.destroy()

def wait_firefox_to_create_profile():
    if os.path.exists('/usr/bin/firefox'):
        propath = os.path.expanduser('~/.mozilla/firefox/profiles.ini')
        if not os.path.exists(propath):
            KillWhenExit.add('firefox -no-remote')
            import time
            start = time.time()
            while not os.path.exists(propath) and time.time() - start < 6:
                time.sleep(0.1)

sys.excepthook = exception_happened

class toolitem(gtk.ToolItem):
    def __init__(self, text, signal_name, callback, *callback_args):
        gtk.ToolItem.__init__(self)
        
        is_string_not_empty(text)
        is_string_not_empty(signal_name)
        assert callable(callback)
        
        label = gtk.Label()
        label.set_markup('<small>%s</small>' % text)
        self.text = text = label
        text.set_alignment(0.5, 0.5)
        text.set_justify(gtk.JUSTIFY_CENTER)
        button = gtk.Button()
        button.add(label)
        button.set_relief(gtk.RELIEF_NONE)
        button.connect(signal_name, callback, *callback_args)
        self.add(button)

class PaneLoader:
    def __init__(self, main_view, pane_class, content_function = None):
        import gobject
        assert isinstance(pane_class, gobject.GObjectMeta)
        assert callable(content_function) or content_function is None
        self.main_view = main_view
        self.pane_class = pane_class
        self.content_function = content_function
        self.pane_object = None
    def get_pane(self):
        if self.pane_object is None:
            if self.content_function: arg = [self.content_function()] # has argument
            else: arg = [] # no argument
            with TimeStat(self.pane_class.__name__):
                self.pane_object = self.pane_class(self.main_view, *arg)
        return self.pane_object
    def need_to_load(self):
        return self.pane_object is None

def create_menu_from(menuitems):
    assert isinstance(menuitems, list)
    menu = gtk.Menu()
    for item in menuitems:
        menu.append(item)
    menu.show_all()
    return menu

class DefaultPaneMenuItem(gtk.CheckMenuItem):
    def __init__(self, text, value, group):
        'text is displayed. value is saved in Config. group consists of all menu items'
        assert isinstance(text, str)
        assert isinstance(value, str)
        assert isinstance(group, list)
        for obj in group:
            assert isinstance(obj, gtk.CheckMenuItem)
        self.text = text.replace('\n', '')
        self.value = value
        self.group = group
        gtk.CheckMenuItem.__init__(self, self.text)
        self.set_draw_as_radio(True)
        self.set_active(Config.get_default_pane() == value)
        self.connect('toggled', lambda w: self.toggled())
    def toggled(self):
        if self.get_active():
            Config.set_default_pane(self.value)
            for obj in self.group:
                if obj != self:
                    obj.set_active(False)
        self.set_active(Config.get_default_pane() == self.value)

class MainView:
    def create_default_pane_menu(self):
        'Create a menu, to select default pane.'
        menuitems = []
        reversed_order = self.ordered_key[:]
        reversed_order.reverse()
        for key in reversed_order:
            pane = self.contents[key]
            assert hasattr(pane, 'pane_class') # pane is a PaneLoader object
            assert hasattr(pane.pane_class, 'text')
            item = DefaultPaneMenuItem(pane.pane_class.text, pane.pane_class.__name__, menuitems)
            menuitems.append(item)
        return create_menu_from(menuitems)
    
    def add_study_button_preference_button_other_button(self):
        item = toolitem(_('Others'), 'button_release_event', 
                        self.__show_popupmenu_on_toolbaritem, create_menu_from(load_others_menuitems()))
        self.toolbar.insert(item, 0)
        self.menu_preference = create_menu_from(load_preferences_menuitems())
        default_pane_item = gtk.MenuItem(_('Default pane'))
        default_pane_item.set_submenu(self.create_default_pane_menu())
        self.menu_preference.append(default_pane_item)
        self.menu_preference.show_all()
        item = toolitem(_('Preferences'), 'button_release_event', 
                        self.__show_popupmenu_on_toolbaritem, self.menu_preference)
        self.toolbar.insert(item, 0)

    def add_pane_buttons_in_toolbar(self):
        for key in self.ordered_key:
            pane_loader = self.contents[key]
            text = pane_loader.pane_class.text
            item = toolitem(text, 'clicked', self.activate_pane, key)
            self.toolbar.insert(item, 0)
        
        self.activate_pane(None, Config.get_default_pane())

    def get_item_icon_size(self):
        return min( int(self.last_x / 20), 48)

    def __show_popupmenu_on_toolbaritem(self, widget, event, menu):
        if event.type == gtk.gdk.BUTTON_RELEASE and event.button == 1:
            def func(menu):
                (x, y) = self.window.get_position()
                rectangle = widget.get_allocation()
                x += rectangle.x
                y += rectangle.y + rectangle.height + 20
                return (x, y, True)
            menu.popup(None, None, func, event.button, event.time)
            return True
        return False
    
    def activate_pane(self, widget, name):
        assert isinstance(name, str)
        self.current_pane = name
        for child in self.toggle_area.get_children():
            self.toggle_area.remove(child)
        pane_loader = self.contents[name]
        if pane_loader.need_to_load():
            import pango
            label = gtk.Label(_('Please wait a few seconds'))
            label.modify_font(pango.FontDescription('Sans 20'))
            self.toggle_area.add(label)
            self.toggle_area.show_all()
            while gtk.events_pending(): gtk.main_iteration()
            pane = pane_loader.get_pane() # load pane
            for child in self.toggle_area.get_children():
                self.toggle_area.remove(child)
            if hasattr(pane, 'get_preference_menuitems'): # insert preference_menuitems
                for item in pane.get_preference_menuitems():
                    self.menu_preference.append(item)
                self.menu_preference.show_all()
        self.toggle_area.add(pane_loader.get_pane())
        self.toggle_area.show_all()

    def lock(self):
        self.stop_delete_event = True
        self.toolbar.set_sensitive(False)
    
    def unlock(self):
        self.stop_delete_event = False
        self.toolbar.set_sensitive(True)

    def terminate_program(self, *w):
        if self.stop_delete_event:
            return True
        
        from support.windowpos import WindowPos
        WindowPos.save(self.window,'main')

        gtk.main_quit()
        sys.exit()

    def register(self, pane_class, content_function = None):
        import gobject
        key = pane_class.__name__
        self.contents[key] = PaneLoader(self, pane_class, content_function)
        self.ordered_key.append(key)

    def __init__(self):
        self.window = None # MainView window
        self.stop_delete_event = False
        self.contents = {}
        self.ordered_key = [] # contains keys in self.contents, in calling order of self.register
        self.menu_preference = None # "Preference" menu
        
        self.toggle_area = gtk.VBox()
        self.toggle_area.set_border_width(5)
        
        vbox = gtk.VBox(False, 0)
        
        self.toolbar = gtk.Toolbar()
        self.toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        self.toolbar.set_style(gtk.TOOLBAR_BOTH)
        vbox.pack_start(self.toolbar, False)
        vbox.pack_start(gtk.HSeparator(), False)
        vbox.pack_start(self.toggle_area, True, True)
        
        self.window = window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title('Ailurus')
        self.last_x = self.window.get_size()[0]
        window.connect("delete_event", self.terminate_program)
        window.add(vbox)

        from support.windowpos import WindowPos
        WindowPos.load(window,'main')
        
        from system_setting_pane import SystemSettingPane
#        from clean_up_pane import CleanUpPane
        from info_pane import InfoPane
#        from computer_doctor_pane import ComputerDoctorPane
#        if UBUNTU or UBUNTU_DERIV:
#            from ubuntu.repos_config_pane import ReposConfigPane
#        if FEDORA:
#            from fedora.repos_edit_pane import FedoraReposEditPane

#        self.register(ComputerDoctorPane, load_cure_objs)
#        self.register(CleanUpPane)
#        if BACKEND:
#            from snapshot_pane import SnapshotPane
#            self.register(SnapshotPane)
#        if UBUNTU or UBUNTU_DERIV:
#            self.register(ReposConfigPane)
#        if FEDORA:
#            self.register(FedoraReposEditPane)
        self.register(SystemSettingPane, load_setting)
        self.register(InfoPane, load_info)
        
        self.add_study_button_preference_button_other_button()
        self.add_pane_buttons_in_toolbar()
        self.window.show_all()
        
with TimeStat(_('start up')):
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    change_task_name()
    set_default_window_icon()
    check_home_dir_permission()
    check_required_packages()
    
    while gtk.events_pending(): gtk.main_iteration()
    main_view = MainView()

gtk.gdk.threads_init()
gtk.gdk.threads_enter()
gtk.main()
gtk.gdk.threads_leave()
sys.exit()
