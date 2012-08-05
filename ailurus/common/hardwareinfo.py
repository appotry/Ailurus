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

def print_traceback(): # do not display error message
    pass

def __read(path):
    with open(path) as f:
        ret = f.read().rstrip()
    return ret

def __bios():
    #The idea of this function is borrowd from cpu-g. Thanks!
    ret = []
    try:
        string = __read('/sys/devices/virtual/dmi/id/bios_vendor').strip()
        assert string
        ret.append( row(_('BIOS vendor:'), string) )
    except:
        print_traceback()

    try:
        string = __read('/sys/devices/virtual/dmi/id/bios_version').strip()
        assert string
        ret.append( row(_('BIOS version:'), string) )
    except:
        print_traceback()
        
    try:
        string = __read('/sys/devices/virtual/dmi/id/bios_date').strip()
        assert string
        ret.append( row(_('BIOS release date:'), string) )
    except:
        print_traceback()
    
    return ret

def __motherboard():
    ret = []
    try:
        string = __read('/sys/devices/virtual/dmi/id/board_name').strip()
        assert string
        ret.append( row(_('Motherboard name:'), string) )
    except IOError: pass
    except:
        print_traceback()
        
    try:
        string = __read('/sys/devices/virtual/dmi/id/board_vendor').strip()
        assert string
        ret.append( row(_('Motherboard vendor:'), string) )
    except IOError: pass
    except:
        print_traceback()
    
    return ret

def __cpu():
    ret = []
    
    try:
        core = 0
        with open('/proc/cpuinfo') as f:
            for line in f:
                v = line.split(':')
                v[0] = v[0].strip()
                if 'model name'==v[0]: core+=1
        multicore = core>1
        
        cache_info = {}
        for cpu_num in range(0, core):
            path = "/sys/devices/system/cpu/cpu%d/cache/" % cpu_num
            cache_info['cpu%s' % cpu_num] = cpus = { 'L1':'','L2':'','L3':'' }
            indexes = []
            try:   indexes = os.listdir(path)
            except: pass # no such folder
            for index in indexes:
                subpath = path + index + '/'
                with open(subpath + 'level') as f:
                    level = f.read().strip()
                with open(subpath + 'type') as f:
                    cache_type = f.read().strip()
                with open(subpath + 'size') as f:
                    size = f.read().strip()
                cpus['L%s' % level] += '%s %s cache. ' % (size, cache_type)   
                    
        core = 0
        with open('/proc/cpuinfo') as f:
            for line in f:
                v = line.split(':')
                v[0] = v[0].strip()
                if v[0] == 'model name':
                    core += 1
                    if multicore: name = _('CPU %s name:') % core
                    else: name = _('CPU name:')
                    value = v[1].strip().replace('  ',' ')
                    ret.append(row(name, value))
                elif v[0] == 'bogomips':
                    if multicore: 
                        mips_name = _('CPU %s Mips:') % core
                        mips_value = v[1].strip()
                        L1_cache_name = _('CPU %s level 1 cache size:') % core
                        L2_cache_name = _('CPU %s level 2 cache size:') % core
                    else: 
                        mips_name = _('CPU Mips:')
                        mips_value = v[1].strip()
                        L1_cache_name = _('Level 1 cache:')
                        L2_cache_name = _('Level 2 cache:')
                    L1_cache_value = cache_info['cpu%s' % (core-1)]['L1']
                    L2_cache_value = cache_info['cpu%s' % (core-1)]['L2']
                    if L1_cache_value: ret.append(row(L1_cache_name, L1_cache_value))
                    if L2_cache_value: ret.append(row(L2_cache_name, L2_cache_value))
                    ret.append(row(mips_name, mips_value, tooltip = _('It is a measure for the computation speed. "Mips" is short for Millions of Instructions Per Second.')))
            
            _64bit = _('No')
            f.seek(0, 0)
            for line in f:
                v = line.split(':')
                v[0] = v[0].strip()
                if v[0]=='flags':
                    if ' lm ' in v[1]:
                        _64bit = _('Yes!')
            ret.append( row(_('64 bit CPU?'), _64bit) )
    except:
        print_traceback()

    return ret

def __mem():
    try:
        with open('/proc/meminfo') as f:
            for line in f:
                v = line.split(':')
                if v[0]=='MemTotal':
                    string = v[1].strip() # format: YYY KB
                    value = float(string.split()[0])
                    if value > 1024*1024:
                        new_string = '%.1f GB' % (value/1024/1024)
                    elif value > 1024:
                        new_string = '%.1f MB' % (value/1024)
                    else:
                        new_string = string
                    return [row(_('Total memory:'), new_string)]
    except:
        print_traceback()
        return []

def __swap():
    try:
        total_size = 0
        with open('/proc/swaps') as f:
            contents = f.readlines()
        for line in contents[1:]: # the first line is a text header
            filename, type, size = line.split()[0:3]
            total_size += int(size)
        if total_size:
            return [row(_('Total swap:'), _('%s MBytes') % (total_size/1000))]
        else:
            return [] # no swap
    except:
        print_traceback()
        return []
        
def __pci():
    ret = []
    try:
        f = get_output('lspci')
        for line in f.split('\n'):
            v = line.split(' ', 1)[1]
            v = v.split(':', 1)
            if v[0]=='Display controller':
                ret.append( row(_('Display card:'), v[1].strip()) )
            elif v[0]=='Ethernet controller':
                ret.append( row(_('Ethernet card:'), v[1].strip()) )
            elif v[0]=='Multimedia audio controller':
                ret.append( row(_('Audio card:'), v[1].strip()) )
    except:
        print_traceback()
    return ret

def get():
    return [ __motherboard, __bios, __cpu,
             __mem, __swap, __pci, ] 
