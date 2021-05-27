Name:		alttab
Version:	1.6.0
Release:	1%{?dist}
Summary:	Task Switcher
License:	GPL-3.0-only
URL:		https://github.com/sagb/alttab
Source:		%{url}/archive/v%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:  pkgconfig(libpng)
BuildRequires:	pkgconfig(xpm)
BuildRequires:  uthash-devel
BuildRequires:  rubygem-ronn-ng

%description
alttab is a X11 window switcher designed for minimalistic window managers or standalone X11 session.

%prep
%autosetup

%build
./bootstrap.sh
%configure
%make_build

%install
%make_install

%files
%doc %{_datadir}/doc/alttab/
%doc ChangeLog
%license COPYING
%{_bindir}/alttab
%{_mandir}/man1/alttab.1.gz

%changelog
