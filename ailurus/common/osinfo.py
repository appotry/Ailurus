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
from lib import *

def __kernel():
    ret = []
    try: ret.append( row(_('Kernel version:'), get_output('uname -r')) )
    except: print_traceback()
    
    try: ret.append( row(_('Kernel arch:'), get_output('uname -m')) )
    except: print_traceback()
    return ret

def __xorg():
    try:
        for line in get_output('Xorg -version').split('\n'):
            if line.startswith('X.Org X Server'):
                return [row(_('X server version:'), line.strip())]
    except:
        print_traceback()
        return []

def __gcc():
    try:
        return [row(_('GCC version:'), get_output('gcc -dumpversion').strip())]
    except: print_traceback()
    return []

def __java():
    try:
        import re 
        c=re.split('"', get_output('java -version'))[1]
        return [row(_('Java version:'), c)]
    except CommandFailError: pass
    except: print_traceback()
    return []

def __python():
     try: 
         return [row(_('Python version:'), sys.version.split()[0])]
     except: 
         print_traceback()
         return []
 
def __gtk():
     try:
         import gtk
         return [row(_('GTK version:'), '.'.join(map(str, gtk.gtk_version)))]
     except:
         print_traceback()
         return []
 
def __pygtk():
     try: 
         import gtk
         return [row(_('PyGTK version:'), '.'.join(map(str, gtk.pygtk_version)))]
     except: 
         print_traceback()
         return []
    
def __opengl():
    ret = []
    try:
        direct_render = vendor = vendor_version = renderer = None
        f = get_output('glxinfo')
        for line in f.split('\n'):
            v = line.split(':')
            if v[0]=='direct rendering':  direct_render = v[1].strip()
            if v[0]=='OpenGL vendor string': vendor = v[1].strip()
            if v[0]=='OpenGL version string': vendor_version = v[1].strip()
            if v[0]=='OpenGL renderer string': renderer = v[1].strip()
        if direct_render:
            ret.append( row(_('OpenGL direct rendering:'), direct_render) )
        if vendor:
            ret.append( row(_('OpenGL vendor:'), vendor) )
        if renderer:
            ret.append( row(_('OpenGL renderer:'), renderer) )
        if vendor_version:
            ret.append( row(_('OpenGL version:'), vendor_version) )

    except: 
        print_traceback()
        print >>sys.stderr, 'Command failed: glxinfo'
    return ret

def __os_version():
    try:
        import platform
        name, version = platform.dist()[0:2]
        return [row(_('%s version:') % name, version)]
    except:
        print_traceback()
        return [] 

def get():
    return [ __kernel, __xorg,
             __opengl, __gcc, __java, __python, __gtk, __pygtk, __os_version ]

if __name__ == '__main__':
    print get()
