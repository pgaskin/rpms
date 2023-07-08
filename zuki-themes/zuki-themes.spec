Name:		zuki-themes
Version:	4.0
Release:	2%{?dist}
Summary:	Zuki themes

License:	GPLv3
URL:		https://github.com/lassekongo83/%{name}
Source0:	%{url}/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	meson
BuildRequires:	sassc

Requires:	filesystem
Requires:	gtk-murrine-engine
Requires:	gtk2-engines

%description
Zuki is a series of themes for GTK, gnome-shell and more.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/Zuki{-shell,tre,tre-dark,two,two-dark}

%changelog
* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 4.0-2
- Rebuild.

* Thu Jan 26 2023 Patrick Gaskin <patrick@pgaskin.net> - 4.0-1
- Update to 4.0.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-4
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-3
- Rebuild.

* Thu Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-2
- Rebuild.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-1
- Initial package.
