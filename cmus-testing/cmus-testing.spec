%global forgeurl https://github.com/pgaskin/cmus
%global commit   84db889e7bba0984a417afc8f40de7322011e5f2
%forgemeta

Name:		cmus-testing
Version:	2.9.1
Release:	1%{?dist}
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
Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-1.20210228git84db889
- Initial package.
