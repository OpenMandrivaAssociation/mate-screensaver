%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Screensaver
Name:		mate-screensaver
Version:	1.8.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(libmatekbdui)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(libsystemd-login)
BuildRequires:	pkgconfig(xscrnsaver)
Requires:	dbus-x11
Suggests:	mandriva-theme-screensaver

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
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--enable-locking \
	--enable-pam \
	--with-shadow \
	--with-systemd \
	--disable-more-warnings

%make

%install
%makeinstall_std

# remove unneeded converter
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS
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
%{_datadir}/applications/screensavers/gnomelogo-floaters.desktop
%{_datadir}/applications/screensavers/personal-slideshow.desktop
%{_datadir}/applications/screensavers/popsquares.desktop
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/cosmos
%{_datadir}/backgrounds/cosmos/*
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/mate-screensaver/*
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/pixmaps/gnome-logo-white.svg
%{_mandir}/man1/mate-screensaver*

%files devel        
%{_libdir}/pkgconfig/mate-screensaver.pc

