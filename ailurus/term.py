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

import os, sys, vte, gtk

class W:
    def __init__(self):
        terminal = vte.Terminal()
        terminal.connect('child-exited', self.exit) 
        self.terminal = terminal

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_position(gtk.WIN_POS_CENTER)
        window.connect('delete-event', self.exit)
        window.add(terminal)
        window.show_all()

    def exit(self, *w):
        sys.exit()

    def run(self, argv):
        msg = ' '.join(argv) + '\r\n'
        self.terminal.feed(msg)

        env = os.environ.copy()
        env['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

        pid = self.terminal.fork_command(command=argv[0], argv=argv,
                                         directory=os.getcwd(),
                                         envv=['%s=%s' % x for x in env.items()])
        if pid == -1: sys.exit()

if __name__ == '__main__':
    W().run(sys.argv[1:])
    gtk.main()
