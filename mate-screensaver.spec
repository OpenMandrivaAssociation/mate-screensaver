Summary:	MATE Screensaver
Name:		mate-screensaver
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(libmatekbdui)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xxf86misc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xtst)

Requires: xsltproc
Requires: dbus-x11
Suggests: mandriva-theme-screensaver

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.
It is designed to support:

* the ability to lock down configuration settings
* translation into other languages
* user switching

%package devel
Summary:	Pkgconfig file for %{name}
Group:		Development/Other

%description devel
This package contains the pkgconfig file for %{name}.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-more-warnings

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS
%{_sysconfdir}/mateconf/schemas/mate-screensaver.schemas
%{_sysconfdir}/pam.d/mate-screensaver
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_bindir}/*
%{_libexecdir}/mate-screensaver-gl-helper
%{_libexecdir}/mate-screensaver/floaters
%{_libexecdir}/mate-screensaver/popsquares
%{_libexecdir}/mate-screensaver/slideshow
%{_libexecdir}/mate-screensaver-dialog
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/cosmos-slideshow.desktop
%{_datadir}/applications/screensavers/footlogo-floaters.desktop
%{_datadir}/applications/screensavers/personal-slideshow.desktop
%{_datadir}/applications/screensavers/popsquares.desktop
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/cosmos
%{_datadir}/backgrounds/cosmos/*
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/mate-screensaver/*
%{_datadir}/pixmaps/mate-logo-white.svg
%{_mandir}/man1/mate-screensaver*

%files devel        
%{_libdir}/pkgconfig/mate-screensaver.pc


%changelog
* Tue Jun 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802775
- imported package mate-screensaver

