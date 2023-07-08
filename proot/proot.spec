Name:		proot
Version:	5.3.1
Release:	4%{?dist}
Summary:	chroot, mount --bind, and binfmt_misc without privilege/setup for Linux

License:	GPLv2
URL:		https://github.com/proot-me/%{name}
Source:		%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	pkgconfig(talloc)
BuildRequires:	pkgconfig(libarchive)

%description
PRoot is a user-space implementation of chroot, mount --bind, and binfmt_misc.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build -C src loader.elf loader-m32.elf build.h PREFIX=%{_prefix}
%make_build -C src proot PREFIX=%{_prefix}

# TODO: figure out dependencies
#%check
#make -C test

%install
%make_install -C src PREFIX=%{_prefix}

%files
%doc doc/proot/manual.rst
%license COPYING
%{_bindir}/proot

%changelog
* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 5.3.1-4
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 5.3.1-3
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 5.3.1-2
- Fix build.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 5.3.1-1
- Update to 5.3.1.

* Sat Sep 11 2021 Patrick Gaskin <patrick@pgaskin.net> - 5.2.0-1
- Rebuild.

* Thu Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 5.2.0.alpha-2
- Rebuild.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 5.2.0.alpha-1
- Initial package.
