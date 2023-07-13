%global forgeurl https://github.com/pgaskin/cmus
%global commit   10a8e31f8d0223b0b914427d78fdfc7c77154e38
%forgemeta

Name:		cmus-testing-plugins-rpmfusion
Version:	2.10.0
Release:	3%{?dist}
Summary:	Plugins for ncurses-based music player with RPMFusion dependencies.

License:	GPLv2+
URL:		%{forgeurl}
Source:		%{forgesource}

BuildRequires:	gcc
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	faad2-devel
BuildRequires:	libmp4v2-devel

Requires:	cmus-testing = 2.10.0
Supplements:	cmus-testing = 2.10.0

%description
This package contains plugins for cmus requiring nonfree or restricted packages
from RPMFusion, including the AAC, FFmpeg, and MP4 input plugins.

%prep
%forgesetup

%build
./configure \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	datadir=%{_datadir} \
	libdir=%{_libdir} \
	mandir=%{_mandir} \
	exampledir=%{_datadir}/cmus/examples \
	CONFIG_AAC=y \
	CONFIG_ALSA=n \
	CONFIG_AO=n \
	CONFIG_ARTS=n \
	CONFIG_CDDB=n \
	CONFIG_CDIO=n \
	CONFIG_COREAUDIO=n \
	CONFIG_CUE=n \
	CONFIG_DISCID=n \
	CONFIG_FFMPEG=y \
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
