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

def __preferences():
    menu_query_before_exit = gtk.CheckMenuItem(_('Query before exit'))
    menu_query_before_exit.set_active(Config.get_query_before_exit())
    menu_query_before_exit.connect('toggled', 
            lambda w: Config.set_query_before_exit(w.get_active()))

    return [ menu_query_before_exit ]

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
