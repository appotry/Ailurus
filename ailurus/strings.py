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

AMule_0 = 'aMule'
AMule_1 = _("""Free peer-to-peer file sharing application that works with EDonkey network and Kad network, offering similar features to eMule""")
AWN_0 = _("""Avant Window Navigator""")
AWN_1 = _("A dock sits at the bottom of the screen which lists open windows. It also supports third party applets.")
Agave_0 = 'Agave'
Agave_1 = _("""A designer which can generate a variety of colorschemes from a single starting color""")
Alacarte_0 = 'Alacarte'
Alacarte_1 = _("Edit GNOME menu easily")
Anjuta_0 = _("""Anjuta""")
Anjuta_1 = _("""GNOME IDE for C/C++ with a number of features such as project management, application wizard, interactive debugger, source editor, version control, GUI designer and profiler.""")
Audacity_0 = _("""Audacity""")
Audacity_1 = _('Record and edit sounds')
AutoApt_0 = _("""Auto-apt""")
AutoApt_1 = _(""""auto-apt run ./configure" helps you automatically install required packages.""")
AutoTools_0 = _("""Autoconf and Automake""")
AutoTools_1 = _("Automatically generate configure scripts and GNU Standard makefiles")
Avidemux_0 = _("""Avidemux""")
Avidemux_1 = _("""Video editor which can do simple cutting, filtering and encoding tasks. It supports scripts and automated job queue.""")
Banshee_0 = _("""Banshee""")
Banshee_1 = _("""Media player and media manager written in Mono and Gtk#. It is the default media player for several Linux distribution.""")
Bluefish_0 = _("""Bluefish""")
Bluefish_1 = _("An editor targeted towards webdesigners. It supports many programming and markup languages, and it focuses on editing dynamic websites.")
Bluez_0 = _("""BlueZ""")
Bluez_1 = _("Official Linux bluetooth support")
Boost_0 = _("""Boost C++ libraries""")
Boost_1 = _("Peer-reviewed portable C++ libraries, which will be in the new C++ 0x standard.")
BosWars_0 = _("""Bos Wars""")
BosWars_1 = _("""Real time strategy game, just like Red Alarm""")
BreatheIconTheme_0 = _("""Breathe Icon Theme""")
BreatheIconTheme_1 = _("""Mix KDE's "Oxygen" icons with Ubuntu's "Human" theme.""")
Build_Essential_0 = _("""g++, make, gdb and libc""")
Build_Essential_1 = _("""Popular development tools""")
CHMSee_Read_CHM_Documents_0 = _("""ChmSee""")
CHMSee_Read_CHM_Documents_1 = _("View .chm files")
CheckInstall_0 = _("""CheckInstall""")
CheckInstall_1 = _("""Help you build .deb packages""")
Cheese_0 = _("""Cheese""")
Cheese_1 = _("""It helps you take pictures and videos from web camera. It also provides some graphical effects in order to please your play instinct.""")
ChildsPlay_0 = _("""ChildsPlay""")
ChildsPlay_1 = _("Educational games for young children")
ClawsMail_0 = _("""Claws Mail""")
ClawsMail_1 = _("""Lightweight email client""")
CodeBlocks_0 = _("""Code::Blocks""")
CodeBlocks_1 = _("C/C++ IDE with many features")
Comix_0 = _("""Comix""")
Comix_1 = _("""Image viewer specifically designed to handle comic books""")
CompizSettingManager_0 = _("""Compiz settings manager""")
CompizSettingManager_1 = _("""Full-function software which can configure all options of Compiz window manager""")
CompizSettingManagerSimple_0 = _("""Simple-ccsm""")
CompizSettingManagerSimple_1 = _("Simple configure software for Compiz window manager")
Ctags_Cscope_0 = _("""Ctags and Cscope""")
Ctags_Cscope_1 = _("Popular source code parsers")
Deluge_0 = _("""Deluge""")
Deluge_1 = _("""Lightweight bittorrent client""")
Devhelp_0 = _("""Devhelp""")
Devhelp_1 = _("""Browse GNOME/GTK API documentation""")
Dia_0 = _("""Dia""")
Dia_1 = _("""Open source substitution for Visio""")
EasyTAG_0 = _("""EasyTAG""")
EasyTAG_1 = _("""Edit tags for MP3, FLAC, Ogg files""")
Emacs_0 = _("""Emacs""")
Emacs_1 = _("Advanced text editor")
Emesene_0 = _("""Emesene""")
Emesene_1 = _("""MSN Messenger client with a simpler interface and a nicer look""")
Empathy_0 = _("""Empathy""")
Empathy_1 = _("""Messaging program which supports many protocols""")
Enhance_Decompression_Capability_0 = _("""p7zip and cabextract""")
Enhance_Decompression_Capability_1 = _("compressor/decompressor for .7z and .cab files")
Evince_Read_Chinese_PDF_0 = _("""Encoding data for the poppler PDF library""")
Evince_Read_Chinese_PDF_1 = _('Make Evince be able to reveal Japanese, Korean, Chinese pdf')
Evolution_0 = _("""Evolution""")
Evolution_1 = _("""Email client, calendar, contact manager and address manager""")
Extcalc_0 = _("""Extcalc""")
Extcalc_1 = _('Multifunctional graphic calculator')
Fcitx_0 = _("""Fcitx""")
Fcitx_1 = _("""Popular Chinese input method""")
FileZilla_0 = _("""FileZilla""")
FileZilla_1 = _("""Popular FTP client""")
FireWall_0 = _("""Firestarter""")
FireWall_1 = _("""Configure software for "iptables" firewall. "iptables" is the filewall which Linux system comes up with.""")
FreeDOOM_0 = _("""FreeDOOM""")
FreeDOOM_1 = _("Open source clone of DOOM")
FreeGLut3_0 = _("""OpenGL library""")
FreeGLut3_1 = _("""This is a library for writing OpenGL programs.""")
FrozenBubble_0 = _("""Frozen Bubble""")
FrozenBubble_1 = _("""Open source clone of the popular "Puzzle Bobble" game""")
GCompris_0 = _("""GCompris""")
GCompris_1 = _('Educational games for children aged 2 to 10')
GCstar_0 = _("""GCstar""")
GCstar_1 = _("""Manage your collections such as movies, books, music""")
GIMP_0 = _("""GIMP""")
GIMP_1 = _("""Open source substitution for Photoshop""")
Glade_0 = _('Glade')
Glade_1 = _('Visually graphical user interface designer')
GMP_0 = _("""GMP""")
GMP_1 = _('GNU high precision arithmetic library')
GNOMEColors_0 = _("""GNOME Colors""")
GNOMEColors_1 = _("""A set of icons with 7 color variations""")
GNOMEDo_0 = _("""GNOME Do""")
GNOMEDo_1 = _("""Desktop launcher which helps you quickly perform actions""")
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
Gnash_0 = _("""Gnash""")
Gnash_1 = _('SWF movie player for web browser')
Gnote_0 = _("""Gnote""")
Gnote_1 = _("""Mono-free alternative to Tomboy Notes""")
GoogleGadgetsGTK_0 = _("""Google gadgets (GTK version)""")
GoogleGadgetsGTK_1 = _("Eye candy widgets most of which are developed by Google's users")
GoogleGadgetsQT_0 = _("""Google gadgets (QT version)""")
GoogleGadgetsQT_1 = _("Eye candy widgets most of which are developed by Google's users")
Gwibber_0 = _("""Gwibber""")
Gwibber_1 = _("""Microblogging client which supports Twitter and Facebook""")
HardwareLister_0 = _("""lshw""")
HardwareLister_1 = _("""A small application which displays detailed hardware information""")
Hedgewars_0 = _("""Hedgewars""")
Hedgewars_1 = _("""Hedgehogs fight enemies with fantastic weapons""")
ImageMagick_0 = _("""ImageMagick""")
ImageMagick_1 = _("""Help you edit images. You can launch it by /usr/bin/display""")
Inkscape_0 = _("""Inkscape""")
Inkscape_1 = _('Vector image designer. It is the open source substitution of CorelDraw.')
K3B_0 = _("""K3B""")
K3B_1 = _('Burn DVD/VCD')
Kadu_0 = _("""Kadu""")
Kadu_1 = _("""Popular instant messenger in Poland""")
Keepassx_0 = _("""Keepassx""")
Keepassx_1 = _("""Password manager which saves many different information e.g. user names and passwords in one single database.""")
Kflickr_0 = _("""kflickr""")
Kflickr_1 = _("""Upload photos to Flickr""")
Kupfer_0 = _("""Kupfer""")
Kupfer_1 = _("""Lightweight desktop launcher""")
Leafpad_0 = _("""Leafpad""")
Leafpad_1 = _("""Simple text editor""")
Liferea_0 = _("""Liferea""")
Liferea_1 = _("""Simple RSS feed reader""")
LinuxDCPP_0 = _("""Linuxdcpp""")
LinuxDCPP_1 = _("""Connect to a central hub then share files and chat with other people.""")
MACChanger_0 = _("""MACChanger""")
MACChanger_1 = _("""Change the MAC address of network interfaces""")
Midori_0 = _("""Midori""")
Midori_1 = _("""Lightweight web browser""")
MiniCom_Ckermit_0 = _("""Minicom and Kermit""")
MiniCom_Ckermit_1 = _('Communication software for embedded MCU boards')
Minitube_0 = _("""Minitube""")
Minitube_1 = _("""This is a simple YouTube client. You enter a keyword, then the software will retrieve all relative URLs from YouTube and play them one after the other.""")
Miro_0 = _("""Miro""")
Miro_1 = _("""Internet TV video player""")
Moonlight_0 = _("""Moonlight""")
Moonlight_1 = _("""Open source implementation of Microsoft Silverlight. It provides Windows media codecs. You can enjoy Windows video in webpages.""")
Multimedia_Codecs_0 = _("""gstreamer multi-media codec""")
Multimedia_Codecs_1 = _("Libraries supporting video playback, audio mixing and non-linear video editing")
Nautilus_Actions_0 = _(""""Actions configuration" entry""")
Nautilus_Actions_1 = _("""Configure which software to be launched on selected files. This entry is in "System"->"Preferences" menu.""")
Nautilus_Audio_Convert_0 = _(""""Convert audio files" entry""")
Nautilus_Audio_Convert_1 = _("""Converts between WAV, OGG, MP3, MPC, FLAC, APE and AAC files.""")
Nautilus_Filename_Repairer_0 = _(""""Repair filename" entry""")
Nautilus_Filename_Repairer_1 = _("""When any file with wrong encoding filename is right clicked, show a "Repair filename" menu item.""")
Nautilus_Gksu_0 = _(""""Open as administrator" entry""")
Nautilus_Gksu_1 = _("""Launch selected files or open selected folder with administration privileges.""")
Nautilus_Image_Converter_0 = _(""""Resize/Rotate images" entries""")
Nautilus_Image_Converter_1 = _("""Resize or rotate selected images.""")
Nautilus_Open_Terminal_0 = _(""""Open in terminal" entry""")
Nautilus_Open_Terminal_1 = _("""Open a terminal in current folder.""")
Nautilus_Script_Collection_Svn_0 = _(""""Subversion commands" entries""")
Nautilus_Script_Collection_Svn_1 = _("""A lot of subversion management command""")
Nautilus_Share_0 = _(""""Share folders" entry""")
Nautilus_Share_1 = _("""Share folders using Samba""")
Nautilus_Wallpaper_0 = _(""""Set as wallpaper" entry""")
Nautilus_Wallpaper_1 = _("""Set an image as wallpaper using context menu""")
Ncurses_and_qt3mt_0 = _("""Ncurses5 and QT3""")
Ncurses_and_qt3mt_1 = _("""Necessary libraries for compiling Linux kernel""")
Netbeans_0 = _("""NetBeans""")
Netbeans_1 = _("""An open source IDE which supports several languages (C, C++, Java, Ruby, etc.) and frameworks (J2SE, J2ME, etc.)""")
Nexuiz_0 = _("""Nexuiz""")
Nexuiz_1 = _("""3D first-person shooter game""")
Octave_0 = _("""Octave""")
Octave_1 = _('Matlab compatible numerical computation appliation')
OpenJDK_0 = _("""OpenJDK 6""")
OpenJDK_1 = _("Open source implementation of Java")
Openshot_0 = _("""Openshot""")
Openshot_1 = _("""Popular non-linear video editor""")
POSIX_ManPages_0 = _("""POSIX library manual pages""")
POSIX_ManPages_1 = _("""Install manual pages about Linux system calls, library calls, and POSIX libraries.""")
Parcellite_0 = _("""Parcellite""")
Parcellite_1 = _("""This is a powerful clipboard manager. It can preserve 25 strings concurrently.""")
PiTiVi_0 = _("""PiTiVi""")
PiTiVi_1 = _("Movie editor designed for both the newcomer and the professional users")
Pidgin_0 = _("""Pidgin""")
Pidgin_1 = _("A chat program which lets you log in multiple chat networks simultaneously. It supports many chat networks.")
PowerTop_0 = _("""PowerTop""")
PowerTop_1 = _("""Help you save power for your laptop.""")
QCad_0 = _("""QCad""")
QCad_1 = _('Open source substitution of AutoCAD')
QT_Creator_0 = _("""Qt Creator""")
QT_Creator_1 = _("""Lightweight Qt IDE""")
Qnapi_0 = _("""Qnapi""")
Qnapi_1 = _("""Help you find and download Poland subtitles for given video file""")
QtiPlot_0 = _("""QtiPlot""")
QtiPlot_1 = _("""Open source substitution of Origin. It is the indispensable plotting application for writing Physics experiments reports.""")
QutIM_0 = _("""qutIM""")
QutIM_1 = _("""Lightweight messaging program""")
R_Language_Basic_0 = _("""R language""")
R_Language_Basic_1 = _("""A powerful statistical computation language and a graphics system.""")
SDL_0 = _("""SDL library""")
SDL_1 = _("""A cross-platform multimedia library designed to provide low level access to hardware.""")
SMPlayer_0 = _("""SMPlayer""")
SMPlayer_1 = _("""Qt frontend for MPlayer""")
ScienceBiology_0 = _("""Med-bio""")
ScienceBiology_1 = _("""A lot of software for molecular biology, structural biology and bioinformatics.""")
Screenlets_0 = _("""Screenlets""")
Screenlets_1 = _("""Add eye candy gadgets on desktop, such as sticky notes, clocks, weather forecasts and so on.""")
Scribus_0 = _("""Scribus""")
Scribus_1 = _("""Professional typesetting software""")
ShikiColors_0 = _("""Shiki Colors""")
ShikiColors_1 = _("""Hybrid theme which is designed to be fast and stable""")
Shutter_0 = _("""Shutter""")
Shutter_1 = _("""A screenshot program. You can take a screenshot of a specific area, window, whole screen, then apply different effects to it.""")
Sonata_0 = _("""Sonata""")
Sonata_1 = _("""Lightweight music player""")
Stardict_0 = _("""Stardict""")
Stardict_1 = _("Popular dictionary software")
StartupManager_0 = _("""Startup Manager""")
StartupManager_1 = _("""Change GRUB settings and themes""")
Svn_Git_bzr_0 = _("""Subversion, Git and Bzr""")
Svn_Git_bzr_1 = _('Popular version control systems')
TeXLive_0 = _("""TeXLive""")
TeXLive_1 = _("""Create a file "example.tex", then compile it by "xelatex example.tex".""")
TheManaWorld_0 = _("""The Mana World""")
TheManaWorld_1 = _("""2D MMORPG""")
Thunderbird_0 = _("""Thunderbird""")
Thunderbird_1 = _("""Email client and RSS reader""")
Transmission_0 = _("""Transmission""")
Transmission_1 = _("""Lightweight bittorrent client""")
TuxPaint_0 = _("""Tux Paint""")
TuxPaint_1 = _('Drawing software for young children three years and up')
Typespeed_0 = _("""Typespeed""")
Typespeed_1 = _("""Type words which are flying from left to right as fast as you can""")
Ubuntu_Studio_Theme_0 = _("""Ubuntu Studio Theme""")
Ubuntu_Studio_Theme_1 = _("A theme of Ubuntu which is aimed at audio, video and graphic enthusiast")
Umbrello_0 = _("""Umbrello""")
Umbrello_1 = _("""UML modelling software""")
VIM_0 = _("""VIM""")
VIM_1 = _("Enhanced text editor")
VLC_0 = _("""VLC""")
VLC_1 = _("""Media player and media format converter""")
VirtualBox_0 = _("""VirtualBox open source edition""")
VirtualBox_1 = _("""It is the only professional virtual machine which is freely available under the terms of GPL.""")
Vuze_Karmic_0 = _("""Vuze""")
Vuze_Karmic_1 = _('Help you download files via bittorrent network and search videos')
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
WorldofPadman_1 = _("""Funny shooter game""")
Wormux_0 = _("""Wormux""")
Wormux_1 = _("""Funny fight game on 2D maps""")
Zhcon_0 = _("""Zhcon""")
Zhcon_1 = _("""Help you display Chinese characters in TTY terminal. You can launch it by "zhcon --utf8".""")
Zim_0 = _("""Zim""")
Zim_1 = _("""Notebook software which helps you create a wiki to your desktop""")

