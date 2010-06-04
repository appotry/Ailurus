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

AMule_0 = _("""aMule""")
AMule_1 = _("""An eMule-like client for eD2k and Kademlia networks""")
AWN_0 = _("""AWN (Avant Window Navigator): A dock-like bar""")
AWN_1 = "FIXME"
Agave_0 = _("""Agave""")
Agave_1 = _("""Colorscheme designer""")
Alacarte_0 = _("""Alacarte: Edit GNOME menu""")
Alacarte_1 = "FIXME"
Anjuta_0 = _("""Anjuta""")
Anjuta_1 = _("""GNOME IDE for C/C++""")
Audacity_0 = _("""Audacity: Music editor""")
Audacity_1 = "FIXME"
AutoApt_0 = _("""Auto-apt""")
AutoApt_1 = _(""""auto-apt run ./configure" can help you install the packages which are not installed.""")
AutoTools_0 = _("""Autoconf and Automake: Generate configure scripts and Makefiles""")
AutoTools_1 = "FIXME"
Avidemux_0 = _("""Avidemux""")
Avidemux_1 = _("""Video editor""")
Banshee_0 = _("""Banshee""")
Banshee_1 = _("""Media player and media manager""")
Bluefish_0 = _("""Bluefish: Edit HTML web-pages""")
Bluefish_1 = "FIXME"
Bluetooth_0 = _("""Bluetooth support""")
Bluetooth_1 = "FIXME"
Boost_0 = _("""Boost library""")
Boost_1 = "FIXME"
BosWars_0 = _("""Bos Wars""")
BosWars_1 = _("""Real time strategy game, just like Red Alarm""")
BreatheIconTheme_0 = _("""Breathe Icon Theme""")
BreatheIconTheme_1 = _("""Mix KDE's "Oxygen" icons with Ubuntu's "Human" theme.""")
Build_Essential_0 = _("""Build-essential""")
Build_Essential_1 = _("""By installing build-essential, you will get g++, make, gdb and libc.""")
CHMSee_Read_CHM_Documents_0 = _("""ChmSee: A CHM file viewer""")
CHMSee_Read_CHM_Documents_1 = "FIXME"
CheckInstall_0 = _("""CheckInstall""")
CheckInstall_1 = _("""Checkinstall help you build deb package.""")
Cheese_0 = _("""Cheese""")
Cheese_1 = _("""Take pictures and videos from your webcam, also provides some graphical effects""")
ChildsPlay_0 = _("""ChildsPlay: A suite of educational games for children""")
ChildsPlay_1 = "FIXME"
ClawsMail_0 = _("""Claws Mail""")
ClawsMail_1 = _("""Lightweight email client""")
CodeBlocks_0 = _("""Code::Blocks - C/C++ IDE""")
CodeBlocks_1 = "FIXME"
Comix_0 = _("""Comix""")
Comix_1 = _("""Customizable image viewer specifically designed to handle comic books""")
CompizSettingManager_0 = _("""Compiz settings manager""")
CompizSettingManager_1 = _("""Compiz Fusion is the unification of the Beryl project and the community around the Compiz Window Manager. Compiz settings manager is the configuration application for Compiz Fusion. It can configurate effects such as "Desktop cube" and "3D windows".""")
CompizSettingManagerSimple_0 = _("""Simple-ccsm: A simple Compiz settings manager""")
CompizSettingManagerSimple_1 = "FIXME"
Ctags_Cscope_0 = _("""Ctags and Cscope: Popular source code parsers""")
Ctags_Cscope_1 = "FIXME"
Deluge_0 = _("""Deluge""")
Deluge_1 = _("""Lightweight bittorrent client""")
Devhelp_0 = _("""Devhelp""")
Devhelp_1 = _("""Browse GNOME/GTK API documentation""")
Dia_0 = _("""Dia""")
Dia_1 = _("""Open source substitution for Visio""")
EasyTAG_0 = _("""EasyTAG""")
EasyTAG_1 = _("""Edit tags for MP3, FLAC, Ogg files""")
Emacs_0 = _("""Emacs: Advanced text editor""")
Emacs_1 = "FIXME"
Emesene_0 = _("""Emesene""")
Emesene_1 = _("""MSN Messenger client, with a simpler interface and a nicer look""")
Empathy_0 = _("""Empathy""")
Empathy_1 = _("""Messaging program which supports many protocols""")
Enhance_Decompression_Capability_0 = _("""Compression/decompression support for "*.7z" and "*.cab" files""")
Enhance_Decompression_Capability_1 = "FIXME"
Evince_Read_Chinese_PDF_0 = _("""Make Evince be able to reveal Chinese, Japanese, Korean pdf""")
Evince_Read_Chinese_PDF_1 = "FIXME"
Evolution_0 = _("""Evolution""")
Evolution_1 = _("""Email client, calendar, contact manager and address manager""")
Extcalc_0 = _("""Extcalc: A multifunctional graphic calculator""")
Extcalc_1 = "FIXME"
Fcitx_0 = _("""Fcitx""")
Fcitx_1 = _("""This is a popular Chinese input method.
It is from http://fcitx.googlecode.com/""")
FileZilla_0 = _("""FileZilla""")
FileZilla_1 = _("""FTP client""")
FireWall_0 = _("""Firestarter: Configure Linux firewall""")
FireWall_1 = _("""Linux system comes up with a firewall "iptables". Firestarter is the graphical frontend of "iptables".""")
FreeDOOM_0 = _("""FreeDOOM: Open source clone of DOOM""")
FreeDOOM_1 = "FIXME"
FreeGLut3_0 = _("""OpenGL library""")
FreeGLut3_1 = _("""This is a library for writing OpenGL programs.""")
FrozenBubble_0 = _("""Frozen Bubble""")
FrozenBubble_1 = _("""Clone of the popular "Puzzle Bobble" game""")
GCompris_0 = _("""GCompris: Educational games for children aged 2 to 10""")
GCompris_1 = "FIXME"
GCstar_0 = _("""GCstar""")
GCstar_1 = _("""Manage your collections such as movies, books, music""")
GIMP_0 = _("""GIMP""")
GIMP_1 = _("""Open source substitution for Photoshop""")
GMP_0 = _("""GNU multiprecision arithmetic library""")
GMP_1 = "FIXME"
GNOMEColors_0 = _("""GNOME Colors""")
GNOMEColors_1 = _("""A set of icons with 7 color variations""")
GNOMEDo_0 = _("""GNOME Do""")
GNOMEDo_1 = _("""Desktop launcher, which helps you quickly perform actions""")
GNOMEShell_0 = _("""GNOME shell""")
GNOMEShell_1 = _("""Experience GNOME 3 desktop""")
GNOME_mplayer_0 = _("""GNOME MPlayer""")
GNOME_mplayer_1 = _("""GTK frontend for MPlayer""")
Geany_0 = _("""Geany""")
Geany_1 = _("""Lightweight text editor""")
Ghex_0 = _("""Ghex""")
Ghex_1 = _("""Hex editor""")
Giver_0 = _("""Giver""")
Giver_1 = _("""Automatically discover other people running Giver on the network, then send files to other people""")
Glest_0 = _("""Glest""")
Glest_1 = _("""Real time strategy game, just like Warcraft""")
Globulation2_0 = _("""Globulation 2""")
Globulation2_1 = _("""Real time strategy game which focuses on strategy rather than on micro-management""")
Gnash_0 = _("""Flash plugin for web browser""")
Gnash_1 = "FIXME"
Gnote_0 = _("""Gnote""")
Gnote_1 = _("""Mono-free alternative to Tomboy Notes""")
GoogleGadgetsGTK_0 = _("""Google gadgets (GTK version)""")
GoogleGadgetsGTK_1 = "FIXME"
GoogleGadgetsQT_0 = _("""Google gadgets (QT version)""")
GoogleGadgetsQT_1 = "FIXME"
Gwibber_0 = _("""Gwibber""")
Gwibber_1 = _("""Microblogging client which supports Twitter and Facebook""")
HardwareLister_0 = _("""lshw: List hardware information""")
HardwareLister_1 = _("""A small application which displays detailed hardware information""")
Hedgewars_0 = _("""Hedgewars""")
Hedgewars_1 = _("""Hedgehogs fight enemies with fantastic weapons""")
ImageMagick_0 = _("""ImageMagick: Edit images""")
ImageMagick_1 = _("""You can start it by /usr/bin/display""")
Inkscape_0 = _("""Inkscape: Design vector image. Open source substitution of CorelDraw.""")
Inkscape_1 = "FIXME"
K3B_0 = _("""K3B: Create DVD/VCD""")
K3B_1 = "FIXME"
Kadu_0 = _("""Kadu""")
Kadu_1 = _("""Kadu is an instant messenger, which is very popular in Poland.
Command : yum install kadu""")
Keepassx_0 = _("""Keepassx""")
Keepassx_1 = _("""Password manager which saves many different information e.g. user names and passwords in one single database.""")
Kflickr_0 = _("""kflickr""")
Kflickr_1 = _("""Upload photos to Flickr""")
Kupfer_0 = _("""Kupfer""")
Kupfer_1 = _("""Lightweight desktop launcher""")
Leafpad_0 = _("""Leafpad""")
Leafpad_1 = _("""Simple text editor""")
Liferea_0 = _("""Liferea: a RSS feed reader""")
Liferea_1 = _("""This is a simple and easy used RSS feed reader.""")
LinuxDCPP_0 = _("""Linuxdcpp""")
LinuxDCPP_1 = _("""Connect to a central hub then share files and chat with other people.""")
MACChanger_0 = _("""MACChanger: change MAC address""")
MACChanger_1 = _("""MACChanger is a utility for viewing/manipulating the MAC address of network interfaces.""")
Midori_0 = _("""Midori""")
Midori_1 = _("""Lightweight web browser""")
MiniCom_Ckermit_0 = _("""Minicom and Kermit: Communication software for embedded MCU boards""")
MiniCom_Ckermit_1 = "FIXME"
Minitube_0 = _("""Minitube""")
Minitube_1 = _("""Simple Youtube client""")
Miro_0 = _("""Miro""")
Miro_1 = _("""Video player""")
Moonlight_0 = _("""Moonlight: an open source implementation of Microsoft® Silverlight""")
Moonlight_1 = _("""Moonlight provides Windows® media codecs. By this application, you can enjoy Windows® video/audio in webpages.""")
Multimedia_Codecs_0 = _("""Multi-media codec""")
Multimedia_Codecs_1 = "FIXME"
Nautilus_Actions_0 = _(""""Actions configuration" entry""")
Nautilus_Actions_1 = _("""It allows the configuration of programs to be launched on files selected.
<span color="red">This entry is not in context menu. It is in "System"->"Preferences" menu.</span>""")
Nautilus_Audio_Convert_0 = _(""""Convert audio files" entry""")
Nautilus_Audio_Convert_1 = _("""Converts between WAV, OGG, MP3, MPC, FLAC, APE and AAC files.
These packages will also be installed: 
<i>lame libid3-3.8.3-dev flac faac faad mppenc</i>""")
Nautilus_Filename_Repairer_0 = _(""""Repair filename" entry""")
Nautilus_Filename_Repairer_1 = _("""When any file with wrong encoding filename is right clicked,
 show a "Repair filename" menu item.""")
Nautilus_Gksu_0 = _(""""Open as administrator" entry""")
Nautilus_Gksu_1 = _("""Launch selected files with administration privileges using the context menu.
Open selected folder with administration privileges.""")
Nautilus_Image_Converter_0 = _(""""Resize/Rotate images" entries""")
Nautilus_Image_Converter_1 = _("""Resize or rotate selected images.""")
Nautilus_Open_Terminal_0 = _(""""Open in terminal" entry""")
Nautilus_Open_Terminal_1 = _("""Open a terminal in current folder.""")
Nautilus_Script_Collection_Svn_0 = _(""""Subversion commands" entries""")
Nautilus_Script_Collection_Svn_1 = _(""""Subversion commands" entries""")
Nautilus_Search_Tool_0 = _(""""Search files" entries""")
Nautilus_Search_Tool_1 = "FIXME"
Nautilus_Share_0 = _(""""Share folders" entry""")
Nautilus_Share_1 = _("""Share folders by Samba.""")
Nautilus_Wallpaper_0 = _(""""Set as wallpaper" entry""")
Nautilus_Wallpaper_1 = _(""""Set as wallpaper" entry""")
Ncurses_and_qt3mt_0 = _("""Ncurses5 and QT3""")
Ncurses_and_qt3mt_1 = _("""libncurses5 is a library controlling writing to the console screen.
libqt3-mt is Trolltech Qt library, version 3.""")
Netbeans_0 = _("""NetBeans""")
Netbeans_1 = _("""It is an open source IDE which supports several languages (C, C++, Java, Ruby, etc.) and frameworks (J2SE, J2ME, etc.). Official site: http://netbeans.org/downloads/ . This application depends on Java.""")
Nexuiz_0 = _("""Nexuiz""")
Nexuiz_1 = _("""3D first-person shooter game""")
Octave_0 = _("""Octave: A Matlab® compatible numerical computation appliation""")
Octave_1 = "FIXME"
OpenJDK_0 = _("""OpenJDK 6""")
OpenJDK_1 = "FIXME"
Openshot_0 = _("""Openshot""")
Openshot_1 = _("""Non-linear video editor""")
POSIX_ManPages_0 = _("""POSIX library manual pages""")
POSIX_ManPages_1 = _("""Install manual pages about Linux system calls, library calls, and POSIX libraries.""")
Parcellite_0 = _("""Parcellite: clipboard manager""")
Parcellite_1 = _("""This is a powerful clipboard manager. It can preserve 25 strings concurrently.""")
PiTiVi_0 = _("""PiTiVi: Movie editor""")
PiTiVi_1 = "FIXME"
Pidgin_0 = _("""Pidgin""")
Pidgin_1 = "FIXME"
PowerTop_0 = _("""PowerTop""")
PowerTop_1 = _("""Powertop helps you save power for your laptop.""")
QCad_0 = _("""QCad: A CAD software which supports DXF-format""")
QCad_1 = "FIXME"
QT_Creator_0 = _("""Qt Creator""")
QT_Creator_1 = _("""This is an IDE for Qt.""")
Qnapi_0 = _("""Qnapi""")
Qnapi_1 = _("""QNapi is unofficial free clone of NAPI-PROJEKT program. Its purpose is to find and download subtitles for given video file. Currently only Polish subtitles are available.""")
QtiPlot_0 = _("""QtiPlot: The equivalence of "Origin" plotting application in Linux""")
QtiPlot_1 = _("""It is the indispensable plotting application for writing Physics experiments reports.""")
QutIM_0 = _("""qutIM""")
QutIM_1 = _("""Lightweight messaging program""")
R_Language_Basic_0 = _("""R language (basic development environment)""")
R_Language_Basic_1 = _("""A powerful statistical computation language and a graphics system.
If you want to use the latest version of R language, please read http://cran.r-project.org/""")
SDL_0 = _("""SDL library""")
SDL_1 = _("""This is a library for writing SDL programs.
SDL is a cross-platform multimedia library designed to provide low level access to audio keyboard, mouse, joystick, 3D hardware via OpenGL, and 2D video framebuffer.""")
SMPlayer_0 = _("""SMPlayer""")
SMPlayer_1 = _("""Qt frontend for MPlayer""")
ScienceBiology_0 = _("""Med-bio: A lot of micro-biology software""")
ScienceBiology_1 = _("""A lot of software for molecular biology, structural biology and bioinformatics.""")
Screenlets_0 = _("""Screenlets: Add eye candy gadgets on desktop""")
Screenlets_1 = _("""Screenlets is able to add eye candy gadgets on desktop, such as sticky notes, clocks, weather forecasts, calendars and so on, in order to decorate the desktop.""")
Scribus_0 = _("""Scribus""")
Scribus_1 = _("""Professional typesetting software""")
ShikiColors_0 = _("""Shiki Colors""")
ShikiColors_1 = _("""Hybrid theme which is designed to be fast and stable""")
Shutter_0 = _("""Shutter""")
Shutter_1 = _("""Make screenshots""")
Sonata_0 = _("""Sonata""")
Sonata_1 = _("""Lightweight music player""")
Stardict_0 = _("""Stardict""")
Stardict_1 = "FIXME"
StartupManager_0 = _("""Startup Manager: Change GRUB settings and themes""")
StartupManager_1 = _("""Startup manager helps you change GRUB settings and themes.""")
Svn_Git_bzr_0 = _("""Subversion, Git and Bzr: Popular version control systems""")
Svn_Git_bzr_1 = "FIXME"
TeXLive_0 = _("""TeXLive""")
TeXLive_1 = _("""Create a file "example.tex", then compile it by "xelatex example.tex". http://ailurus.cn/?p=329""")
TheManaWorld_0 = _("""The Mana World""")
TheManaWorld_1 = _("""2D MMORPG""")
Thunderbird_0 = _("""Thunderbird""")
Thunderbird_1 = _("""Email client and RSS reader""")
Transmission_0 = _("""Transmission""")
Transmission_1 = _("""Lightweight bittorrent client""")
TuxPaint_0 = _("""Tux Paint: A drawing program for young children three years and up""")
TuxPaint_1 = "FIXME"
Typespeed_0 = _("""Typespeed""")
Typespeed_1 = _("""Typespeed is a typing practise. It only runs in terminal.""")
Ubuntu_Studio_Theme_0 = _("""Ubuntu Studio Theme""")
Ubuntu_Studio_Theme_1 = "FIXME"
Umbrello_0 = _("""Umbrello: UML modelling""")
Umbrello_1 = _("""Umbrello help you do UML modelling.""")
VIM_0 = _("""VIM""")
VIM_1 = "FIXME"
VLC_0 = _("""VLC""")
VLC_1 = _("""Media player and media format converter""")
VirtualBox_0 = _("""VirtualBox open source edition""")
VirtualBox_1 = _("""It is the only professional virtual machine which is freely available under the terms of GPL. Official site: http://www.virtualbox.org/wiki/Downloads""")
Vuze_Karmic_0 = _("""Vuze: Download via bittorrent; Search videos""")
Vuze_Karmic_1 = "FIXME"
WINE_0 = _("""WINE""")
WINE_1 = _("""This is an indispensable application for running Windows applications on Linux.""")
Warsow_0 = _("""Warsow""")
Warsow_1 = _("""3D first-person shooter game, just like DOOM""")
Warzone2100_0 = _("""Warzone 2100""")
Warzone2100_1 = _("""Real time strategy game""")
Wesnoth_0 = _("""Battle for Wesnoth""")
Wesnoth_1 = _("""A popular turn-based game""")
Workrave_0 = _("""Workrave""")
Workrave_1 = _("""The program frequently alerts you to leave computers, take micro-pauses, rest breaks and restricts you to your daily limit of using computers.""")
WorldofPadman_0 = _("""World of Padman: Funny shooter game""")
WorldofPadman_1 = _("""Ailurus will install the game, and apply the latest patch.
Download from ftp://ftp.snt.utwente.nl/pub/games/worldofpadman/linux/""")
Wormux_0 = _("""Wormux""")
Wormux_1 = _("""Funny fight game on 2D maps""")
Zhcon_0 = _("""Zhcon""")
Zhcon_1 = _("""Zhcon helps you display Chinese characters in TTY terminal.
You can launch it by "zhcon --utf8".""")
Zim_0 = _("""Zim""")
Zim_1 = _("""Notebook software which helps you create a wiki to your desktop""")
