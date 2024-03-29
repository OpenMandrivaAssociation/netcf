%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	A distribution agnostic library and tool for configuring network interfaces
Name:		netcf
Version:	0.2.8
Release:	2
Group:		Networking/Other
License:	LGPLv2
Url:		https://pagure.io/netcf
Source0:	https://fedorahosted.org/released/netcf/netcf-%{version}.tar.gz

BuildRequires:	readline-devel
BuildRequires:	pkgconfig(augeas)
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(gpg-error)

%description
netcf is

    * a library for configuring network interfaces
    * a command line tool (ncftool) to do the same from the command line
    * distribution-agnostic and supports multiple distributions and operating
      systems (well, soon, anyway)
    * sets up Ethernet interfaces, bridges, and bonds 

Both libvirt and NetworkManager need this functionality - netcf implements what
is common to both of them.

%package -n %{libname}
Group:		System/Libraries
Summary:	A distribution agnostic library for configuring network interfaces

%description -n %{libname}
A distribution agnostic library for configuring network interfaces

Both libvirt and NetworkManager need this functionality - netcf implements what
is common to both of them.

%package -n %{devname}
Group:		Development/C
Summary:	Development files for a library for configuring network interfaces
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for a distribution agnostic library for configuring network 
interfaces.

%prep
%setup -q
autoreconf -fi
#see https://bugzilla.redhat.com/show_bug.cgi?id=852549
#in future we should switch off with-libnl1 and use libnl3

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%doc README NEWS AUTHORS
%{_bindir}/*
%{_datadir}/%{name}
/usr/lib/systemd/system/netcf-transaction.service
%{_libexecdir}/netcf-transaction.sh
%{_mandir}/man1/ncftool.1.*

%files -n %{libname}
%{_libdir}/libnetcf.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc

