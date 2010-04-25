%define name ailurus
%define version 10.04.2.2
%define unmangled_version 10.04.2.2
%define release 1
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: makes Linux easier to use
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://homerxing.fedorapeople.org/%{name}-%{unmangled_version}.tar.gz
License: GPLv2+
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Homer Xing <homer.xing@gmail.com>
Requires: python pygtk2 notify-python vte rpm-python pygobject2 dbus-python wget unzip xterm
Url: http://ailurus.googlecode.com/
BuildRequires: python python-devel python-distutils-extra intltool sed

%description
Ailurus is an application which makes Linux easier to use.

Features:
* Help users learn some Linux skills
* Install/remove some nice applications
* Enable/disable some third party repositories
* Display information about BIOS, motherboard, CPU and battery
* Show/Hide Computer, Home folder, Trash icon and Network icon on desktop
* Configure Nautilus thumbnail cache
* Configure Nautilus context menu
* Configure Window behavior
* Configure GNOME auto-start applications
* Show/Hide GNOME splash screen

%prep
%setup -q -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/python2.6/site-packages/ailurus/clean_up_pane.py
/usr/lib/python2.6/site-packages/ailurus/libapp.py
/usr/lib/python2.6/site-packages/ailurus/show_a_linux_skill_bubble.py
/usr/lib/python2.6/site-packages/ailurus/libsetting.py
/usr/lib/python2.6/site-packages/ailurus/loader.py
/usr/lib/python2.6/site-packages/ailurus/lib.py
/usr/lib/python2.6/site-packages/ailurus/system_setting_pane.py
/usr/lib/python2.6/site-packages/ailurus/__init__.py
/usr/lib/python2.6/site-packages/ailurus/install_remove_pane.py
/usr/lib/python2.6/site-packages/ailurus/info_pane.py
/usr/lib/python2.6/site-packages/ailurus/libu.py
/usr/lib/python2.6/site-packages/ailurus/daemon.py
/usr/lib/python2.6/site-packages/ailurus/main.py
/usr/lib/python2.6/site-packages/ailurus/common/hardwareinfo.py
/usr/lib/python2.6/site-packages/ailurus/common/apps_eclipse.py
/usr/lib/python2.6/site-packages/ailurus/common/setting.py
/usr/lib/python2.6/site-packages/ailurus/common/osinfo.py
/usr/lib/python2.6/site-packages/ailurus/common/__init__.py
/usr/lib/python2.6/site-packages/ailurus/common/menu.py
/usr/lib/python2.6/site-packages/ailurus/common/apps.py
/usr/lib/python2.6/site-packages/ailurus/common/tips.py
/usr/lib/python2.6/site-packages/ailurus/gnome/setting.py
/usr/lib/python2.6/site-packages/ailurus/gnome/osinfo.py
/usr/lib/python2.6/site-packages/ailurus/gnome/__init__.py
/usr/lib/python2.6/site-packages/ailurus/gnome/apps.py
/usr/lib/python2.6/site-packages/ailurus/gnome/tips.py
/usr/lib/python2.6/site-packages/ailurus/fedora/fastest_mirror_pane.py
/usr/lib/python2.6/site-packages/ailurus/fedora/osinfo.py
/usr/lib/python2.6/site-packages/ailurus/fedora/__init__.py
/usr/lib/python2.6/site-packages/ailurus/fedora/apps.py
/usr/lib/python2.6/site-packages/ailurus/fedora/rpm_recovery_pane.py
/usr/lib/python2.6/site-packages/ailurus/fedora/libserver.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/fastest_mirror_pane.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app4.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/setting.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/apt_recovery_pane.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/quick_setup.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/osinfo.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app3.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/__init__.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app1.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/menu.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/apps.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/third_party_repos.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/tips.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/libserver.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app0.py
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app2.py
/usr/lib/python2.6/site-packages/ailurus/support/terminal_single_thread.py
/usr/lib/python2.6/site-packages/ailurus/support/windowpos.py
/usr/lib/python2.6/site-packages/ailurus/support/dumpaptcache2.py
/usr/lib/python2.6/site-packages/ailurus/support/tipoftheday.py
/usr/lib/python2.6/site-packages/ailurus/support/keygrabber.py
/usr/lib/python2.6/site-packages/ailurus/support/multidragview.py
/usr/lib/python2.6/site-packages/ailurus/support/safely_deletable_pkgs.py
/usr/lib/python2.6/site-packages/ailurus/support/dumpaptcache.py
/usr/lib/python2.6/site-packages/ailurus/support/splashwindow.py
/usr/lib/python2.6/site-packages/ailurus/support/__init__.py
/usr/lib/python2.6/site-packages/ailurus/support/searchbox.py
/usr/lib/python2.6/site-packages/ailurus/support/terminal.py
/usr/lib/python2.6/site-packages/ailurus/support/pangobuffer.py
/usr/lib/python2.6/site-packages/ailurus/support/undobuffer.py
/usr/lib/python2.6/site-packages/ailurus/support/dumprpmcache.py
/usr/lib/python2.6/site-packages/ailurus/support/releasenotesviewer.py
/usr/lib/python2.6/site-packages/ailurus/clean_up_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/clean_up_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/libapp.pyc
/usr/lib/python2.6/site-packages/ailurus/libapp.pyo
/usr/lib/python2.6/site-packages/ailurus/show_a_linux_skill_bubble.pyc
/usr/lib/python2.6/site-packages/ailurus/show_a_linux_skill_bubble.pyo
/usr/lib/python2.6/site-packages/ailurus/libsetting.pyc
/usr/lib/python2.6/site-packages/ailurus/libsetting.pyo
/usr/lib/python2.6/site-packages/ailurus/loader.pyc
/usr/lib/python2.6/site-packages/ailurus/loader.pyo
/usr/lib/python2.6/site-packages/ailurus/lib.pyc
/usr/lib/python2.6/site-packages/ailurus/lib.pyo
/usr/lib/python2.6/site-packages/ailurus/system_setting_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/system_setting_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/__init__.pyc
/usr/lib/python2.6/site-packages/ailurus/__init__.pyo
/usr/lib/python2.6/site-packages/ailurus/install_remove_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/install_remove_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/info_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/info_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/libu.pyc
/usr/lib/python2.6/site-packages/ailurus/libu.pyo
/usr/lib/python2.6/site-packages/ailurus/daemon.pyc
/usr/lib/python2.6/site-packages/ailurus/daemon.pyo
/usr/lib/python2.6/site-packages/ailurus/main.pyc
/usr/lib/python2.6/site-packages/ailurus/main.pyo
/usr/lib/python2.6/site-packages/ailurus/common/hardwareinfo.pyc
/usr/lib/python2.6/site-packages/ailurus/common/hardwareinfo.pyo
/usr/lib/python2.6/site-packages/ailurus/common/apps_eclipse.pyc
/usr/lib/python2.6/site-packages/ailurus/common/apps_eclipse.pyo
/usr/lib/python2.6/site-packages/ailurus/common/setting.pyc
/usr/lib/python2.6/site-packages/ailurus/common/setting.pyo
/usr/lib/python2.6/site-packages/ailurus/common/osinfo.pyc
/usr/lib/python2.6/site-packages/ailurus/common/osinfo.pyo
/usr/lib/python2.6/site-packages/ailurus/common/__init__.pyc
/usr/lib/python2.6/site-packages/ailurus/common/__init__.pyo
/usr/lib/python2.6/site-packages/ailurus/common/menu.pyc
/usr/lib/python2.6/site-packages/ailurus/common/menu.pyo
/usr/lib/python2.6/site-packages/ailurus/common/apps.pyc
/usr/lib/python2.6/site-packages/ailurus/common/apps.pyo
/usr/lib/python2.6/site-packages/ailurus/common/tips.pyc
/usr/lib/python2.6/site-packages/ailurus/common/tips.pyo
/usr/lib/python2.6/site-packages/ailurus/gnome/setting.pyc
/usr/lib/python2.6/site-packages/ailurus/gnome/setting.pyo
/usr/lib/python2.6/site-packages/ailurus/gnome/osinfo.pyc
/usr/lib/python2.6/site-packages/ailurus/gnome/osinfo.pyo
/usr/lib/python2.6/site-packages/ailurus/gnome/__init__.pyc
/usr/lib/python2.6/site-packages/ailurus/gnome/__init__.pyo
/usr/lib/python2.6/site-packages/ailurus/gnome/apps.pyc
/usr/lib/python2.6/site-packages/ailurus/gnome/apps.pyo
/usr/lib/python2.6/site-packages/ailurus/gnome/tips.pyc
/usr/lib/python2.6/site-packages/ailurus/gnome/tips.pyo
/usr/lib/python2.6/site-packages/ailurus/fedora/fastest_mirror_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/fedora/fastest_mirror_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/fedora/osinfo.pyc
/usr/lib/python2.6/site-packages/ailurus/fedora/osinfo.pyo
/usr/lib/python2.6/site-packages/ailurus/fedora/__init__.pyc
/usr/lib/python2.6/site-packages/ailurus/fedora/__init__.pyo
/usr/lib/python2.6/site-packages/ailurus/fedora/apps.pyc
/usr/lib/python2.6/site-packages/ailurus/fedora/apps.pyo
/usr/lib/python2.6/site-packages/ailurus/fedora/rpm_recovery_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/fedora/rpm_recovery_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/fedora/libserver.pyc
/usr/lib/python2.6/site-packages/ailurus/fedora/libserver.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/fastest_mirror_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/fastest_mirror_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app4.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app4.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/setting.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/setting.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/apt_recovery_pane.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/apt_recovery_pane.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/quick_setup.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/quick_setup.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/osinfo.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/osinfo.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app3.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app3.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/__init__.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/__init__.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app1.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app1.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/menu.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/menu.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/apps.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/apps.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/third_party_repos.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/third_party_repos.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/tips.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/tips.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/libserver.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/libserver.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app0.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app0.pyo
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app2.pyc
/usr/lib/python2.6/site-packages/ailurus/ubuntu/app2.pyo
/usr/lib/python2.6/site-packages/ailurus/support/terminal_single_thread.pyc
/usr/lib/python2.6/site-packages/ailurus/support/terminal_single_thread.pyo
/usr/lib/python2.6/site-packages/ailurus/support/windowpos.pyc
/usr/lib/python2.6/site-packages/ailurus/support/windowpos.pyo
/usr/lib/python2.6/site-packages/ailurus/support/dumpaptcache2.pyc
/usr/lib/python2.6/site-packages/ailurus/support/dumpaptcache2.pyo
/usr/lib/python2.6/site-packages/ailurus/support/tipoftheday.pyc
/usr/lib/python2.6/site-packages/ailurus/support/tipoftheday.pyo
/usr/lib/python2.6/site-packages/ailurus/support/keygrabber.pyc
/usr/lib/python2.6/site-packages/ailurus/support/keygrabber.pyo
/usr/lib/python2.6/site-packages/ailurus/support/multidragview.pyc
/usr/lib/python2.6/site-packages/ailurus/support/multidragview.pyo
/usr/lib/python2.6/site-packages/ailurus/support/safely_deletable_pkgs.pyc
/usr/lib/python2.6/site-packages/ailurus/support/safely_deletable_pkgs.pyo
/usr/lib/python2.6/site-packages/ailurus/support/dumpaptcache.pyc
/usr/lib/python2.6/site-packages/ailurus/support/dumpaptcache.pyo
/usr/lib/python2.6/site-packages/ailurus/support/splashwindow.pyc
/usr/lib/python2.6/site-packages/ailurus/support/splashwindow.pyo
/usr/lib/python2.6/site-packages/ailurus/support/__init__.pyc
/usr/lib/python2.6/site-packages/ailurus/support/__init__.pyo
/usr/lib/python2.6/site-packages/ailurus/support/searchbox.pyc
/usr/lib/python2.6/site-packages/ailurus/support/searchbox.pyo
/usr/lib/python2.6/site-packages/ailurus/support/terminal.pyc
/usr/lib/python2.6/site-packages/ailurus/support/terminal.pyo
/usr/lib/python2.6/site-packages/ailurus/support/pangobuffer.pyc
/usr/lib/python2.6/site-packages/ailurus/support/pangobuffer.pyo
/usr/lib/python2.6/site-packages/ailurus/support/undobuffer.pyc
/usr/lib/python2.6/site-packages/ailurus/support/undobuffer.pyo
/usr/lib/python2.6/site-packages/ailurus/support/dumprpmcache.pyc
/usr/lib/python2.6/site-packages/ailurus/support/dumprpmcache.pyo
/usr/lib/python2.6/site-packages/ailurus/support/releasenotesviewer.pyc
/usr/lib/python2.6/site-packages/ailurus/support/releasenotesviewer.pyo
/usr/bin/ailurus
/usr/share/man/man1/ailurus.1
/usr/share/desktop-directories/ailurus_quick_start.directory
/etc/xdg/menus/applications-merged/ailurus.menu
/usr/share/applications/ailurus-recovery.desktop
/usr/share/applications/ailurus-information.desktop
/usr/share/applications/ailurus-clean-up.desktop
/usr/share/applications/ailurus-install-software.desktop
/usr/share/applications/ailurus.desktop
/usr/share/applications/ailurus-fastest-repository.desktop
/usr/share/applications/ailurus-system-setting.desktop
/usr/share/ailurus/ChangeLog
/usr/share/ailurus/data/appicons/FFWeaveSync35.png
/usr/share/ailurus/data/appicons/FFAdblock.png
/usr/share/ailurus/data/appicons/FFFireBug.png
/usr/share/ailurus/data/appicons/GEdit_Suitable_For_Programmer.png
/usr/share/ailurus/data/appicons/FFTamperData.png
/usr/share/ailurus/data/appicons/ImageMagick.png
/usr/share/ailurus/data/appicons/WINE_2.png
/usr/share/ailurus/data/appicons/GNOMEArtNextGen.png
/usr/share/ailurus/data/appicons/OSD_Lyrics.png
/usr/share/ailurus/data/appicons/TeXLive2009.png
/usr/share/ailurus/data/appicons/QCad.png
/usr/share/ailurus/data/appicons/WINE.png
/usr/share/ailurus/data/appicons/AutoTools.png
/usr/share/ailurus/data/appicons/QueryBeforeRmALotFiles.png
/usr/share/ailurus/data/appicons/HITTeXTemplate.png
/usr/share/ailurus/data/appicons/R_Language_Basic.png
/usr/share/ailurus/data/appicons/scim.png
/usr/share/ailurus/data/appicons/Ubuntu_Studio_Theme.png
/usr/share/ailurus/data/appicons/Eclipse.png
/usr/share/ailurus/data/appicons/FFSeoQuake.png
/usr/share/ailurus/data/appicons/TeXLive2007.png
/usr/share/ailurus/data/appicons/Varkon.png
/usr/share/ailurus/data/appicons/VIM_and_VIMRC.png
/usr/share/ailurus/data/appicons/PBC.png
/usr/share/ailurus/data/appicons/Repo_WINE.png
/usr/share/ailurus/data/appicons/Full_Language_Pack.png
/usr/share/ailurus/data/appicons/freecad.png
/usr/share/ailurus/data/appicons/FFWebDeveloper.png
/usr/share/ailurus/data/appicons/Screenlets.png
/usr/share/ailurus/data/appicons/OpenJDK6.png
/usr/share/ailurus/data/appicons/FFGreaseMonkey.png
/usr/share/ailurus/data/appicons/Typespeed.png
/usr/share/ailurus/data/appicons/Repo_Firefox_3_6.png
/usr/share/ailurus/data/appicons/PowerTop.png
/usr/share/ailurus/data/appicons/Flash_Player.png
/usr/share/ailurus/data/appicons/SDL.png
/usr/share/ailurus/data/appicons/downthemall.png
/usr/share/ailurus/data/appicons/FFYetAnotherSmoothScrolling.png
/usr/share/ailurus/data/appicons/Speed_Up_Firefox.png
/usr/share/ailurus/data/appicons/Zhcon.png
/usr/share/ailurus/data/appicons/StartupManager.png
/usr/share/ailurus/data/appicons/_tasksel.png
/usr/share/ailurus/data/appicons/Repo_OSD_Lyrics.png
/usr/share/ailurus/data/appicons/Evince_Read_Chinese_PDF.png
/usr/share/ailurus/data/appicons/VirtualBox.png
/usr/share/ailurus/data/appicons/ChineseAcademyofSciencesTeXTemplate.png
/usr/share/ailurus/data/appicons/bluetooth.png
/usr/share/ailurus/data/appicons/memory.png
/usr/share/ailurus/data/appicons/ColorfulBashPromptSymbols.png
/usr/share/ailurus/data/appicons/Boost.png
/usr/share/ailurus/data/appicons/Moonlight.png
/usr/share/ailurus/data/appicons/FFDownloadStatusBar.png
/usr/share/ailurus/data/appicons/Workrave_And_Auto_Start_It.png
/usr/share/ailurus/data/appicons/R_Language_Full.png
/usr/share/ailurus/data/appicons/Fctix.png
/usr/share/ailurus/data/appicons/POSIX_ManPages.png
/usr/share/ailurus/data/appicons/Multimedia_Codecs.png
/usr/share/ailurus/data/appicons/CHMSee_Read_CHM_Documents.png
/usr/share/ailurus/data/appicons/GStreamer_Codecs.png
/usr/share/ailurus/data/appicons/FFCleanHide.png
/usr/share/ailurus/data/appicons/FFChromeTheme_3_5.png
/usr/share/ailurus/data/appicons/FFUserAgentSwitcher.png
/usr/share/ailurus/data/appicons/GMP.png
/usr/share/ailurus/data/appicons/FFLiveHTTPHeaders.png
/usr/share/ailurus/data/appicons/ComicVODPlayer_new.png
/usr/share/ailurus/data/appicons/Svn_Git_bzr.png
/usr/share/ailurus/data/appicons/Umbrello.png
/usr/share/ailurus/data/appicons/CompizSettingManager.png
/usr/share/ailurus/data/appicons/CreateDesktopFolder.png
/usr/share/ailurus/data/appicons/WINE_1.png
/usr/share/ailurus/data/appicons/MiniCom_Ckermit.png
/usr/share/ailurus/data/appicons/FFRadioGet.png
/usr/share/ailurus/data/appicons/FFTabMixLite.png
/usr/share/ailurus/data/appicons/Ncurses_and_qt3mt.png
/usr/share/ailurus/data/appicons/Eliminate_CUPS_Cannot_Print_Bug.png
/usr/share/ailurus/data/appicons/Build_Essential.png
/usr/share/ailurus/data/appicons/FFDownThemAll.png
/usr/share/ailurus/data/appicons/FFEasyDragToGo.png
/usr/share/ailurus/data/appicons/Gedit_GB2312.png
/usr/share/ailurus/data/appicons/FFNoscript.png
/usr/share/ailurus/data/appicons/qq.png
/usr/share/ailurus/data/appicons/QtiPlot.png
/usr/share/ailurus/data/appicons/Gnash.png
/usr/share/ailurus/data/appicons/FFViewSourceChart.png
/usr/share/ailurus/data/appicons/Adobe_Flash_Player.png
/usr/share/ailurus/data/appicons/CDT.png
/usr/share/ailurus/data/appicons/DisableGettyKarmic.png
/usr/share/ailurus/data/appicons/CompizSettingManagerSimple.png
/usr/share/ailurus/data/appicons/shada-radio.png
/usr/share/ailurus/data/appicons/Repo_VirtualBox.png
/usr/share/ailurus/data/appicons/brlcad.png
/usr/share/ailurus/data/appicons/VirtualBox_OSE.png
/usr/share/ailurus/data/appicons/Electric.png
/usr/share/ailurus/data/appicons/TsingHuaTeXTemplate.png
/usr/share/ailurus/data/appicons/CUPS.png
/usr/share/ailurus/data/appicons/ChangeTerminalColor.png
/usr/share/ailurus/data/appicons/default.png
/usr/share/ailurus/data/appicons/DisableGetty.png
/usr/share/ailurus/data/appicons/XJTUTeXTemplate.png
/usr/share/ailurus/data/appicons/FFFlashgot.png
/usr/share/ailurus/data/appicons/FreeGLut3.png
/usr/share/ailurus/data/appicons/Bioclipse.png
/usr/share/ailurus/data/appicons/Ctags_Cscope.png
/usr/share/ailurus/data/appicons/ScienceBiology.png
/usr/share/ailurus/data/appicons/FFChromeTheme_3_0.png
/usr/share/ailurus/data/appicons/FFYSlow.png
/usr/share/ailurus/data/appicons/Enhance_Decompression_Capability.png
/usr/share/ailurus/data/appicons/FFFoxyProxy.png
/usr/share/ailurus/data/appicons/CommonUsedProgrammingPackages.png
/usr/share/ailurus/data/appicons/Octave.png
/usr/share/ailurus/data/appicons/nautilus.png
/usr/share/ailurus/data/appicons/Generic_Genome_Browser.png
/usr/share/ailurus/data/appicons/FFAutoProxy.png
/usr/share/ailurus/data/appicons/FFFireGesture.png
/usr/share/ailurus/data/appicons/OpenJUMP.png
/usr/share/ailurus/data/appicons/Decompression_Capability.png
/usr/share/ailurus/data/other_icons/Repo_Acire.png
/usr/share/ailurus/data/other_icons/Nautilus_Filename_Repairer.png
/usr/share/ailurus/data/other_icons/toolbar_forward.png
/usr/share/ailurus/data/other_icons/NScripts.png
/usr/share/ailurus/data/other_icons/toolbar_quit.png
/usr/share/ailurus/data/other_icons/RSSOwl.png
/usr/share/ailurus/data/other_icons/toolbar_back.png
/usr/share/ailurus/data/other_icons/ChildsPlay.png
/usr/share/ailurus/data/other_icons/quicksetup.png
/usr/share/ailurus/data/other_icons/TuxPaint.png
/usr/share/ailurus/data/other_icons/Nautilus_Search_Tool.png
/usr/share/ailurus/data/other_icons/Repo_Ailurus.png
/usr/share/ailurus/data/other_icons/Repo_Canonical_Partner.png
/usr/share/ailurus/data/other_icons/Parcellite.png
/usr/share/ailurus/data/other_icons/Bluetooth.png
/usr/share/ailurus/data/other_icons/GCompris.png
/usr/share/ailurus/data/other_icons/Stardict_without_Dictionaries.png
/usr/share/ailurus/data/other_icons/blank.png
/usr/share/ailurus/data/other_icons/ubuntu.png
/usr/share/ailurus/data/other_icons/Nautilus_Share.png
/usr/share/ailurus/data/other_icons/Nautilus_Gksu.png
/usr/share/ailurus/data/other_icons/AWN.png
/usr/share/ailurus/data/other_icons/fedora.png
/usr/share/ailurus/data/other_icons/Nautilus_Script_Collection_Svn.png
/usr/share/ailurus/data/other_icons/Pidgin_beta.png
/usr/share/ailurus/data/other_icons/WorldofPadman.png
/usr/share/ailurus/data/other_icons/PlayOnLinux.png
/usr/share/ailurus/data/other_icons/Tor.png
/usr/share/ailurus/data/other_icons/Extcalc.png
/usr/share/ailurus/data/other_icons/Vuze_Karmic.png
/usr/share/ailurus/data/other_icons/python.png
/usr/share/ailurus/data/other_icons/CodeBlocks.png
/usr/share/ailurus/data/other_icons/Getting_things_gnome.png
/usr/share/ailurus/data/other_icons/wallpaper-tray.png
/usr/share/ailurus/data/other_icons/Audacity.png
/usr/share/ailurus/data/other_icons/m_clean_up.png
/usr/share/ailurus/data/other_icons/Songbird.png
/usr/share/ailurus/data/other_icons/done.png
/usr/share/ailurus/data/other_icons/Speedup_Nautilus.png
/usr/share/ailurus/data/other_icons/ailurus_for_splash.png
/usr/share/ailurus/data/other_icons/Nautilus_Image_Converter.png
/usr/share/ailurus/data/other_icons/tux.png
/usr/share/ailurus/data/other_icons/toolbar_study.png
/usr/share/ailurus/data/other_icons/Nautilus_Actions.png
/usr/share/ailurus/data/other_icons/toolbar_disable.png
/usr/share/ailurus/data/other_icons/Gnome_color.png
/usr/share/ailurus/data/other_icons/Repo_XBMC.png
/usr/share/ailurus/data/other_icons/Bluefish.png
/usr/share/ailurus/data/other_icons/QT_Creator.png
/usr/share/ailurus/data/other_icons/Shutter.png
/usr/share/ailurus/data/other_icons/Liferea.png
/usr/share/ailurus/data/other_icons/Chromium.png
/usr/share/ailurus/data/other_icons/Repo_Songbird.png
/usr/share/ailurus/data/other_icons/Stardict.png
/usr/share/ailurus/data/other_icons/Blueman.png
/usr/share/ailurus/data/other_icons/s_nautilus.png
/usr/share/ailurus/data/other_icons/Nautilus_Wallpaper.png
/usr/share/ailurus/data/other_icons/Audacious.png
/usr/share/ailurus/data/other_icons/Nautilus_Audio_Convert.png
/usr/share/ailurus/data/other_icons/toolbar_enable.png
/usr/share/ailurus/data/other_icons/Acire.png
/usr/share/ailurus/data/other_icons/XBMC.png
/usr/share/ailurus/data/other_icons/fail.png
/usr/share/ailurus/data/other_icons/s_desktop.png
/usr/share/ailurus/data/other_icons/Nautilus_Open_Terminal.png
/usr/share/ailurus/data/other_icons/PiTiVi.png
/usr/share/ailurus/data/other_icons/Netbeans.png
/usr/share/ailurus/data/other_icons/FireWall.png
/usr/share/ailurus/data/other_icons/started.png
/usr/share/ailurus/data/other_icons/nautilus.png
/usr/share/ailurus/data/suyun_icons/notify-icon.png
/usr/share/ailurus/data/suyun_icons/update.png
/usr/share/ailurus/data/suyun_icons/logo.png
/usr/share/ailurus/data/suyun_icons/m_check_update.png
/usr/share/ailurus/data/suyun_icons/shortcut.png
/usr/share/ailurus/data/suyun_icons/default.png
/usr/share/ailurus/data/suyun_icons/logo_with_reflection.png
/usr/share/ailurus/data/umut_icons/p_math.png
/usr/share/ailurus/data/umut_icons/i_java.png
/usr/share/ailurus/data/umut_icons/i_battery.png
/usr/share/ailurus/data/umut_icons/p_firefox.png
/usr/share/ailurus/data/umut_icons/s_session.png
/usr/share/ailurus/data/umut_icons/eclipse.png
/usr/share/ailurus/data/umut_icons/s_font.png
/usr/share/ailurus/data/umut_icons/i_bios.png
/usr/share/ailurus/data/umut_icons/p_game.png
/usr/share/ailurus/data/umut_icons/i_X.png
/usr/share/ailurus/data/umut_icons/s_window.png
/usr/share/ailurus/data/umut_icons/s_icon.png
/usr/share/ailurus/data/umut_icons/i_motherboard.png
/usr/share/ailurus/data/umut_icons/p_repository.png
/usr/share/ailurus/data/umut_icons/i_ethernet.png
/usr/share/ailurus/data/umut_icons/p_em.png
/usr/share/ailurus/data/umut_icons/p_language_support.png
/usr/share/ailurus/data/umut_icons/i_uptime.png
/usr/share/ailurus/data/umut_icons/s_sound.png
/usr/share/ailurus/data/umut_icons/i_cpu.png
/usr/share/ailurus/data/umut_icons/s_memory.png
/usr/share/ailurus/data/umut_icons/p_internet.png
/usr/share/ailurus/data/umut_icons/i_gcc.png
/usr/share/ailurus/data/umut_icons/i_opengl.png
/usr/share/ailurus/data/umut_icons/p_latex.png
/usr/share/ailurus/data/umut_icons/bug.png
/usr/share/ailurus/data/umut_icons/s_power.png
/usr/share/ailurus/data/umut_icons/m_propose_suggestion.png
/usr/share/ailurus/data/umut_icons/s_restriction.png
/usr/share/ailurus/data/umut_icons/i_locale.png
/usr/share/ailurus/data/umut_icons/i_firefox.png
/usr/share/ailurus/data/umut_icons/i_host.png
/usr/share/ailurus/data/umut_icons/i_default.png
/usr/share/ailurus/data/umut_icons/i_userinfo.png
/usr/share/ailurus/data/umut_icons/p_education.png
/usr/share/ailurus/data/umut_icons/quick_setup.png
/usr/share/ailurus/data/umut_icons/p_statistics.png
/usr/share/ailurus/data/umut_icons/s_shortcutkey.png
/usr/share/ailurus/data/umut_icons/p_biology.png
/usr/share/ailurus/data/umut_icons/i_gnome.png
/usr/share/ailurus/data/umut_icons/p_hardware.png
/usr/share/ailurus/data/umut_icons/p_multimedia.png
/usr/share/ailurus/data/umut_icons/p_virtualmachine.png
/usr/share/ailurus/data/umut_icons/s_terminal.png
/usr/share/ailurus/data/umut_icons/p_appearance.png
/usr/share/ailurus/data/umut_icons/p_server.png
/usr/share/ailurus/data/umut_icons/p_geography.png
/usr/share/ailurus/data/umut_icons/p_develop.png
/usr/share/ailurus/data/umut_icons/default.png
/usr/share/ailurus/data/umut_icons/m_quit.png
/usr/share/ailurus/data/umut_icons/i_display.png
/usr/share/ailurus/data/umut_icons/s_menu.png
/usr/share/ailurus/data/umut_icons/p_widgets.png
/usr/share/ailurus/data/umut_icons/i_audiocard.png
/usr/share/ailurus/data/umut_icons/s_update.png
/usr/share/ailurus/data/umut_icons/p_embedded_system.png
/usr/share/ailurus/data/umut_icons/p_office.png
/usr/share/ailurus/data/umut_icons/s_network.png
/usr/share/ailurus/data/umut_icons/i_memory.png
/usr/share/ailurus/data/sora_icons/m_others.png
/usr/share/ailurus/data/sora_icons/m_study_linux.png
/usr/share/ailurus/data/sora_icons/m_linux_setting.png
/usr/share/ailurus/data/sora_icons/m_propose_suggestion.png
/usr/share/ailurus/data/sora_icons/m_install_remove.png
/usr/share/ailurus/data/sora_icons/m_linux.png
/usr/share/ailurus/data/sora_icons/m_recovery.png
/usr/share/ailurus/data/sora_icons/m_quit.png
/usr/share/ailurus/data/sora_icons/m_fastest_repos.png
/usr/share/ailurus/data/sora_icons/m_hardware.png
/usr/share/ailurus/data/sora_icons/m_tip_of_the_day.png
/usr/share/ailurus/data/sora_icons/m_preference.png
/usr/share/ailurus/data/velly_icons/quick_start.png
/usr/share/ailurus/data/velly_icons/m_linux_info.png
/usr/share/ailurus/data/velly_icons/m_clean_up.png
/usr/share/ailurus/data/velly_icons/m_setting.png
/usr/share/ailurus/data/velly_icons/m_install_software.png
/usr/share/ailurus/data/velly_icons/m_recovery.png
/usr/share/ailurus/data/velly_icons/m_fastest_repos.png
/usr/share/ailurus/data/velly_icons/m_hardware_info.png
/usr/share/dbus-1/system-services/cn.ailurus.service
/etc/dbus-1/system.d/cn.ailurus.conf
/usr/share/PolicyKit/policy/cn.ailurus.policy
/usr/share/polkit-1/actions/cn.ailurus.policy
/usr/share/ailurus/support/ubuntu-native-64bit-flash-installer.sh
/usr/share/ailurus/support/show-a-linux-skill-bubble
/usr/share/ailurus/support/enable_sudo
/usr/share/ailurus/support/ailurus-daemon
/usr/share/ailurus/support/wine_wqy_font.reg
/usr/share/ailurus/support/disable_sudo
/usr/share/ailurus/support/cn.ailurus.service
/usr/share/ailurus/support/cn.ailurus.conf
/usr/share/locale/en_CA/LC_MESSAGES/ailurus.mo
/usr/share/locale/da/LC_MESSAGES/ailurus.mo
/usr/share/locale/uk/LC_MESSAGES/ailurus.mo
/usr/share/locale/pt_BR/LC_MESSAGES/ailurus.mo
/usr/share/locale/ru/LC_MESSAGES/ailurus.mo
/usr/share/locale/sv/LC_MESSAGES/ailurus.mo
/usr/share/locale/cs/LC_MESSAGES/ailurus.mo
/usr/share/locale/tr/LC_MESSAGES/ailurus.mo
/usr/share/locale/fi/LC_MESSAGES/ailurus.mo
/usr/share/locale/bn/LC_MESSAGES/ailurus.mo
/usr/share/locale/nn/LC_MESSAGES/ailurus.mo
/usr/share/locale/gl/LC_MESSAGES/ailurus.mo
/usr/share/locale/zh_HK/LC_MESSAGES/ailurus.mo
/usr/share/locale/be/LC_MESSAGES/ailurus.mo
/usr/share/locale/ca/LC_MESSAGES/ailurus.mo
/usr/share/locale/kk/LC_MESSAGES/ailurus.mo
/usr/share/locale/mk/LC_MESSAGES/ailurus.mo
/usr/share/locale/nb/LC_MESSAGES/ailurus.mo
/usr/share/locale/fa/LC_MESSAGES/ailurus.mo
/usr/share/locale/zh_TW/LC_MESSAGES/ailurus.mo
/usr/share/locale/ja/LC_MESSAGES/ailurus.mo
/usr/share/locale/te/LC_MESSAGES/ailurus.mo
/usr/share/locale/nl/LC_MESSAGES/ailurus.mo
/usr/share/locale/oc/LC_MESSAGES/ailurus.mo
/usr/share/locale/pl/LC_MESSAGES/ailurus.mo
/usr/share/locale/bg/LC_MESSAGES/ailurus.mo
/usr/share/locale/hi/LC_MESSAGES/ailurus.mo
/usr/share/locale/bs/LC_MESSAGES/ailurus.mo
/usr/share/locale/fr/LC_MESSAGES/ailurus.mo
/usr/share/locale/eo/LC_MESSAGES/ailurus.mo
/usr/share/locale/id/LC_MESSAGES/ailurus.mo
/usr/share/locale/lt/LC_MESSAGES/ailurus.mo
/usr/share/locale/th/LC_MESSAGES/ailurus.mo
/usr/share/locale/sk/LC_MESSAGES/ailurus.mo
/usr/share/locale/is/LC_MESSAGES/ailurus.mo
/usr/share/locale/fo/LC_MESSAGES/ailurus.mo
/usr/share/locale/it/LC_MESSAGES/ailurus.mo
/usr/share/locale/de/LC_MESSAGES/ailurus.mo
/usr/share/locale/ar/LC_MESSAGES/ailurus.mo
/usr/share/locale/ms/LC_MESSAGES/ailurus.mo
/usr/share/locale/pt/LC_MESSAGES/ailurus.mo
/usr/share/locale/zh_CN/LC_MESSAGES/ailurus.mo
/usr/share/locale/es/LC_MESSAGES/ailurus.mo
/usr/share/locale/ka/LC_MESSAGES/ailurus.mo
/usr/share/locale/ro/LC_MESSAGES/ailurus.mo
/usr/share/locale/he/LC_MESSAGES/ailurus.mo
/usr/share/locale/jv/LC_MESSAGES/ailurus.mo
/usr/share/locale/ml/LC_MESSAGES/ailurus.mo
/usr/share/locale/el/LC_MESSAGES/ailurus.mo
/usr/share/locale/vi/LC_MESSAGES/ailurus.mo
/usr/share/locale/sl/LC_MESSAGES/ailurus.mo
/usr/share/locale/sq/LC_MESSAGES/ailurus.mo
/usr/share/locale/ga/LC_MESSAGES/ailurus.mo
/usr/share/locale/hu/LC_MESSAGES/ailurus.mo
/usr/share/locale/sr/LC_MESSAGES/ailurus.mo
/usr/share/locale/ko/LC_MESSAGES/ailurus.mo
/usr/share/locale/en_AU/LC_MESSAGES/ailurus.mo
/usr/share/locale/en_GB/LC_MESSAGES/ailurus.mo
/usr/share/omf/ailurus
/usr/lib/python2.6/site-packages/ailurus-10.04.2.2-py2.6.egg-info

%changelog
* Sat Apr 24 2010 Homer Xing <homer.xing@gmail.com> 10.04.2-1
- Initial package
