%global forgeurl https://github.com/sagb/alttab
%global commit   f4d1b5b5876fbf1542598f7422685ca5b980264f
%forgemeta

Name:		alttab
Version:	1.7.1
Release:	3%{?dist}
Summary:	Task Switcher

License:	GPL-3.0-only
URL:		%{forgeurl}
Source:		%{forgesource}

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
%forgesetup

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
* Sun May 03 2026 Patrick Gaskin <patrick@pgaskin.net> - 1.7.1-3.20260421gitf4d1b5b
- Update to latest commit.

* Sun May 03 2026 Patrick Gaskin <patrick@pgaskin.net> - 1.7.1-2
- Rebuild.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 1.7.1-1
- Update to 1.7.1.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 1.6.1-5
- Rebuild.

* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 1.6.1-4
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 1.6.1-3
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 1.6.1-2
- Rebuild.

* Thu Dec 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 1.6.1-1
- Update to 1.6.1.

* Thu Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 1.6.0-2
- Rebuild.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 1.6.0-1
- Initial package.
