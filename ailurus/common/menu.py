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
import sys, os
import gtk, pango
from lib import *
from libu import *
from support.checkupdate import *

def set_proxy_server():
    proxy_string_entry = gtk.Entry()
    try:    proxy_string_entry.set_text(get_proxy_string())
    except: proxy_string_entry.set_text('')
    proxy_table = gtk.Table()
    proxy_table.set_row_spacings(5)
    proxy_table.set_col_spacings(5)
    proxy_table.attach(gtk.Label(_('Proxy string:')), 0, 1, 0, 1, gtk.FILL, gtk.FILL)
    proxy_table.attach(proxy_string_entry, 1, 2, 0, 1)
    label_example = gtk.Label()
    label_example.set_markup('<small>%s</small>'%(_('Example:') + ' http://USERNAME:PASSWORD@inproxy.sjtu.edu.cn:PORTNUMBER/'))
    label_example.set_selectable(True)
    proxy_table.attach(label_example, 1, 2, 1, 2, gtk.FILL, gtk.FILL)
    
    use_proxy = gtk.CheckButton(_('Use a proxy server'))
    def toggled(w):
        Config.set_use_proxy(w.get_active())
        proxy_table.set_sensitive(w.get_active())
        try:
            if w.get_active(): enable_urllib2_proxy()
            else:              disable_urllib2_proxy()
        except:
            print_traceback()
    use_proxy.connect('toggled', toggled)
    use_proxy.set_active(Config.get_use_proxy())
    use_proxy.toggled() # raise "toggled" signal

    dialog = gtk.Dialog(
        _('Set proxy server'), 
        None, gtk.DIALOG_MODAL|gtk.DIALOG_NO_SEPARATOR, 
        (gtk.STOCK_OK, gtk.RESPONSE_OK) )
    dialog.set_border_width(10)
    dialog.vbox.set_spacing(10)
    dialog.vbox.pack_start(use_proxy, False)
    dialog.vbox.pack_start(proxy_table, False)
    dialog.vbox.show_all()
    dialog.run()
    set_proxy_string(proxy_string_entry.get_text())
    dialog.destroy()

def __preferences():
    menu_query_before_exit = gtk.CheckMenuItem(_('Query before exit'))
    menu_query_before_exit.set_active(Config.get_query_before_exit())
    menu_query_before_exit.connect('toggled', 
            lambda w: Config.set_query_before_exit(w.get_active()))

    set_proxy = gtk.MenuItem(_('Proxy server'))
    set_proxy.connect('activate', lambda w: set_proxy_server())

    return [ set_proxy, menu_query_before_exit ]

def right_label(text):
    font = pango.FontDescription('Georgia')
    ret = gtk.Label(text)
    ret.modify_font(font)
    ret.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#667766"))
    ret.set_alignment(1, 0)
    ret.set_justify(gtk.JUSTIFY_RIGHT)
    return ret

def left_label(text):
    font = pango.FontDescription('Georgia')
    ret = gtk.Label(text)
    ret.modify_font(font)
    ret.set_alignment(0, 0.5)
    ret.set_justify(gtk.JUSTIFY_LEFT)
    ret.set_selectable(True)
    box = gtk.HBox()
    box.pack_start(ret, True, True, 6)
    return box

def url_button(url):
    import gtk, pango
    def func(w, url): open_web_page(url)
    def enter(w, e): 
        try: w.get_window().set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND2))
        except AttributeError: pass
    def leave(w, e): 
        try: w.get_window().set_cursor(gtk.gdk.Cursor(gtk.gdk.LEFT_PTR))
        except AttributeError: pass
    label = gtk.Label()
    label.set_markup("<span color='blue'><u>%s</u></span>"%url)
    font = pango.FontDescription('Georgia')
    label.modify_font(font)
    button = gtk.Button()
    button.connect('clicked', func, url)
    button.connect('enter-notify-event', enter)
    button.connect('leave-notify-event', leave)
    button.set_relief(gtk.RELIEF_NONE)
    button.add(label)
    align = gtk.Alignment(0, 0.5)
    align.add(button)
    return align

def copy_text_to_clipboard(store):
    assert isinstance(store, gtk.ListStore)

    import StringIO
    text = StringIO.StringIO()
    for row in store:
        key = row[0]
        value = row[1]
        print >>text, key
        print >>text, '\t', value
    copy_to_clipboard(text.getvalue())

def __others():
    about = gtk.MenuItem( _('About') )
    about.connect('activate', lambda *w: show_about_dialog())
    
    return [about]
   
def get_preferences_menu():
    return __preferences()

def get_others_menu():
    return __others()
