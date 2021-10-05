%global debug_package %{nil}
%define module ntfs3

Name:		%{module}-dkms
Version:	27
Release:	1%{?dist}
Summary:	NTFS read-write driver GPL implementation by Paragon Software

License:	GPLv2
URL:		https://www.paragon-software.com/home/ntfs3-driver-faq/
Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/rawdiff/?id=f7464060f7ab9a2424428008f0ee9f1e267e410f&id2=6abaa83c7352b31450d7e8c173f674324c16b02b#/ntfs3.patch
Source1:	https://aur.archlinux.org/cgit/aur.git/plain/kernel-5.12-backport.patch?h=ntfs3-dkms&id=57faff39920ed4815abcaa40349a19aa59e7ddf9#/kernel-5.12-backport.patch
Source2:	https://aur.archlinux.org/cgit/aur.git/plain/kernel-5.14-backport.patch?h=ntfs3-dkms&id=57faff39920ed4815abcaa40349a19aa59e7ddf9#/kernel-5.14-backport.patch
Source3:	https://aur.archlinux.org/cgit/aur.git/plain/kernel-5.15-backport.patch?h=ntfs3-dkms&id=57faff39920ed4815abcaa40349a19aa59e7ddf9#/kernel-5.15-backport.patch

BuildArch:	noarch

Provides:	kmod(%{module}.ko) = %{version}
Requires:	dkms >= 2.2.0.3
Requires:	kernel-devel

%description
This is fully functional NTFS Read-Write driver. Current version works with
NTFS(including v3.1) and normal/compressed/sparse files and supports journal
replaying.

%prep
%setup -c -T -n %{name}-%{version}

patch -p3 -t -N -i "%{SOURCE0}" || true

mkdir patches
cp "%{SOURCE1}" patches/kernel-5.12-backport.patch
cp "%{SOURCE2}" patches/kernel-5.14-backport.patch
cp "%{SOURCE3}" patches/kernel-5.15-backport.patch

cat << 'EOF' > dkms.conf
PACKAGE_NAME="%{module}"
PACKAGE_VERSION="%{version}"
BUILT_MODULE_NAME[0]="%{module}"
DEST_MODULE_LOCATION[0]="/kernel/fs/%{module}"
MAKE[0]="KVERSION=$kernelver CONFIG_NTFS3_FS=m CONFIG_NTFS3_LZX_XPRESS=y CONFIG_NTFS3_FS_POSIX_ACL=y make KDIR=$kernel_source_dir"
PATCH[0]="kernel-5.15-backport.patch"
PATCH_MATCH[0]="^([0-4]\.|5\.[0-9]\.|5\.1[0-4]\.).*"
PATCH[1]="kernel-5.14-backport.patch"
PATCH_MATCH[1]="^([0-4]\.|5\.[0-9]\.|5\.1[0-3]\.).*"
PATCH[2]="kernel-5.12-backport.patch"
PATCH_MATCH[2]="^([0-4]\.|5\.[0-9]\.|5\.1[0-1]\.).*"
EOF

cat << 'EOF' >> Makefile

ccflags-$(CONFIG_NTFS3_LZX_XPRESS) += -DCONFIG_NTFS3_LZX_XPRESS
ccflags-$(CONFIG_NTFS3_FS_POSIX_ACL) += -DCONFIG_NTFS3_FS_POSIX_ACL
all:
	make -C /lib/modules/$(KVERSION)/build M=$(PWD) modules
clean:
	make -C /lib/modules/$(KVERSION)/build M=$(PWD) clean
EOF

%build

%install
mkdir -p %{buildroot}%{_usrsrc}
cp -rf ${RPM_BUILD_DIR}/%{name}-%{version} ${RPM_BUILD_ROOT}/usr/src/%{module}-%{version}

%post
%{_prefix}/lib/dkms/common.postinst %{module} %{version} || exit $?
echo "%{name}-%{version}-%{release}" > %{_sharedstatedir}/dkms/%{module}/%{version}/version
exit 0

%preun
# if upgrading
if [ $1 -eq 1 ]; then
	# if it is a new ntfs3 version (rather than just a package version)
	if [ "$(dkms status %{module} | sed 's/,//g' | sort -r -V | awk '/installed/{print $2; exit}')" != "%{version}" ]; then
		# remove the old module
		true
	else
		# don't remove the old module (they will be removed on rebuild)
		exit 0
	fi
fi

# if the module is from the package, remove it
if [ -f %{_sharedstatedir}/dkms/%{module}/%{version}/version ]; then
	if [ "$(cat %{_sharedstatedir}/dkms/%{module}/%{version}/version)" = "%{name}-%{version}-%{release}" ]; then
		dkms remove -m %{module} -v %{version} -q --all --rpm_safe_upgrade || :
	fi
fi

exit 0

%files
%{_usrsrc}/%{module}-%{version}

%changelog
* Tue Oct 05 2021 Patrick Gaskin <patrick@pgaskin.net> - 27-1
- Update to final ntfs3 patches.
- Update backport patches from the AUR package for 5.14+ compatibility.

* Thu Jun 01 2021 Patrick Gaskin <patrick@pgaskin.net> - 26-2
- Rebuild.

* Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 26-1
- Initial package.
