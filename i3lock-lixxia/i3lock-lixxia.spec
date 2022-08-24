%global forgeurl https://github.com/Lixxia/i3lock
%global commit   be2a08a71ccbeecc961243fedf34595f20398837
%forgemeta

Name:		i3lock-lixxia
Version:	0
Release:	4%{?dist}
Summary:	Simple X display locker like slock

License:	MIT
URL:		%{forgeurl}
Source:		%{forgesource}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	pkg-config
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(xcb-xrm)
BuildRequires:	pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:	pkgconfig(xkbcommon-x11) >= 0.5.0
BuildRequires:	pkgconfig(cairo)
BuildRequires:	libev-devel
BuildRequires:	pam-devel

Provides:	i3lock = 2.12
Conflicts:	i3lock

%description
i3lock is a simple screen locker like slock. After starting it, you will see a
white screen (you can configure the color/an image). You can return to your
screen by entering your password.

This package contains Lixxia's fork, which has additional customization options
including a clock.

%prep
%forgesetup
sed -i '/^int input_position;/s/^/extern /' unlock_indicator.c

%build
autoreconf --force --install
%configure
%make_build

%install
%make_install INSTALL="install -p"
install -Dpm0644 i3lock.1 %{buildroot}%{_mandir}/man1/i3lock.1

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/i3lock
%{_sysconfdir}/pam.d/i3lock
%{_mandir}/man1/i3lock.1.gz

%changelog
* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 0-4.20210526gitbe2a08a
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 0-3.20210526gitbe2a08a
- Rebuild.

* Thu Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-2.20210526gitbe2a08a
- Rebuild.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-1.20210526gitbe2a08a
- Initial package.
