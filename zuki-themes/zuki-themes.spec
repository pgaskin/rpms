%define version_p1 3.38
%define version_p2 1

Name:		zuki-themes
Version:	%{version_p1}.%{version_p2}
Release:	3%{?dist}
Summary:	Zuki themes

License:	GPLv3
URL:		https://github.com/lassekongo83/%{name}
Source0:	%{url}/archive/v%{version_p1}-%{version_p2}.tar.gz

BuildArch:	noarch
BuildRequires:	meson
BuildRequires:	sassc

Requires:	filesystem
Requires:	gtk-murrine-engine
Requires:	gtk2-engines

%description
Zuki is a series of themes for GTK, gnome-shell and more.

%prep
%autosetup -n %{name}-%{version_p1}-%{version_p2} -p1

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
* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-3
- Rebuild.

* Thu Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-2
- Rebuild.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 3.38.1-1
- Initial package.
