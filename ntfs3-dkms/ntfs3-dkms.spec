%global debug_package %{nil}
%define module ntfs3

Name:		%{module}-dkms
Version:	26
Release:	1%{?dist}
URL:		https://www.paragon-software.com/home/ntfs3-driver-faq/
Summary:	NTFS read-write driver GPL implementation by Paragon Software
License:	GPLv2
BuildArch:	noarch

Source0:        https://lore.kernel.org/lkml/20210402155347.64594-2-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~1.patch
Source1:        https://lore.kernel.org/lkml/20210402155347.64594-3-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~2.patch
Source2:        https://lore.kernel.org/lkml/20210402155347.64594-4-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~3.patch
Source3:        https://lore.kernel.org/lkml/20210402155347.64594-5-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~4.patch
Source4:        https://lore.kernel.org/lkml/20210402155347.64594-6-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~5.patch
Source5:        https://lore.kernel.org/lkml/20210402155347.64594-7-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~6.patch
Source6:        https://lore.kernel.org/lkml/20210402155347.64594-8-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~7.patch
Source7:        https://lore.kernel.org/lkml/20210402155347.64594-9-almaz.alexandrovich@paragon-software.com/raw#/%{name}-%{version}~8.patch
Source8:	https://aur.archlinux.org/cgit/aur.git/plain/legacy_kernel.patch?h=ntfs3-dkms&id=de7decc2f54bcaa8e31c653c72d7f459563f34ec#/legacy_kernel.patch

Provides:       kmod(%{module}.ko) = %{version}
Requires:       dkms >= 2.2.0.3
Requires:       kernel-devel

%description
This is fully functional NTFS Read-Write driver. Current version works with
NTFS(including v3.1) and normal/compressed/sparse files and supports journal
replaying.

%prep
%setup -c -T -n %{name}-%{version}

for patch in "%{SOURCE0}" "%{SOURCE1}" "%{SOURCE2}" "%{SOURCE3}" "%{SOURCE4}" "%{SOURCE5}" "%{SOURCE6}" "%{SOURCE7}"; do
	patch -p3 -N -i "${patch}"
done

mkdir patches
cp "%{SOURCE8}" patches/legacy_kernel.patch

cat << 'EOF' > dkms.conf
PACKAGE_NAME="%{module}"
PACKAGE_VERSION="%{version}"
BUILT_MODULE_NAME[0]="%{module}"
DEST_MODULE_LOCATION[0]="/kernel/fs/%{module}"
AUTOINSTALL="yes"
MAKE[0]="KVERSION=$kernelver CONFIG_NTFS3_FS=m CONFIG_NTFS3_LZX_XPRESS=y CONFIG_NTFS3_FS_POSIX_ACL=y make KDIR=$kernel_source_dir"
PATCH[0]="legacy_kernel.patch"
PATCH_MATCH[0]="^([0-4]\.|5\.[0-9]\.|5\.1[0-1]\.).*"
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
Thu May 27 2021 Patrick Gaskin <patrick@pgaskin.net> - 26-1
- Initial package.
