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
import gtk
import sys, os
from lib import *
from libu import *
from libsetting import *

class nautilus_thumbnail_setting(Set):
    @classmethod
    def f(cls):
        table = gtk.Table()
        table.set_col_spacings(10)
        
        import os
        text = label_left_align( _('The thumbnail cache directory is "%s/.thumbnails".')%os.environ['HOME'] )
        table.attach(text, 0, 2, 0, 1, gtk.FILL, gtk.FILL)
    
        label = label_left_align(_('Size of each thumbnail (in pixels):'))
        key = '/apps/nautilus/icon_view/thumbnail_size'
        label.set_tooltip_text(_('GConf key: %s')%key)
        table.attach(label, 0, 1, 1, 2, gtk.FILL, gtk.FILL)
        
        o = GConfNumericEntry(key, 16, 96)
        table.attach(o, 1, 2, 1, 2, gtk.FILL, gtk.FILL)
        
        label = label_left_align(_('Maximum size of thumbnail cache (in MBytes):'))
        key = '/desktop/gnome/thumbnail_cache/maximum_size'
        label.set_tooltip_text(_('GConf key: %s')%key)
        table.attach(label, 0, 1, 2, 3, gtk.FILL, gtk.FILL)
        
        o = GConfNumericEntry(key, 0, 2048)
        table.attach(o, 1, 2, 2, 3, gtk.FILL, gtk.FILL)
        
        label = label_left_align(_('Maximum time each thumbnail remains in cache (in days):'))
        key = '/desktop/gnome/thumbnail_cache/maximum_age'
        label.set_tooltip_text(_('GConf key: %s')%key)
        table.attach(label, 0, 1, 3, 4, gtk.FILL, gtk.FILL)
        
        o = GConfNumericEntry(key, 0, 30)
        table.attach(o, 1, 2, 3, 4, gtk.FILL, gtk.FILL)
        
        o = gtk.Button(_('Clean thumbnail image cache') + ' (%s)' % _('command: rm -rf $HOME/.thumbnails/*'))
        def clean(*w):
            os.system('rm -rf $HOME/.thumbnails/*')
            notify(_('Nautilus thumbnail image cache is clean'), ' ')
        o.connect('clicked', clean)
        table.attach(o, 0, 2, 4, 5, gtk.FILL, gtk.FILL)
        
        return table
    
    title = _('Nautilus thumbnail settings')
    category = 'nautilus'
