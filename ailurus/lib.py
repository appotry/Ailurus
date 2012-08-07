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

import os, gettext, subprocess, pickle, glob, platform, time, datetime
import term

gettext.translation('ailurus', '/usr/share/locale', fallback=True).install(names=['ngettext'])

def run(cmd):
    s = 'python %s %s' % (term.__file__, cmd)
    subprocess.call(s.split())

class RPM:
    @classmethod
    def load(cls):
        cls.installed = set()
        import rpm
        ts = rpm.TransactionSet()
        mi = ts.dbMatch()
        for h in mi:
            v = h[rpm.RPMTAG_NAME]
            cls.installed.add(v)

    @classmethod
    def change(cls, to_install, to_remove):
        if to_install:
            run('sudo yum install %s' % to_install)
        if to_remove:
            run('sudo yum remove %s' % to_remove)

class APT:
    @classmethod
    def load(cls):
        cls.installed = set()
        import apt
        cls.apt_cache = apt.cache.Cache()
        for pkg in cls.apt_cache:
            if pkg.isInstalled:
                cls.installed.add(pkg.name)

    @classmethod
    def change(cls, to_install, to_remove):
        if to_install:
            run('sudo apt-get install %s' % to_install)
        if to_remove:
            run('sudo apt-get remove %s' % to_remove)

d = platform.linux_distribution()[0]
if d in ('Debian', 'Ubuntu'):
    backend = APT
elif d in ('Fedora'):
    backend = RPM

def now(): # return current time in seconds
    return long(time.time())

def time_string(time):
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

class Snapshot:
    path = os.path.expanduser('~/.ailurus/')
    try: os.mkdir(path)
    except: pass

    def __init__(self, d):
        self.d = d
        self.filename = self.path + 's_%d' % self.d['time']
    
    def time(self):
        return self.d['time']

    @classmethod
    def new(cls, time, pkgs):
        s = Snapshot({'time': time, 'pkgs': pkgs})
        s.write()
        return s
    
    def write(self):
        with open(self.filename, 'w') as f:
            pickle.dump(self.d, f)
    
    @classmethod
    def load(cls, path):
        with open(path) as f:
            d = pickle.load(f)
        return Snapshot(d)

    def diff(self, current):
        past = self.d['pkgs']
        installed = current.difference(past)
        removed = past.difference(current)
        return installed, removed
    
    @classmethod
    def all_snapshots(cls):
        return [cls.load(p) for p in glob.glob(cls.path + 's_*')]
