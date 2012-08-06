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

from __future__ import with_statement

def install_locale():
    import gettext
    gettext.translation('ailurus', '/usr/share/locale', fallback=True).install(names=['ngettext'])

def run(command):
    string = 'python "%s/support/term.py" %s' % (A, command)

def run_as_root(cmd):
    string = 'sudo python "%s/support/term.py" %s' % (A, command)

def is_string_not_empty(string):
    if type(string)!=str and type(string)!=unicode: raise TypeError(string)
    if string=='': raise ValueError

def is32():
    import os
    return os.uname()[-1] != 'x86_64'

class RPM:
    fresh_cache = False
    __set1 = set() # __set1 consists of all installed software
    __set2 = set() # __set2 = __set1 + all available software
    @classmethod
    def cache_changed(cls):
        cls.fresh_cache = False
    @classmethod
    def refresh_cache(cls):
        if cls.fresh_cache: return
        cls.fresh_cache = True
        cls.__set1 = set()
        cls.__set2 = set()
        import subprocess, os

        path = A+'/support/dump_rpm_installed.py'
        task = subprocess.Popen(['python', path],
            stdout=subprocess.PIPE,
            )
        for line in task.stdout:
            cls.__set1.add(line.strip())
        task.wait()
    @classmethod
    def get_installed_pkgs_set(cls):
        cls.refresh_cache()
        return set(cls.__set1)

class APT:
    fresh_cache = False
    apt_get_update_is_called = False
    apt_cache = None # instance of apt.cache.Cache
    @classmethod
    def cache_changed(cls):
        cls.fresh_cache = False
    @classmethod
    def refresh_cache(cls):
        if cls.fresh_cache: return
        import apt
        try:
            cls.apt_cache = apt.cache.Cache()
            assert cls.apt_cache != None # TODO: how to cope with this error?
        except SystemError, e: # syntax error in source config
            raise APTSourceSyntaxError(*e.args)
        else:
            cls.fresh_cache = True
    @classmethod
    def get_installed_pkgs_set(cls):
        cls.refresh_cache()
        ret = set()
        for pkg in cls.apt_cache:
            if pkg.isInstalled:
                ret.add(pkg.name)
        return ret
    @classmethod
    def installed(cls, package_name):
        cls.refresh_cache()
        if not package_name in cls.apt_cache:
            return False
        p = cls.apt_cache[package_name]
        if hasattr(p, 'is_installed'):
            return p.is_installed # recommended attribute 
        else:
            return p.isInstalled # deprecated attribute

class PACMAN:
    @classmethod
    def cache_changed(cls):
        cls.fresh_cache = False
    @classmethod
    def refresh_cache(cls):
        if cls.fresh_cache: return
        cls.fresh_cache = True
        cls.__pkgs = set()
        import subprocess, os
        task = subprocess.Popen(['pacman', '-Q'],
            stdout=subprocess.PIPE,
            )
        for line in task.stdout:
            cls.__pkgs.add(line.split()[0])
        task.wait()
    @classmethod
    def get_installed_pkgs_set(cls):
        cls.refresh_cache()
        return set(cls.__pkgs)

import os

def print_traceback():
    import sys, traceback
    traceback.print_exc(file = sys.stderr)

def now(): # return current time in seconds
    import time
    return long(time.time())

def time_string(time):
    import datetime
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M')

class Snapshot:
    def __init__(self, _dict):
        assert isinstance(_dict, dict) and \
               'time' in _dict and \
               'comment' in _dict and \
               'pkgs' in _dict
        self.dict = _dict
    
    def remove(self):
        os.unlink(self.path())
    
    @classmethod
    def new_snapshot(cls):
        dict = {}
        dict['time'] = now()
        dict['comment'] = ''
        BACKEND.cache_changed() # if the system is changed outside ...
        dict['pkgs'] = BACKEND.get_installed_pkgs_set() # set
        s = Snapshot(dict)
        s.write()
        return s
    
    def path(self):
        return Config.config_dir + 'snapshot_%d' % self.time()
    
    def time(self):
        return self.dict['time']

    def comment(self):
        return self.dict['comment']

    def set_comment(self, new_comment):
        assert isinstance(new_comment, str)
        self.dict['comment'] = new_comment.replace('\n', ' ').strip()
        self.write()
    
    def write(self):
        with open(self.path(), 'w') as f:
            for k,v in self.dict.items():
                if k == 'pkgs':
                    v = ','.join(list(v))
                print >>f, '%s=%s' % (k,v)
    
    @classmethod
    def read(cls, path):
        with open(path) as f:
            lines = f.readlines()
        lines = [l.strip() for l in lines]
        lines = [l for l in lines if l]
        dict = {}
        for line in lines:
            k, v = line.split('=', 1)
            if k == 'pkgs':
                if v: v = set(v.split(','))
                else: v = set()
            elif k == 'time': v = long(v)
            dict[k] = v
        return Snapshot(dict)

    def difference(self):
        current = BACKEND.get_installed_pkgs_set()
        self_pkgs = self.dict['pkgs']
        new_installed = current.difference(self_pkgs)
        new_removed = self_pkgs.difference(current)
        return new_installed, new_removed
    
    @classmethod
    def list_snapshots(cls):
        ret = []
        import glob
        paths = glob.glob(Config.config_dir + 'snapshot_*')
        for p in paths:
            filename = os.path.basename(p)
            assert filename.startswith('snapshot_')
            time = long(filename[9:])
            ret.append(time)
        return ret
    
    @classmethod
    def get_snapshot_at(cls, time):
        path = Config.config_dir + 'snapshot_%s' % time
        return cls.read(path)
    
    @classmethod
    def all_snapshots(cls):
        ret = []
        import glob
        paths = glob.glob(Config.config_dir + 'snapshot_*')
        for p in paths:
            ret.append(cls.read(p))
        return ret

install_locale()
