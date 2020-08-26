Summary:         Native ZFS for Linux
Group:           Utilities/System
Name:            zfs
Version:         0.8.1
Release:         2
License:         CDDL
URL:             http://zfsonlinux.org/
Source:          http://archive.zfsonlinux.org/downloads/zfsonlinux/zfs/%{name}-%{version}.tar.gz
BuildRequires:   zlib-devel
BuildRequires:   e2fsprogs-devel
BuildRequires:   util-linux-devel
BuildRequires:   libblkid-devel
BuildRequires:   libattr-devel
BuildRequires:   libtirpc-devel
BuildRequires:   libselinux-devel
BuildRequires:   libgudev-devel
BuildRequires:   openssl-devel

BuildRequires:   ca-certificates 

Requires     :   autoconf  
Requires     :   automake 
Requires     :   rpm-build
Requires     :   ksh 
Requires     :   libacl-devel 
Requires     :   libaio-devel
Requires     :   device-mapper-devel 
Requires     :   openssl-devel
Requires     :   libtirpc-devel  
Requires     :   elfutils-libelf-devel 


#Requires:   zlib-devel
#Requires:   e2fsprogs-devel
#Requires:   util-linux-devel
#Requires:   libblkid-devel
#Requires:   libattr-devel
#Requires:   libtirpc-devel
#Requires:   libselinux-devel
#Requires:   libgudev-devel
#Requires:   openssl-devel
%description
ZFS is an advanced file system and volume manager which was originally
developed for Solaris and is now maintained by the Illumos community.

ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.

Requires:        %{name}
Requires:        zlib e2fsprogs
BuildRequires:   zlib-devel e2fsprogs-devel
Requires:        %{name}
Requires:        parted lsscsi
Requires:        ksh
Requires:        %{name}
Requires:        dracut


%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
#%configure --with-config=user
./configure --build=arm-linux
make -s -j$(nproc)

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/default/zfs
/sbin/mount.zfs
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/system/*
%{_prefix}/lib/systemd/system-generators/zfs-mount-generator
%{_prefix}/local/share/zfs/*
%{_prefix}/local/share/initramfs-tools/*
%{_prefix}/local/share/man/man1/*
%{_prefix}/local/share/man/man5/*
%{_prefix}/local/share/man/man8/*
%{_prefix}/local/src/*
%{_prefix}/local/share/pkgconfig/*
%{_prefix}/local/sbin/*
%{_prefix}/local/lib/*
%{_prefix}/local/include/*
%{_prefix}/local/bin/*
%{_prefix}/lib/modules-load.d/zfs.conf
%{_prefix}/lib/dracut/modules.d/02zfsexpandknowledge/module-setup.sh
%{_prefix}/local/etc/sudoers.d/zfs
%{_prefix}/local/etc/init.d/*
%{_prefix}/local/etc/zfs/*
%{_prefix}/local/libexec/zfs/*
%{_prefix}/lib/dracut/modules.d/90zfs/*
/lib/udev/rules.d/*
/lib/udev/*_id
/lib/modules/4.19.90-2003.4.0.0036.oe1.aarch64/extra/

#%doc AUTHORS COPYRIGHT LICENSE *.md
%post
[ -x /sbin/chkconfig ] && /sbin/chkconfig --add zfs
exit 0

%preun
[ "$1" = 0 ] && [ -x /sbin/chkconfig ] && /sbin/chkconfig --del zfs
exit 0

%changelog
* Tue Oct 08 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuild for Fedora
