%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Screensaver
Name:		mate-screensaver
Version:	1.20.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(libmatekbdui)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	xmlto

Requires:	dbus-x11

Suggests:	mandriva-theme-screensaver

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

MATE Screensaver is a screen saver and locker that aims to have simple,
sane, secure defaults and be well integrated with the desktop. It is
designed to support:

  * the ability to lock down configuration settings
  * translation into many languages
  * user switching

%files -f %{name}.lang
%doc COPYING AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/pam.d/mate-screensaver
%config(noreplace) %{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/*
%{_libexecdir}/mate-screensaver-dialog
%{_libexecdir}/mate-screensaver-gl-helper
%{_libexecdir}/mate-screensaver/floaters
%{_libexecdir}/mate-screensaver/popsquares
%{_libexecdir}/mate-screensaver/slideshow
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

#---------------------------------------------------------------------------

%package devel
Summary:	Pkgconfig file for %{name}
Group:		Development/Other

%description devel
This package contains the pkgconfig file for %{name}.

%files devel
%{_libdir}/pkgconfig/mate-screensaver.pc

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-more-warnings \
	--disable-schemas-compile \
	--enable-docbook-docs \
	%{nil}
%make

%install
%makeinstall_std

# fix doc path
mv -f %{buildroot}%{_docdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-screensaver-preferences.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/screensavers/cosmos-slideshow.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/screensavers/footlogo-floaters.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/screensavers/gnomelogo-floaters.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/screensavers/personal-slideshow.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/screensavers/popsquares.desktop

