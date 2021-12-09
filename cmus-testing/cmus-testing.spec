%global forgeurl https://github.com/pgaskin/cmus
%global commit   b4a917ced80b3a2f8851e3b464fded40f264ec7a
%forgemeta

Name:		cmus-testing
Version:	2.9.1
Release:	9%{?dist}
Summary:	ncurses-based music player

License:	GPLv2+
URL:		%{forgeurl}
Source:		%{forgesource}

BuildRequires:	gcc
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio_cdda)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	libmpcdec-devel

Provides:	cmus = %{version}
Conflicts:	cmus

%description
cmus is a small, fast and powerful console music player for Unix-like operating
systems.

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
	CONFIG_AAC=n \
	CONFIG_ALSA=y \
	CONFIG_AO=y \
	CONFIG_ARTS=n \
	CONFIG_CDDB=y \
	CONFIG_CDIO=y \
	CONFIG_COREAUDIO=n \
	CONFIG_CUE=y \
	CONFIG_DISCID=y \
	CONFIG_FFMPEG=n \
	CONFIG_FLAC=y \
	CONFIG_JACK=y \
	CONFIG_MAD=y \
	CONFIG_MIKMOD=n \
	CONFIG_BASS=n \
	CONFIG_MODPLUG=y \
	CONFIG_MP4=n \
	CONFIG_MPC=y \
	CONFIG_MPRIS=y \
	CONFIG_OPUS=y \
	CONFIG_OSS=n \
	CONFIG_PULSE=y \
	CONFIG_ROAR=n \
	CONFIG_SAMPLERATE=y \
	CONFIG_SNDIO=n \
	CONFIG_SUN=n \
	CONFIG_TREMOR=n \
	CONFIG_VORBIS=y \
	CONFIG_VTX=n \
	CONFIG_WAVEOUT=n \
	CONFIG_WAVPACK=y \
	CONFIG_WAV=y \
	CFLAGS="${RPM_OPT_FLAGS}" \
	LDFLAGS="${RPM_LD_FLAGS}"
%make_build V=2

%install
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_datadir}/cmus/examples .
chmod -x examples/*

%files
%doc AUTHORS examples
%license COPYING
%{_bindir}/cmus
%{_bindir}/cmus-remote
%{_libdir}/cmus/
%{_datadir}/cmus/
%{_mandir}/man1/cmus-remote.1.gz
%{_mandir}/man1/cmus.1.gz
%{_mandir}/man7/cmus-tutorial.7.gz

%changelog
* Sat Dec 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-9.20211209gitb4a917c
- Update to upstream master.
- Merge pgaskin/pause-on-output-change.

* Sat Oct 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-8.20210608git462f7da
- Bump release version for rebuild.

* Tue Jun 08 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-7.20210608git462f7da
- Update pgaskin/remove-cache-with-track.

* Sat Jun 05 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-6.20210605gitefa21cc
- Update pgaskin/pl-env.

* Fri Jun 04 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-5.20210604git45c5a31
- Update to upstream master.
  - Includes pgaskin/fix-1093.
- Update pgaskin/pl-env.
- Merge pgaskin/fix-passwd-docs.
- Merge pgaskin/remove-cache-with-track.

* Thu Jun 03 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-4.20210603git71ebcd3
- Update to upstream master.
  - Includes nefthy/flac-channel-map-fix.
- Update pgaskin/pl-env.
- Merge pgaskin/fix-1093.

* Wed Jun 02 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-3.20210602gita3e6caa
- Update to latest commit.
  - Includes dryleev/fix-ffmpeg-freeze.
- Merge pgaskin/pl-env.

* Tue Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-2.20210601git48efe76
- Rebuild.

* Tue Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-1.20210601git48efe76
- Update to latest commit.
  - Update allavaz/smart-rg.
  - Update gavtroy/dev_album_shuffle.
  - Merge gavtroy/dev_wideterm.
  - Update to upstream master.
    - Includes allavaz/smart-rg.
    - Includes gavtroy/dev_format_nested.
    - Includes gavtroy/dev_wideterm.
    - Includes gavtroy/dev_album_shuffle.
  - Update gavtroy/dev_ignore_dups.
  - Merge dryleev/fix-ffmpeg-freeze.
  - Merge nefthy/flac-channel-map-fix.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-1.20210228git84db889
- Initial package.
