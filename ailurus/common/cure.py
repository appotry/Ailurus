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

class Create_basic_vimrc(C):
    __doc__ = _('Create basic VIM configuration file (.vimrc)')
    detail = _('File content:') + ' syntax on; set autoindent; set number; set mouse=a'
    file = os.path.expanduser('~/.vimrc')
    def exists(self):
        if UBUNTU or UBUNTU_DERIV:
            return APT.installed('vim') and not os.path.exists(self.file)
        if FEDORA:
            return RPM.installed('vim-enhanced') and not os.path.exists(self.file)
    def cure(self):
        with open(self.file, 'w') as f:
            f.write('syntax on\n'
                    'set autoindent\n'
                    'set number\n'
                    'set mouse=a\n')

class Query_before_remove_a_lot_of_files(C) :
    __doc__ = _('Query you before delete more than three files in BASH')
    detail = _('Prevent destruction when you mistype "rm subdir/*" as "rm subdir/ *".\n'
               'Add this line into $HOME/.bashrc: alias rm="rm -I"')
    bashrc = os.path.expanduser('~/.bashrc')
    line = "alias rm='rm -I'"
    def exists(self):
        return not file_contain(self.bashrc, self.line)
    def cure(self):
        file_append(self.bashrc, self.line)
