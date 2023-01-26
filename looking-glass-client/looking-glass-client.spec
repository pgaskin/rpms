Name:    looking-glass-client
Version: 0~B6
Release: 1%{?dist}
Summary: Low latency KVMFR implementation for guests with VGA PCI Passthrough (client)

License: GPLv2
Source0: https://github.com/gnif/LookingGlass/archive/refs/tags/B6.tar.gz
Source1: https://github.com/gnif/LGMP/archive/1b170ad8d732c8649d75f2ab71c11731661b0b96.tar.gz
Source2: https://github.com/gnif/PureSpice/archive/247c57ee36110bc1d99e42355338a25ff2e483b0.tar.gz
Source3: https://github.com/cimgui/cimgui/archive/261250f88f374e751b2de1501ba5c0c11e420b5a.tar.gz
Source4: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/930bc8014b43653204d411add2009c0d86e4a945/wayland-protocols-930bc8014b43653204d411add2009c0d86e4a945.tar.gz
Source5: https://github.com/memononen/nanosvg/archive/64d59e4d53308104181c6a7ad71fbf423f71910f.tar.gz
Source6: https://github.com/ocornut/imgui/archive/c71a50deb5ddf1ea386b91e60fa2e4a26d080074.tar.gz
Source7: %{name}-sysusers.conf
Source8: %{name}-tmpfiles.conf

BuildRequires: systemd-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: coreutils
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libdecor-0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xpresent)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: gawk
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(samplerate)
BuildRequires: binutils-devel
BuildRequires: pkgconfig(spice-protocol)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(hogweed)

# LookingGlass/client/audiodevs/PipeWire:     pkgconfig(libpipewire-0.3)
# LookingGlass/client/audiodevs/PulseAudio:   pkgconfig(libpulse)
# LookingGlass/client/displayservers/Wayland: pkgconfig(wayland-client) pkgconfig(wayland-cursor) pkgconfig(xkbcommon) ENABLE_LIBDECOR:pkgconfig(libdecor-0)
# LookingGlass/client/displayservers/X11:     pkgconfig(x11) pkgconfig(xi) pkgconfig(xfixes) pkgconfig(xscrnsaver) pkgconfig(xinerama) pkgconfig(xcursor) pkgconfig(xpresent) pkgconfig(xkbcommon)
# LookingGlass/client/renderers/EGL:          pkgconfig(egl) pkgconfig(gl) OPTIONAL:pkgconfig(wayland-egl) gawk
# LookingGlass/client/renderers/OpenGL:       pkgconfig(gl)
# LookingGlass/client:                        pkgconfig(fontconfig) ENABLE_PIPEWIRE|ENABLE_PULSEAUDIO:pkgconfig(samplerate)
# LookingGlass/common/src/platform/linux:     ENABLE_BACKTRACE:binutils-devel
# PureSpice:                                  pkgconfig(spice-protocol) pkgconfig(nettle) pkgconfig(hogweed)
# missing from previous deps:                 pkgconfig(xrandr)

Requires: dejavu-sans-mono-fonts

%description
Looking Glass is an open source application that allows the use of a KVM
(Kernel-based Virtual Machine) configured for VGA PCI Pass-through without an
attached physical monitor, keyboard or mouse. This is the final step required
to move away from dual booting with other operating systems for legacy
programs that require high performance graphics.

%prep
cd "%{_builddir}"
rm -rf LookingGlass-B6
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE0}" || exit $?
cd LookingGlass-B6 || exit $?
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .

rm -rf repos
mkdir repos
cd repos || exit $?
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE1}" || exit $?
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE2}" || exit $?
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE3}" || exit $?
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE4}" || exit $?
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE5}" || exit $?
/usr/lib/rpm/rpmuncompress -x -v "%{SOURCE6}" || exit $?
mv LGMP-* LGMP || exit $?
mv PureSpice-* PureSpice || exit $?
mv cimgui-* cimgui || exit $?
mv wayland-protocols-* wayland-protocols || exit $?
mv nanosvg-* nanosvg || exit $?
rmdir cimgui/imgui && mv imgui-* cimgui/imgui || exit $?
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .

%build
cd "%{_builddir}/LookingGlass-B6/client"
%cmake -DENABLE_OPENGL=ON -DENABLE_EGL=ON -DENABLE_BACKTRACE=ON -DENABLEX11=ON -DENABLE_WAYLAND=ON -DENABLE_LIBDECOR=ON -DENABLE_PIPEWIRE=ON -DENABLE_PULSEAUDIO=ON
%cmake_build

%install
cd "%{_builddir}/LookingGlass-B6/client"
%cmake_install
install -Dm644 %{SOURCE7} %{buildroot}%{_sysusersdir}/%{name}.conf
install -Dm644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%pre
%sysusers_create_compat ${SOURCE7}

%post
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf &>/dev/null || :
usermod -aG looking-glass qemu 2>/dev/null || :

%files
%{_bindir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf

%changelog
* Thu Jan 26 2023 Patrick Gaskin <patrick@pgaskin.net> - B6.0.0-1
- Initial package.
