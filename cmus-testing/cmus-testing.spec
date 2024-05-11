%global forgeurl https://github.com/pgaskin/cmus
%global commit   f4e4fb6dd74cf60ee0bb6641a688457478abd968
%forgemeta

Name:		cmus-testing
Version:	2.11.0
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
* Sat May 11 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.11.0-1.20240511gitf4e4fb6
- Reset to upstream master.
- Merge gavtroy/flat-library-view.
- Merge gavtroy/cmdline-cursor-context.
- Merge gavtroy/gapless-mp4.
- Merge gavtroy/part-is-disc.
- Merge gavtroy/resume-pl.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-11.20240510git2658824
- Reset to upstream master.
- Merge gavtroy/flat-library-view.
- Merge gavtroy/cmdline-cursor-context.
- Merge gavtroy/gapless-mp4.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-10.20231105git2c5aafc
- Rebuild.

* Sun Nov 05 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-9.20231105git2c5aafc
- Reset to upstream master.
- Merge gavtroy/flat-library-view.

* Sat Jul 29 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-8.20230729git45a5045
- Reset to upstream master.
- Merge pgaskin/fix-passwd-docs.
- Merge pgaskin/bracketed-paste.
- Merge gavtroy/count-albumtracks.
- Merge gavtroy/sort-albums-by-date.
- Merge gavtroy/flat-library-view.
- Merge gavtroy/sorted-album-next.
- Merge gavtroy/fix-unmute-softvol.

* Sat Jul 22 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-7.20230722gitdef777c
- Reset to upstream master.
- Merge pgaskin/fix-passwd-docs.
- Merge pgaskin/bracketed-paste.
- Merge pgaskin/mouse-bar-right.
- Merge gavtroy/count-albumtracks.
- Merge gavtroy/sort-albums-by-date.
- Merge gavtroy/flat-library-view.

* Sat Jul 22 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-6.20230722gitd8a248a
- Reset to upstream master.
- Merge pgaskin/fix-passwd-docs.
- Merge pgaskin/bracketed-paste.
- Merge pgaskin/mouse-bar-right.
- Merge gavtroy/count-albumtracks.
- Merge gavtroy/cycle-view-no-wrap.
- Merge gavtroy/sort-albums-by-date.

* Sun Jul 16 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-5.20230716git001f1a4
- Update to upstream master.
  - Includes origin/pa-no-drain.
  - Includes VladislavGrudinin/clang-build-fix.
  - Includes rayes0/master (support italic text).
  - Includes feature detection for A_ITALIC (over rayes0/master).
- Merge pgaskin/bracketed-paste.
- Merge pgaskin/mouse-bar-right.

* Sat Jul 15 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-4.20230715git5f0e861
- Update to upstream master.
  - Includes pgaskin/pl-env.
- Merge origin/pa-no-drain.
- Merge VladislavGrudinin/clang-build-fix.
- Add feature detection for A_ITALIC (over rayes0/master).

* Thu Jul 13 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-3.20230713git10a8e31
- Update to upstream master.
  - Includes gavtroy/dev_ignore_dups.
- Update pgaskin/pl-env.

* Thu Jul 13 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-2.20230713gita52df51
- Reset to upstream master.
- Merge gavtroy/dev_ignore_dups.
- Merge pgaskin/fix-passwd-docs.
- Merge pgaskin/pl-env.
- Merge rayes0/master (support italic text).

* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 2.10.0-1.20230708git8330956
- Update to upstream master.
- Merge gavtroy/dont_search_in_filename.
- Merge gavtroy/auto_hide_playlist_panel.
- Merge gavtroy/ffmpeg_truncated.
- Merge gavtroy/mp4_trackid.
- Merge gavtroy/titleline_startup.

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
- Update pgaskin/pause-on-output-change.

* Thu Dec 09 2021 Patrick Gaskin <patrick@pgaskin.net> - 0-9.20211209gitb4a917c
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
