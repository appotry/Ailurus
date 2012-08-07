%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:			ailurus
Version: 12.08
Release:		1%{?dist}
Summary:		A tool for backuping a name list of installed software
Group:			Applications/System
License:		GPLv2+
URL:			http://ailurus.googlecode.com/
Source:		http://ailurus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python2-devel python-distutils-extra intltool
BuildRequires:	desktop-file-utils
BuildArch:		noarch
# The automatic dependency consists of python and rpmlib only. It is insufficient.
Requires:		pygtk2 vte rpm-python pygobject2

%description
Ailurus is a tool for backuping a name list of installed software.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=$RPM_BUILD_ROOT
desktop-file-install \
	--delete-original \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
	${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/ailurus
%{_datadir}/applications/ailurus.desktop
%{_datadir}/ailurus/
%{_datadir}/icons/hicolor/*/apps/ailurus.png
%{_mandir}/man1/ailurus.1*
%{python_sitelib}/ailurus/
%{python_sitelib}/ailurus*.egg-info

%changelog
* Tue Oct 12 2010 Liang Suilong <liangsuilong@gmail.com> 10.10.3-1
- Upstream to 10.10.3
