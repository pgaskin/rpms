%global forgeurl https://github.com/pgaskin/cmus
%global commit   e328d34e28d379997d4bd56b2f63b67f1a993d16
%forgemeta

Name:		cmus-testing-plugins-rpmfusion
Version:	2.12.0
Release:	1%{?dist}
Summary:	Plugins for ncurses-based music player with RPMFusion dependencies.

License:	GPLv2+
URL:		%{forgeurl}
Source:		%{forgesource}

BuildRequires:	gcc
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	faad2-devel
BuildRequires:	libmp4v2-devel

Requires:	cmus-testing = 2.12.0
Supplements:	cmus-testing = 2.12.0

%description
This package contains plugins for cmus requiring nonfree or restricted packages
from RPMFusion, including the AAC and MP4 input plugins.

%prep
%forgesetup

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--docdir=%{_datadir}/cmus \
	CONFIG_AAC=y \
	CONFIG_AAUDIO=n \
	CONFIG_ALSA=n \
	CONFIG_AO=n \
	CONFIG_ARTS=n \
	CONFIG_CDDB=n \
	CONFIG_CDIO=n \
	CONFIG_COREAUDIO=n \
	CONFIG_CUE=n \
	CONFIG_DISCID=n \
	CONFIG_FFMPEG=n \
	CONFIG_FLAC=n \
	CONFIG_JACK=n \
	CONFIG_MAD=n \
	CONFIG_MIKMOD=n \
	CONFIG_BASS=n \
	CONFIG_MODPLUG=n \
	CONFIG_MP4=y \
	CONFIG_MPC=n \
	CONFIG_MPRIS=n \
	CONFIG_OPUS=n \
	CONFIG_OSS=n \
	CONFIG_PULSE=n \
	CONFIG_ROAR=n \
	CONFIG_SAMPLERATE=n \
	CONFIG_SNDIO=n \
	CONFIG_SUN=n \
	CONFIG_TREMOR=n \
	CONFIG_VORBIS=n \
	CONFIG_VTX=n \
	CONFIG_WAVEOUT=n \
	CONFIG_WAVPACK=n \
	CONFIG_WAV=n \
	CFLAGS="${RPM_OPT_FLAGS}" \
	LDFLAGS="${RPM_LD_FLAGS}"
%make_build plugins V=2

%install
make install-plugins DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS
%license COPYING
%{_libdir}/cmus/{ip,op}/*

%changelog
* Sat Oct 26 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.12.0-1.20240923gite328d34
- Update for latest cmus-testing release.

* Mon Sep 23 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-8.20240923git2d11ce1
- Update for latest cmus-testing release.

* Mon Sep 23 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-7.20240923gitb942bec
- Update for latest cmus-testing release.

* Sun Sep 22 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-6.20240922git58caca8
- Update for latest cmus-testing release.
- Build ffmpeg plugin as part of free package (rpmfusion ffmpeg is a drop-in replacement).

* Fri Sep 20 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-5.20240920git257b2bf
- Update for latest cmus-testing release.

* Sat Sep 14 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-4.20240914gitbbfb75f
- Update for latest cmus-testing release.

* Tue Aug 06 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-3.20240806git91ad600
- Update for latest cmus-testing release.

* Sat May 11 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-2.20240511gitf4e4fb6
- Rebuild.

* Sat May 11 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-1.20240511gitf4e4fb6
- Update for latest cmus-testing release.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-11.20240510git2658824
- Update for latest cmus-testing release.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-10.20231105git2c5aafc
- Rebuild.

* Sun Nov 05 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-9.20231105git2c5aafc
- Update for latest cmus-testing release.

* Sat Jul 29 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-8.20230729git45a5045
- Update for latest cmus-testing release.

* Sat Jul 22 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-7.20230722gitdef777c
- Update for latest cmus-testing release.

* Sat Jul 22 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-6.20230722gitd8a248a
- Update for latest cmus-testing release.

* Sun Jul 16 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-5.20230716git001f1a4
- Update for latest cmus-testing release.

* Sat Jul 15 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-4.20230715git5f0e861
- Update for latest cmus-testing release.

* Thu Jul 13 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-3.20230713git10a8e31
- Update for latest cmus-testing release.

* Thu Jul 13 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-2.20230713gita52df51
- Update for latest cmus-testing release.

* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-1.20230708git8330956
- Update for latest cmus-testing release.

* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.9.1-15.20211209gite4b5908
- Rebuild.

* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.9.1-14.20211209gite4b5908
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 2.9.1-13.20211209gite4b5908
- Fix versioning.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 0-12.20211209gite4b5908
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 0-11.20211209gite4b5908
- Rebuild.

* Thu Dec 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-10.20211209gite4b5908
- Update for latest cmus-testing release.

* Thu Dec 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-9.20211209gitb4a917c
- Update for latest cmus-testing release.

* Sat Oct 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-8.20210608git462f7da
- Bump release version for rebuild.

* Tue Jun 08 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-7.20210608git462f7da
- Update for latest cmus-testing release.

* Sat Jun 05 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-6.20210605gitefa21cc
- Update for latest cmus-testing release.

* Fri Jun 04 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-5.20210604git45c5a31
- Update for latest cmus-testing release.

* Thu Jun 03 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-4.20210603git71ebcd3
- Update for latest cmus-testing release.

* Wed Jun 02 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-3.20210602gita3e6caa
- Update for latest cmus-testing release.

* Tue Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-2.20210601git48efe76
- Rebuild.

* Tue Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-1.20210601git48efe76
- Initial package.
