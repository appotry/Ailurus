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
from lib import *
from libu import *

def url_button(url):
    import gtk
    def func(w, url): open_web_page(url)
    def enter(w, e): 
        try: w.get_window().set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND2))
        except AttributeError: pass
    def leave(w, e): 
        try: w.get_window().set_cursor(gtk.gdk.Cursor(gtk.gdk.LEFT_PTR))
        except AttributeError: pass
    label = gtk.Label()
    label.set_markup("<span color='blue'><u>%s</u></span>"%url)
    button = gtk.Button()
    button.connect('clicked', func, url)
    button.connect('enter-notify-event', enter)
    button.connect('leave-notify-event', leave)
    button.set_relief(gtk.RELIEF_NONE)
    button.add(label)
    align = gtk.Alignment(0, 0.5)
    align.add(button)
    return align

def version_to_tuple(string):
    return tuple(string.split('.'))

def show_about_dialog():
    import gtk
    gtk.about_dialog_set_url_hook( lambda dialog, link: 1 )
    about = gtk.AboutDialog()
    about.set_name('Ailurus')
    about.set_version(AILURUS_VERSION)
    about.set_website_label( _('Project homepage') )
    about.set_website('http://ailurus.googlecode.com/')
    about.set_authors( [
          _('Developers:'),
          'Homer Xing <homer.xing@gmail.com>', 
          'CHEN Yangyang <skabyy@gmail.com>',
          'MA Yue <velly.empire@gmail.com>',
          'HAN Haofu <gtxx3600@gmail.com>',
          _('Contributors:'),
          'QI Chengjie <starboy.qi@gmail.com>',
          'HUANG Wei <wei.kukey@gmail.com>',
          'SHANG Yuanchun <idealities@gmail.com>',
          'DU Yue <elyes.du@gmail.com>',
          'Devil Wang <wxjeacen@gmail.com>',
          'Ray Chen <chenrano2002@gmail.com>',
           ] )
    about.set_translator_credits(_('translator-credits'))
    about.set_artists( [
          'SU Yun',
          'M. Umut Pulat    http://12m3.deviantart.com/', 
          'Andrea Soragna   http://sora-meliae.deviantart.com/',
          'Paul Davey       http://mattahan.deviantart.com/',] )
    about.set_copyright(_(u"Copyright (C)") + ' Homer Xing <homer.xing@gmail.com>')
    about.set_wrap_license(False)
    about.set_license('''
Ailurus is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

The source code in Ailurus is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Ailurus; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

All images in directory "data/sona_icons" are released under the GPL License. 
Their copyright are holded by Andrea Soragna.''')
    about.vbox.pack_start( gtk.Label( _('\nThis version is released at %s.') % AILURUS_RELEASE_DATE), False)
    about.vbox.show_all()
    about.run()
    about.destroy()
