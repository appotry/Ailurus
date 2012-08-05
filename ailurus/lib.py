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

def get_ailurus_path():
    import os
    return os.path.dirname(os.path.abspath(__file__))

try:
    A = get_ailurus_path()
except: # raise exception in python console because __file__ is not defined
    import os
    A = os.path.expanduser('~/workspace/Ailurus/ailurus/')
    assert os.path.exists(A), 'Please put ailurus code in $HOME/workspace/Ailurus/'
D = A + '/icons/'

def row(text, value, icon = None, tooltip = None): # only used in hardwareinfo.py and osinfo.py
    assert icon is None # do not display icon anymore
    return (text, value, icon, tooltip)

class C:
    this_is_a_cure = True
    MUST_FIX, SUGGESTION = range(2)
    type = SUGGESTION
    detail = ''
    def exists(self):
        raise NotImplementedError
    def cure(self):
        raise NotImplementedError
    
class Config:
    import os
    config_dir = os.path.expanduser('~/.config/ailurus/')
    @classmethod
    def make_config_dir(cls):
        import os
        dir = os.path.expanduser('~/.config/ailurus/')
        if not os.path.exists(dir): # make directory
            os.makedirs(dir)
    @classmethod
    def init(cls):
        assert not hasattr(cls, 'inited')
        cls.inited = True
        # create parser object
        import ConfigParser, os
        cls.parser = ConfigParser.RawConfigParser()
        # read configuration file if it exists
        cls.make_config_dir()
        path = cls.config_dir + 'conf'
        if os.path.exists(path):
            cls.parser.read(path)
    @classmethod
    def save(cls):
        cls.make_config_dir()
        try:
            with open(cls.config_dir + 'conf' , 'w') as f:
                cls.parser.write(f)
        except:
            print_traceback()
    @classmethod
    def set_string(cls, key, value):
        assert isinstance(key, str) and key
        assert isinstance(value, (str,unicode))  and value
        cls.parser.set('DEFAULT', key, value)
        cls.save()
    @classmethod
    def get_string(cls, key):
        assert isinstance(key, str) and key
        return cls.parser.get('DEFAULT', key)
    @classmethod
    def set_int(cls, key, value):
        assert isinstance(key, str) and key
        assert isinstance(value, int), type(value)
        cls.parser.set('DEFAULT', key, value)
        cls.save()
    @classmethod
    def get_int(cls, key):
        assert isinstance(key, str) and key
        value = cls.parser.get('DEFAULT', key)
        return int(value)
    @classmethod
    def set_long(cls, key, value):
        assert isinstance(key, str) and key
        assert isinstance(value, long), type(value)
        cls.parser.set('DEFAULT', key, value)
        cls.save()
    @classmethod
    def get_long(cls, key):
        assert isinstance(key, str) and key
        value = cls.parser.get('DEFAULT', key)
        return long(value)
    @classmethod
    def set_bool(cls, key, value):
        assert isinstance(key, str) and key
        assert isinstance(value, bool)
        cls.parser.set('DEFAULT', key, value)
        cls.save()
    @classmethod
    def get_bool(cls, key):
        assert isinstance(key, str) and key
        value = cls.parser.get('DEFAULT', key)
        value = str(value)
        return value=='True' or value=='true'
    @classmethod
    def is_Ubuntu(cls):
        import os
        if not os.path.exists('/etc/lsb-release'): 
            return False
        with open('/etc/lsb-release') as f:
            c = f.read()
        return 'Ubuntu' in c
    @classmethod
    def get_Ubuntu_version(cls):
        '''return 'hardy', 'intrepid', 'jaunty', 'karmic', 'lucid' ...'''
        with open('/etc/lsb-release') as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith('DISTRIB_CODENAME='):
                return line.split('=')[1].strip()
    @classmethod
    def get_all_Ubuntu_versions(cls):
        return ['hardy', 'intrepid', 'jaunty', 'karmic', 'lucid', 'maverick']
    @classmethod
    def is_Mint(cls):
        import os
        if not os.path.exists('/etc/lsb-release'): return False
        with open('/etc/lsb-release') as f:
            c = f.read()
        return 'LinuxMint' in c
    @classmethod
    def get_Mint_version(cls):
        with open('/etc/lsb-release') as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith('DISTRIB_RELEASE='):
                a = line.split('=')[1].strip()
        return a
    @classmethod
    def is_Fedora(cls):
        import os
        return os.path.exists('/etc/fedora-release')
    @classmethod
    def get_Fedora_version(cls):
        with open('/etc/fedora-release') as f:
            c = f.read()
        return c.split()[2].strip()
    @classmethod
    def is_ArchLinux(cls): # There is no get_arch_version, since ArchLinux has no version.
        import os
        return os.path.exists('/etc/arch-release')
    @classmethod
    def is_Debian(cls):
        import platform
        return platform.dist()[0] == 'debian'
    @classmethod
    def get_Debian_version(cls):
        'return "5.*"'
        import platform
        return platform.dist()[1]

class UserDeniedError(Exception):
    'User has denied keyring authentication'

def install_locale():
    import gettext
    gettext.translation('ailurus', '/usr/share/locale', fallback=True).install(names=['ngettext'])

class CommandFailError(Exception):
    'Fail to execute a command'

def run(command, ignore_error=False):
    is_string_not_empty(command)
    if not isinstance(ignore_error,  bool): raise TypeError

    if getattr(run, 'terminal', None):
        assert run.terminal.__class__.__name__ == 'Terminal'
        try:
            run.terminal.run(command)
        except CommandFailError:
            if not ignore_error: raise
    else:
        print '\x1b[1;33m', _('Run command:'), command, '\x1b[m'
        import os, subprocess
        env = None
        task = subprocess.Popen(command, env=env, shell=True)
        task.wait()
        if task.returncode and ignore_error == False:
            raise CommandFailError(command, task.returncode)

def packed_env_string():
    import os
    env = dict( os.environ )
    env['PWD'] = os.getcwd()
    return repr(env)

def daemon():
    return None

def get_dbus_daemon_version():
    ret = daemon().get_version(dbus_interface='com.googlecode.ailurus.Interface')
    return ret    

def get_authentication_method():
    ret = daemon().get_check_permission_method(dbus_interface='com.googlecode.ailurus.Interface')
    ret = int(ret)
    return ret

def authenticate():
    pass

def spawn_as_root(command):
    is_string_not_empty(command)
    
    authenticate()
    daemon().spawn(command, packed_env_string(), dbus_interface='com.googlecode.ailurus.Interface')

class AccessDeniedError(Exception):
    'User press cancel button in policykit window'

def run_as_root(cmd, ignore_error=False):
    is_string_not_empty(cmd)
    assert isinstance(ignore_error, bool)
    
    print '\x1b[1;33m', _('Run command:'), cmd, '\x1b[m'
    authenticate()

def is_string_not_empty(string):
    if type(string)!=str and type(string)!=unicode: raise TypeError(string)
    if string=='': raise ValueError

def get_output(cmd, ignore_error=False):
    is_string_not_empty(cmd)
    assert isinstance(ignore_error, bool)
    
    import commands
    status, output=commands.getstatusoutput(cmd)
    if status and not ignore_error: raise CommandFailError(cmd, output) # help to fix issue 1092
    return output
    
class TempOwn:
    def __init__(self,path):
        is_string_not_empty(path)
        if path[0]=='-':
            raise ValueError
        import os
        dirname = os.path.dirname(os.path.abspath(path))
        if not os.path.exists(dirname):
            run_as_root('mkdir "%s"'%dirname)
        if not os.path.exists(path):
            run_as_root('touch "%s"'%path)
        run_as_root('chown $USER:$USER %s'%path )
        self.path = path
    def __enter__(self):
        return None
    def __exit__(self, type, value, traceback):
        run_as_root('chown root:root %s'%self.path)

def notify(title, content):
    'Show a notification in the right-upper corner.'
    # title must not be empty. 
    # otherwise, this error happens. notify_notification_update: assertion `summary != NULL && *summary != '\0'' failed
    assert isinstance(title, str) and title
    assert isinstance(content, str)
    try:
        import pynotify
        if not hasattr(notify,'ailurus_notify'):
            notify.ailurus_notify = pynotify.Notification(' ',' ')
        if title == notify.ailurus_notify.get_property('summary'):
            notify.ailurus_notify = pynotify.Notification(title, content)
            notify.ailurus_notify.set_hint_string("x-canonical-append", "")
        else:
            notify.ailurus_notify.update(title, content)
               
        notify.ailurus_notify.set_timeout(10000)
        notify.ailurus_notify.show()
    except:
        print_traceback()

def is32():
    import os
    return os.uname()[-1] != 'x86_64'

def file_contain(path, *lines):
    'Return True if the file contains all the lines'
    is_string_not_empty(path)
    if not len(lines): raise ValueError
    for line in lines:
        is_string_not_empty(line)
    import os
    if os.path.exists(path):
        with open(path, 'r') as f:
            contents = f.readlines()
        for line in lines:
            if line[-1]!='\n': line+='\n'
            if not line in contents: return False
        return True
    return False

def file_insert(path, *args):
    'Insert lines into file. The format of args is "position, line, position, line..."'
    is_string_not_empty(path)
    if not len(args): raise ValueError
    for i in range(0, len(args), 2):
        if type(args[i])!=int: raise TypeError
        is_string_not_empty(args[i+1])
    
    import os
    if not os.path.exists(path):
        run('touch %s'%path)
    with open(path, "r") as f:
        contents = f.readlines()
    for i in range(0, len(args), 2):
        line = args[i]
        string = args[i+1]
        if string[-1]!='\n': string+='\n'
        contents.insert(line, string)
    with open(path, "w") as f:
        f.writelines(contents)

def file_append(path, *lines):
    is_string_not_empty(path)
    if not len(lines): raise ValueError
    for line in lines:
        is_string_not_empty(line)
    with open(path, 'a') as f:
        for line in lines:
            if line[-1]!='\n': line+='\n'
            f.write(line)

def file_remove(path, *lines):
    is_string_not_empty(path)
    if not len(lines): raise ValueError
    for line in lines:
        is_string_not_empty(line)
    with open(path, "r") as f:
        contents = f.readlines()
    for line in lines:
        if line[-1]!='\n': line+='\n'
        try: 
            contents.remove(line)
        except ValueError: pass
    with open(path, "w") as f:
        f.writelines(contents)

def free_space(path):
    is_string_not_empty(path)
    assert path[0]=='/'
    import os, statvfs
    e = os.statvfs(path)
    return e[statvfs.F_BAVAIL] * e[statvfs.F_BSIZE]

def own_by_user(*paths):
    if not len(paths): raise ValueError
    for path in paths:
        is_string_not_empty(path)
        if path[0]=='-': raise ValueError
    for path in paths:
        import os
        if os.stat(path).st_uid != os.getuid():
            run_as_root('chown $USER:$USER "%s"'%path)

def is_pkg_list(packages):
    if not len(packages): raise ValueError
    for package in packages:
        is_string_not_empty(package)
        if package[0]=='-': raise ValueError
        if ' ' in package: raise ValueError

def run_as_root_in_terminal(command, ignore_error=False):
    is_string_not_empty(command)
    print '\x1b[1;33m', _('Run command:'), command, '\x1b[m'
    string = 'python "%s/support/term.py" %s' % (A, command)

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
        
        path = A+'/support/dump_rpm_existing_new.py'
        task = subprocess.Popen(['python', path],
            stdout=subprocess.PIPE,
            )
        for line in task.stdout:
            cls.__set2.add(line.strip())
        task.wait()
    @classmethod
    def get_installed_pkgs_set(cls):
        cls.refresh_cache()
        return set(cls.__set1)
    @classmethod
    def get_existing_pkgs_set(cls):
        cls.refresh_cache()
        return set(cls.__set2)
    @classmethod
    def exist(cls, package_name):
        cls.refresh_cache()
        return package_name in cls.__set1 or package_name in cls.__set2
    @classmethod
    def installed(cls, package_name):
        is_pkg_list([package_name])
        cls.refresh_cache()
        return package_name in cls.__set1
    @classmethod
    def install(cls, *package):
        cls.cache_changed()
        run_as_root_in_terminal('yum install %s -y' % ' '.join(package))
    @classmethod
    def install_local(cls, path):
        assert isinstance(path, str)
        import os
        assert os.path.exists(path)
        cls.cache_changed()
        run_as_root_in_terminal('yum localinstall "%s" --nogpgcheck -y' % path)
    @classmethod
    def remove(cls, *package):
        cls.cache_changed()
        run_as_root_in_terminal('yum remove %s -y' % ' '.join(package))
    @classmethod
    def import_key(cls, path):
        assert isinstance(path, str)
        run_as_root_in_terminal('rpm --import %s' % path)

class APTSourceSyntaxError(Exception):
    pass

class APT:
    fresh_cache = False
    apt_get_update_is_called = False
    apt_cache = None # instance of apt.cache.Cache
    @classmethod
    def cache_changed(cls):
        cls.fresh_cache = False
    @classmethod
    def get_pkg_summary(cls, name):
        assert isinstance(name, str) and name
        cls.refresh_cache()
        return cls.apt_cache[name].summary
    @classmethod
    def has_broken_dependency(cls):
        cls.refresh_cache()
        try:
            return bool(cls.apt_cache.broken_count)
        except AttributeError: # ubuntu hardy
            return False # not a good solution
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
    def get_existing_pkgs_set(cls):
        cls.refresh_cache()
        ret = set()
        for pkg in cls.apt_cache:
            ret.add(pkg.name)
        return ret
    @classmethod
    def get_autoremovable_pkgs(cls):
        cls.refresh_cache()
        ret = []
        for pkg in cls.apt_cache:
            if hasattr(pkg, 'is_auto_removable'): auto_removable = pkg.is_auto_removable
            elif hasattr(pkg, 'isAutoRemovable'): auto_removable = pkg.isAutoRemovable # deprecated
            elif pkg.isInstalled and pkg._depcache.IsGarbage(pkg._pkg): auto_removable = True
            else: auto_removable = False
            
            if auto_removable:
                if hasattr(pkg, 'versions'): # recommended
                    version = pkg.versions[0]
                    installed_size = version.installed_size
                    summary = version.summary
                else: # deprecated
                    installed_size = pkg.installedSize
                    summary = pkg.summary
                ret.append([pkg.name, long(installed_size), summary.replace('\n', ' ')])
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
    @classmethod
    def exist(cls, package_name):
        cls.refresh_cache()
        return package_name in cls.apt_cache
    @classmethod
    def install(cls, *packages):
        is_pkg_list(packages)
        cls.apt_get_update()
        cls.cache_changed()
        run_as_root_in_terminal('apt-get install %s' % ' '.join(packages))
    @classmethod
    def remove(cls, *packages):
        is_pkg_list(packages)
        cls.cache_changed()
        run_as_root_in_terminal('apt-get remove %s' % ' '.join(packages))
    @classmethod
    def neet_to_run_apt_get_update(cls):
        cls.apt_get_update_is_called = False
    @classmethod
    def apt_get_update(cls):
        if cls.apt_get_update_is_called == False:
            run_as_root_in_terminal('apt-get update', ignore_error = True)
            cls.apt_get_update_is_called = True
            cls.cache_changed()
    @classmethod
    def install_local(cls, *packages):
        cls.cache_changed()
        for package in packages:
            run_as_root('gdebi-gtk "%s"' % package) # FIXME
    @classmethod
    def is_cache_lockable(cls):
        return None

class CannotLockAptCacheError(Exception):
    'Cannot lock apt cache'

class PACMAN:
    fresh_cache = False
    pacman_sync_called = False
    __pkgs = set()
    __allpkgs = set()
    @classmethod
    def cache_changed(cls):
        cls.fresh_cache = False
    @classmethod
    def refresh_cache(cls):
        if cls.fresh_cache: return
        cls.fresh_cache = True
        cls.__pkgs = set()
        cls.__allpkgs = set()
        import subprocess, os
        task = subprocess.Popen(['pacman', '-Q'],
            stdout=subprocess.PIPE,
            )
        for line in task.stdout:
            cls.__pkgs.add(line.split()[0])
        task.wait()
        
        task = subprocess.Popen(['pacman', '-Sl'],
            stdout=subprocess.PIPE,
            )
        for line in task.stdout:
            cls.__allpkgs.add(line.split()[1])
        task.wait()
    @classmethod
    def get_installed_pkgs_set(cls):
        cls.refresh_cache()
        return set(cls.__pkgs)
    @classmethod
    def get_existing_pkgs_set(cls):
        cls.refresh_cache()
        return set(cls.__allpkgs)
    @classmethod
    def installed(cls, package_name):
        cls.refresh_cache()
        return package_name in cls.__pkgs
    @classmethod
    def exist(cls, package_name):
        cls.refresh_cache()
        return package_name in cls.__pkgs or package_name in cls.__allpkgs
    @classmethod
    def install(cls, *packages):
        is_pkg_list(packages)
        if not cls.pacman_sync_called:
            cls.pacman_sync()
        cls.cache_changed()
        run_as_root_in_terminal('pacman -S %s' % ' '.join(packages))
    @classmethod
    def install_local(cls, path):
        assert isinstance(path, str)
        import os
        assert os.path.exists(path)
        cls.cache_changed()
        run_as_root_in_terminal('pacman -U "%s"' % path)
    @classmethod
    def remove(cls, *packages):
        is_pkg_list(packages)
        packages = [p for p in packages if PACMAN.installed(p)]
        cls.cache_changed()
        run_as_root_in_terminal('pacman -R %s' % ' '.join(packages))
    @classmethod
    def pacman_sync(cls):
        print '\x1b[1;36m', _('Run "pacman -Sy". Please wait for a few minutes.'), '\x1b[m'
        run_as_root_in_terminal('pacman -Sy')
        cls.pacman_sync_called = True

def get_response_time(url):
    is_string_not_empty(url)

    import urllib2
    import time
    import sys
    begin = time.time()
    if sys.version_info[:2]>(2,5): # for python 2.6+
        urllib2.urlopen(url, timeout=3)
    else: # for python 2.5
        urllib2.urlopen(url) # FIXME: no timeout!
    end = time.time()
    return (end - begin) * 1000 # in milliseconds

def derive_size(size):
    if not ( isinstance(size, int) or isinstance(size, long) ): raise TypeError
    if not size>=0: raise ValueError
    _1G = 1e9
    _1M = 1e6
    _1K = 1e3
    if size>=_1G:
        return _('%.1f GB') % ( size/_1G )
    if size>=_1M:
        return _('%.1f MB') % ( size/_1M )
    if size>=_1K:
        return _('%.1f KB') % ( size/_1K )
    return _('%s bytes') % int(size)

def derive_time(time):
    if not isinstance(time, int): raise TypeError
    if not time>=0: raise ValueError
    _1h = 3600.
    _1m = 60.
    if time >= _1h:
        return _('%.1f hours') % ( time/_1h )
    if time >= _1m:
        return _('%.1f minutes') % ( time/_1m )
    return _('%d seconds') % time

class KillWhenExit:
    task_list = []
    @classmethod
    def add(cls, task):
        import subprocess
        if not isinstance(task, (str, unicode, subprocess.Popen)): raise TypeError
        if isinstance(task, (str, unicode)):
            assert task!=''
            print '\x1b[1;33m', _('Run command:'), task, '\x1b[m' 
            task=subprocess.Popen(task, shell=True)
        cls.task_list.append(task)
    @classmethod
    def kill_all(cls):
        for task in cls.task_list:
            try:
                import os, signal
                os.kill(task.pid, signal.SIGTERM)
            except:
                print_traceback()
        cls.task_list = []

class CannotDownloadError(Exception):
    pass

class UserCancelInstallation(Exception):
    pass

def report_bug(*w):
    page = 'http://code.google.com/p/ailurus/issues/entry'
    notify( _('Opening web page'), page)
    KillWhenExit.add('xdg-open %s'%page)

import os

def print_traceback():
    import sys, traceback
    traceback.print_exc(file = sys.stderr)

class FedoraReposSection:
    def _set(self, lines):
        self.name = lines[0][1:-1]

        self.dict = {}
        for l in lines[1:]:
            try:
                k, v = l.split('=', 1)
            except ValueError: # no '='
                self.dict[l] = ''
            else:
                self.dict[k] = v
        
    def __init__(self, lines, parent):
        assert isinstance(parent, FedoraReposFile)
        self.parent = parent # for delete section
        assert isinstance(lines, list) and lines[0].startswith('[')
        for l in lines: assert not l.endswith('\n')
        self._set(lines)
    
    def set_new_content_as(self, new_content):
        assert isinstance(new_content, str)
        lines = new_content.split('\n')
        lines = [l for l in lines if l]
        self._set(lines)
    
    def to_string(self):
        import StringIO
        stream = StringIO.StringIO()
        print >>stream, '[%s]' % self.name
        for k, v in self.dict.items():
            print >>stream, '%s=%s' % (k, v)
        return stream.getvalue()
        
    def write(self, stream):
        stream.write(self.to_string())

    def is_main_repos(self):
        if 'gpgkey' in self.dict:
            v = self.dict['gpgkey']
            return v == 'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$basearch'
        return False

    def enabled(self):
        if 'enabled' in self.dict and self.dict['enabled']:
            v = self.dict['enabled']
            return v == '1' or v == 'True' or v == 'true'
        else:
            return False

    def set_enabled(self, value):
        if value: self.dict['enabled'] = '1'
        else: self.dict['enabled'] = '0'
        
    def delete(self):
        self.parent.delete_section(self)

class FedoraReposFile:
    def __init__(self, path):
        assert isinstance(path, str)
        self.path = path
        self.sections = []
        if os.path.exists(path):
            with open(path) as f:
                contents = f.readlines()
            contents = [l for l in contents if not l.startswith('#') and l.strip()!=''] # skip comments and blank lines at the beginning
            contents = [l.strip() for l in contents] # strip \n
            lines = []
            for line in contents:
                if line.startswith('[') and lines: # a new section starts
                    section = FedoraReposSection(lines, parent=self)
                    self.sections.append(section)
                    lines = []
                lines.append(line)
            section = FedoraReposSection(lines, parent=self)
            self.sections.append(section)

    def filename(self):
        return os.path.basename(self.path)

    @classmethod
    def full_path(cls, filename):
        assert isinstance(filename, str) and filename and not ' ' in filename
        return '/etc/yum.repos.d/%s' % filename

    @classmethod
    def all_repo_objs(cls):
        import glob
        paths = glob.glob('/etc/yum.repos.d/*.repo')
        return [FedoraReposFile(p) for p in paths]
        
    def write(self):
        if self.sections:
            with TempOwn(self.path):
                with open(self.path, 'w') as f:
                    for s in self.sections:
                        s.write(f)
        else: # no section. remove file
            if os.path.exists(self.path):
                run_as_root('rm -f "%s"' % self.path)

    def delete_section(self, section):
        assert section.parent == self
        assert section in self.sections
        self.sections.remove(section)

    def get_section(self, name):
        assert isinstance(name, str)
        for s in self.sections:
            if s.name == name: return s
        return None
    
    def has_section(self, name):
        assert isinstance(name, str)
        for s in self.sections:
            if s.name == name: return True
        return False

    def append_section(self, section):
        assert isinstance(section, FedoraReposSection)
        assert not section in self.sections
        self.sections.append(section)

def debian_installation_command(package_names):
    return 'apt-get install ' + package_names

def fedora_installation_command(package_names):
    return 'yum install ' + package_names

def archlinux_installation_command(package_names):
    return 'pacman -S ' + package_names

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

Config.init()

install_locale()

import atexit
atexit.register(KillWhenExit.kill_all)

try:
    import pynotify
    pynotify.init('Ailurus')
except:
    print 'Cannot init pynotify'

UBUNTU = Config.is_Ubuntu()
UBUNTU_DERIV = False # True value means Ubuntu derivative. For Ubuntu it is False. For Mint it is True.
MINT = Config.is_Mint()
FEDORA = Config.is_Fedora()
ARCHLINUX = Config.is_ArchLinux()
DEBIAN = Config.is_Debian()
if UBUNTU:
    DISTRIBUTION = 'ubuntu'
    VERSION = Config.get_Ubuntu_version()
    BACKEND = APT
    installation_command_backend = debian_installation_command
elif MINT:
    DISTRIBUTION = 'ubuntu'
    UBUNTU_DERIV = True
    VERSION = Config.get_Mint_version() # VERSION is in ['5', '6', '7', '8', '9', '10']
    VERSION = ['hardy', 'intrepid', 'jaunty', 'karmic', 'lucid', 'maverick'][int(VERSION)-5]
    BACKEND = APT
    installation_command_backend = debian_installation_command
elif FEDORA:
    DISTRIBUTION = 'fedora'
    VERSION = Config.get_Fedora_version()
    BACKEND = RPM
    installation_command_backend = fedora_installation_command
elif ARCHLINUX:
    DISTRIBUTION = 'archlinux'
    VERSION = '' # ArchLinux has no version -_-b
    BACKEND = PACMAN
    installation_command_backend = archlinux_installation_command
elif DEBIAN:
    DISTRIBUTION = 'debian'
    VERSION = Config.get_Debian_version()
    BACKEND = APT
    installation_command_backend = debian_installation_command
else:
    # This Linux distribution is not supported. :(
    DISTRIBUTION = ''
    VERSION = ''
    BACKEND = None
    installation_command_backend = None

DESKTOP = 'gnome'
