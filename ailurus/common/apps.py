#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Ailurus - make Linux easier to use
#
# Copyright (C) 2007-2010, Trusted Digital Technology Laboratory, Shanghai Jiao Tong University, China.
# Copyright (C) 2009-2010, Ailurus Developers Team
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
from libapp import *

class Generic_Genome_Browser(I):
    __doc__ = _('Generic Genome Browser')
    detail = _('Generic Genome Browser is a combination of database and interactive web page '
               'for manipulating and displaying annotations on genomes.\n'
               '<span color="red">Due to the limitation of the authors\' programming ability, '
               '"Generic Genome Browser" cannot be detected or removed by Ailurus.</span>')
    license = AL
    category='biology'
    def install(self):
        if FEDORA:
            for package in ['perl-libwww-perl', 'perl-CPAN']:
                if not RPM.installed(package): RPM.install(package)
        
        f = R('http://gmod.svn.sourceforge.net/viewvc/gmod/Generic-Genome-Browser/trunk/bin/gbrowse_netinstall.pl').download()
        run_as_root_in_terminal('perl ' + f)
    def installed(self):
        return False
    def remove(self):
        raise NotImplementedError

class Bioclipse(_path_lists):
    __doc__ = _('Bioclipse: an awesome Chemical and Biological Informatics application')
    download_url = 'http://sourceforge.net/projects/bioclipse/files/bioclipse2/'
    category = 'biology'
    license = ('Eclipse Public License (EPL) + exception, '
               'see http://www.bioclipse.net/license-0')
    def __init__(self):
        self.shortcut = '/usr/share/applications/bioclipse.desktop'
        self.path = '/opt/bioclipse'
        self.paths = [ self.shortcut, self.path ]
    def install(self):
        if is32():
            f = R(['http://sourceforge.net/projects/bioclipse/files/bioclipse2/bioclipse2.0/bioclipse2.0.linux.gtk.x86.zip/download'],
                  filename = 'bioclipse2.0.linux.gtk.x86.zip').download()
        else:
            f = R(['http://sourceforge.net/projects/bioclipse/files/bioclipse2/bioclipse2.0/bioclipse2.0.linux.gtk.x86_64.zip/download'],
                  filename = 'bioclipse2.0.linux.gtk.x86_64.zip').download()
        with Chdir('/tmp') as o:
            run('unzip -qo %s' %f)
            import os
            if not os.path.exists('/opt'): run_as_root('mkdir /opt')
            run_as_root('rm /opt/bioclipse -rf')
            if is32():
                run_as_root('mv bioclipse2.0.linux.gtk.x86/bioclipse /opt/')
            else:
                run_as_root('mv bioclipse2.0.linux.gtk.x86_64/bioclipse /opt/')
            run_as_root('chown $USER:$USER /opt/bioclipse -R')
            
            create_file(self.shortcut,'''[Desktop Entry]
Name=Bioclipse
Exec=/opt/bioclipse/bioclipse
Encoding=UTF-8
StartupNotify=true
Terminal=false
Type=Application
Categories=Development
Icon=/opt/bioclipse/icon.xpm 
''')
            
            file_append('/opt/bioclipse/bioclipse.ini', '-Dorg.eclipse.swt.browser.XULRunnerPath=/usr/lib/xulrunner/')

class Electric(_path_lists):
    __doc__ = _('Electric: A software for IC design which supports VHDL and Verilog')
    category = 'electronics'
    license = GPL
    download_url = 'http://www.staticfreesoft.com/'
    def __init__(self):
        self.shortcut = '/usr/share/applications/electric.desktop'
        self.file = '/opt/electricBinary.jar'
        self.paths = [self.shortcut, self.file]
    def install(self):
        f = R(
['http://ftp.gnu.org/pub/gnu/electric/electricBinary-8.09.jar'],
11102701, 'c50557bc54b74948e707dc4606009bd93274ec71').download()

        run_as_root('mkdir /opt', ignore_error=True)
        run_as_root('cp %s %s'%(f, self.file) )
        create_file(self.shortcut, '''[Desktop Entry]
Name=Electric
Exec=java -jar %s -Xms512M -Xmx1024M -Dsun.java2d.opengl=true
Encoding=UTF-8
StartupNotify=true
Terminal=false
Type=Application
Categories=Science;Engineering;'''%self.file)

class SweetHome3D(_path_lists):
    __doc__ = _('SweetHome3D: open source interior design application')
    detail = _('Official site:') + ' http://www.sweethome3d.com/'
    category = 'design'
    shortcut = '/usr/share/applications/SweetHome3D.desktop'
    path = '/opt/SweetHome3D-2.3'
    paths = [shortcut, path]
    def install(self):
        if is32(): url = 'http://ncu.dl.sourceforge.net/project/sweethome3d/SweetHome3D/SweetHome3D-2.3/SweetHome3D-2.3-linux-x86.tgz'
        else:       url = 'http://ncu.dl.sourceforge.net/project/sweethome3d/SweetHome3D/SweetHome3D-2.3/SweetHome3D-2.3-linux-x64.tgz'
        f = R([url]).download()
        run_as_root('mkdir /opt', ignore_error=True)
        with Chdir('/opt') as c:
            run_as_root('tar xf ' + f)
        create_file(self.shortcut, '[Desktop Entry]\n'
                                   'Name=SweetHome3D\n'
                                   'Exec=' + self.path + '/SweetHome3D\n'
                                   'Encoding=UTF-8\n'
                                   'StartupNotify=true\n'
                                   'Terminal=false\n'
                                   'Type=Application\n'
                                   'Categories=Graphics;\n')

# Do not install it via Launchpad, because the packages there is 1.6. It is old, since 1.8 has been released. 
class Songbird(I):
    __doc__ = _('Songbird: Open source substitution of iTunes')
    detail = (_('Music player which integrates with online content via plugins. '
               'Site contains project news, download, add-ons directory, help, and how to contribute.') + '\n' + 
              _('Launch it by this command:') + ' LD_BIND_NOW=1 ./songbird')
    download_url = 'http://developer.songbirdnest.com/builds/trunk/latest/' 
    category = 'player'
    license = GPL
    def install(self):
        open_web_page('http://developer.songbirdnest.com/builds/trunk/latest/')
    def installed(self):
        return False
    def remove(self):
        pass

#class OpenJUMP(_path_lists):
#    __doc__ = _('OpenJUMP: A geographic information system')
#    detail = ( 
#              _('Official site: http://openjump.org/ .') +
#              _(' This application depends on Java.') )
#    license = GPL
#    category = 'geography'
#    def __init__(self):
#        self.shortcut = '/usr/share/applications/openjump.desktop'
#        self.dir = '/opt/openjump-1.3'
#        self.paths = [self.shortcut, self.dir]
#    def install(self):
#        f = R(
#['http://ncu.dl.sourceforge.net/project/jump-pilot/OpenJUMP/1.3/openjump-v1.3.zip'],
#12431980, '4df9363f0e41c797f99265107d57184b8c394ae8').download()
#
#        with Chdir('/tmp') as o:
#            run('unzip -oq %s'%f)
#            import os
#            if not os.path.exists('/opt'):
#                run_as_root('mkdir /opt')
#            if not os.path.exists(self.dir):
#                run_as_root('mv openjump-1.3 /opt/')
#            create_file(self.shortcut, '''[Desktop Entry]
#Name=OpenJUMP
#Exec=bash /opt/openjump-1.3/bin/openjump.sh
#Encoding=UTF-8
#StartupNotify=true
#Terminal=false
#Type=Application
#Categories=Science;Engineering; ''')

class TsingHuaTeXTemplate(_download_one_file):
    __doc__ = _('LaTeX Thesis Templates by Tsing Hua University, China')
    import os
    detail = _('These templates include undergraduate dissertation template, master thesis template and PhD thesis template. '
       'They are developed by Tsing Hua University, China. Official website is http://thuthesis.sourceforge.net/\n'
       'After installation, a file "thuthesis.tgz" is placed in the folder "%s".')%os.environ['HOME']
    category = 'latex'
    Chinese = True
    license = 'GPL'
    def __init__(self):
        self.R = R(
['http://thuthesis.googlecode.com/files/thuthesis-4.5.1.tgz'],
9101319, '7f617b66479cafe7c01b7b104e0392a947a064ef')
        import os
        self.file = os.path.expandvars('$HOME/thuthesis.tgz')

class FFAdblock(_ff_extension):
    __doc__ = _('Adblock+: Block 99% advertisement')
    license = MPL
    detail = _('It is able to block 99% ads and banners.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/1865'
    name = u'Adblock Plus'
    R = R(latest(1865), filename='adblock_plus.xpi')

class FFAutoProxy(_ff_extension):
    __doc__ = _('AutoProxy: Proxy management via a third party list')
    Chinese = True
    license = MPL
    detail = ''
    download_url = 'https://addons.mozilla.org/zh-CN/firefox/addon/11009'
    name = u'AutoProxy'
    R = R(latest(11009), filename='autoproxy.xpi')

class FFChromifox(_ff_extension): 
    __doc__ = _('Chromifox: Chrome theme')
    license = TRI_LICENSE(MPL, GPL, LGPL)
    detail = _('A coat of Chrome for Firefox')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/8782'
    name = u'Chromifox Basic'
    R = R(latest(8782), filename='chromifox_basic.jar')

class FFCleanHide(_ff_extension):
    __doc__ = _('CleanHide: Delete hidden text in web page')
    license = GPL
    detail = _('If you find that some web page use hidden text and you cannot copy text easily, try this!')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/3648'
    name = u'CleanHide'
    R = R(latest(3648), filename='cleanhide.xpi')

class FFDownloadStatusBar(_ff_extension): 
    __doc__ = _('DownloadStatusBar: Keep track of downloads in a tiny statusbar.')
    license = MPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/26'
    name = u'Download Statusbar'
    R = R(latest(26), filename='download_statusbar.xpi')

class FFDownThemAll(_ff_extension):
    __doc__ = _('DownThemAll: A reliable multithread downloader')
    license = GPL
    detail = _('It is able to download all images on web-pages.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/201'
    name = u'DownThemAll!'
    R = R(latest(201), filename='downthemall.xpi')

class FFEasyDragToGo(_ff_extension):
    __doc__ = _('EasyDragToGo: Open new tabs by dragging text, links and pictures')
    license = MPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/6639'
    name = u'Easy DragToGo'
    R = R(latest(6639), filename='easy_dragtogo.xpi')

class FFFireBug(_ff_extension):
    __doc__ = _('FireBug: Real-time edit and debug CSS/HTML/JavaScript in webpage')
    category = 'firefox_extension'
    license = BSD
    detail = _('This is a powerful web development tool.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/1843'
    name = u'Firebug'
    R = R(latest(1843), filename='firebug.xpi')

class FFFireGesture(_ff_extension):
    __doc__ = _('FireGesture: Execute commands and user scripts by mouse gestures')
    license = MPL
    detail = _('It supports five kinds of mouse gestures.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/6366'
    name = u'FireGestures'
    R = R(latest(6366), filename='firegestures.xpi')

class FFFlashgot(_ff_extension):
    __doc__ = _('Flashgot: A lightweight and reliable download managers')
    license = GPL
    detail = _("It is able to download all the links, movies and audio clips of a page with a single click.")
    download_url = 'https://addons.mozilla.org/zh-CN/firefox/addon/220'
    name = u'Flashgot'
    R = R(latest(220), filename='flashgot.xpi')

class FFFoxyProxy(_ff_extension):
    __doc__ = _('FoxyProxy: One-click switching proxy')
    license = GPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/2464'
    name = u'FoxyProxy Standard'
    R = R(latest(2464), filename='foxyproxy_standard.xpi')

class FFGreaseMonkey(_ff_extension):
    __doc__ = _('GreaseMonkey: Make change to web pages')
    license = MIT
    detail = _('This is an extension that allow you to install scripts to make changes to web page, such as adding an HTML signature and bypassing image verification.'
              'You can download hundreds of scripts from http://userscripts.org, or '
              'check out http://wiki.greasespot.net/ to get started to write your own scripts. '
              'The book "Dive into Greasemonkey" is worth reading. It can be downloaded freely from http://diveintogreasemonkey.org/ .' )
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/748'
    name = u'Greasemonkey'
    R = R(latest(748), filename='greasemonke.xpi')

class FFLiveHTTPHeaders(_ff_extension):
    __doc__ = _('Live HTTP Headers: View HTTP headers in real-time')
    category = 'firefox_extension'
    license = GPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/3829'
    name = u'Live HTTP Headers'
    R = R(latest(3829), filename='live_http_headers.xpi')

class FFNoscript(_ff_extension):
    __doc__ = _('NoScript: Allow active content to run only from sites you trust')
    license = GPL
    detail = _('Allow active content to run only from sites you trust, and protect yourself against XSS and Clickjacking attacks.' )
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/722'
    name = u'NoScript'
    R = R(latest(722), filename='noscript.xpi')

class FFRadioGet(_ff_extension):
    __doc__  = _('SHA-DA network radio: Listen to and watch radio and TV programs in China')
    Chinese = True
    license = GPL
    detail = ''
    download_url = 'http://ipget.cn/RadioGet/'
    name = u'RadioGet'
    R = R(['http://ipget.cn/RadioGet/RadioGet-0.9.xpi', 'http://ailurus.googlecode.com/files/RadioGet-0.9.xpi'],
    15870, '132b45fd31dff76676d6d66bbe2b0f556f2f34fd') # We add a second url because ipget.cn is in expiration date now :(

class FFSeoQuake(_ff_extension):
    __doc__ = _('SeoQuake: Help you view search engine parameters of your web site')
    category = 'firefox_extension'
    license = MPL
    detail = _('It helps you promote your web sites.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/3036'
    name = u'SeoQuake'
    R = R(latest(3036), filename='seoquake.xpi')

class FFStylish(_ff_extension):
    __doc__ = _('Stylish: Install themes and skins for websites.')
    license = GPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/2108'
    name = u'Stylish'
    R = R(latest(2108), filename='stylish.xpi')

class FFTamperData(_ff_extension):
    __doc__ = _('Tamper Data: View and modify HTTP/HTTPS headers and post request parameters.')
    category = 'firefox_extension'
    license = GPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/966'
    name = u'Tamper Data'
    R = R(latest(966), filename='tamper_data.xpi')

class FFUserAgentSwitcher(_ff_extension):
    __doc__ = _('User Agent Switcher: Camousflag Firefox as other kinds of browsers.')
    license = GPL
    detail = _('It tells the remote websites that you are an IE user.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/59'
    name = u'User Agent Switcher'
    R = R(latest(59), filename='user_agent_switcher.xpi')

class FFViewSourceChart(_ff_extension):
    __doc__ = _('View Source Chart: Show pretty color-coded HTML source code')
    category = 'firefox_extension'
    license = GPL
    detail = _("This extension helps you quickly scan and recognize a document's tags.")
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/655'
    name = u'View Source Chart'
    R = R(latest(655), filename='view_source_chart.xpi')

class FFFirefoxSync(_ff_extension):
    __doc__ = _('Firefox Sync: synchronize bookmarks, browsing history and tabs wherever you go.')
    license = MPL
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/10868'
    name = u'Weave'
    R = R(latest(10868), filename='firefox_sync.xpi')

class FFWebDeveloper(_ff_extension):
    __doc__ = _('Web Developer: Web page analysis tools')
    category = 'firefox_extension'
    license = LGPL
    detail = _('Many developers installed it.')
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/60'
    name = u'Web Developer'
    R = R(latest(60), filename='web_developer.xpi')

class FFYetAnotherSmoothScrolling(_ff_extension):
    __doc__ = _('Yet Another Smooth Scrolling: Customize scrolling behavior')
    license = BSD
    detail = ''
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/5846'
    name = u'Yet Another Smooth Scrolling'
    R = R(latest(5846), filename='yet_another_smooth_scrolling.xpi')

class FFYSlow(_ff_extension):
    __doc__ = _("YSlow: web page performance tuning")
    category = 'firefox_extension'
    license = MPL
    detail = _("It helps you improve web page performance. It tells you why web page is slow.")
    download_url = 'https://addons.mozilla.org/en-US/firefox/addon/5369'
    name = u'YSlow'
    R = R(latest(5369), filename='yslow.xpi')
