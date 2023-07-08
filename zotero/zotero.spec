%define debug_package %{nil}
%define __requires_exclude ^(libclearkey|libfreeblpriv3|liblgpllibs|libmozavcodec|libmozavutil|libmozgtk|libmozsandbox|libmozsqlite3|libnspr4|libnss3|libnssckbi|libnssdbm3|libnssutil3|libplc4|libsmime3|libsoftokn3|libssl3|libxul)\.so
%global __provides_exclude_from %{_libdir}/%{name}

Name:		zotero
Version:	6.0.13
Release:	3%{?dist}
Summary:	Zotero desktop application

License:	AGPLv3
URL:		https://www.zotero.org
Source0:	https://download.zotero.org/client/release/%{version}/Zotero-%{version}_linux-x86_64.tar.bz2
Source1:	zotero.desktop

BuildArch:	x86_64

%description
Zotero is a free, easy-to-use tool to help you collect, organize, cite, and share research.

%prep
%autosetup -n Zotero_linux-x86_64

%build

%install
mkdir -p %{buildroot}{%{_bindir},%{_libdir}/%{name}}
cp -rf %{_builddir}/Zotero_linux-x86_64/* %{buildroot}%{_libdir}/%{name}/
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -Dm644 %{buildroot}%{_libdir}/%{name}/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -Dm644 %{buildroot}%{_libdir}/%{name}/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm644 %{buildroot}%{_libdir}/%{name}/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dm644 %{buildroot}%{_libdir}/%{name}/chrome/icons/default/default256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%doc
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/zotero.png

%changelog
* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-3
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-2
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-1
- Update to 6.0.13.

* Sat Sep 11 2021 Patrick Gaskin <patrick@pgaskin.net> - 5.0.96.3-1
- Initial package.
