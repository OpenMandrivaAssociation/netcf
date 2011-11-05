%define name netcf
%define libmajor 1
%define libname %mklibname %name %libmajor
%define libnamedevel %mklibname -d %name

Name: %name
Version: 0.1.9
Release: %mkrel 1
Group: Networking/Other
License: LGPLv2
Summary: A distribution agnostic library and tool for configuring network interfaces
URL: https://fedorahosted.org/netcf
Source: https://fedorahosted.org/released/netcf/netcf-%{version}.tar.gz
Source1: https://fedorahosted.org/released/netcf/netcf-%{version}.tar.gz.sig
BuildRequires: augeas-devel libxslt-devel libnl-devel readline-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
netcf is

    * a library for configuring network interfaces
    * a command line tool (ncftool) to do the same from the command line
    * distribution-agnostic and supports multiple distributions and operating
      systems (well, soon, anyway)
    * sets up Ethernet interfaces, bridges, and bonds 

Both libvirt and NetworkManager need this functionality - netcf implements what
is common to both of them.

%package -n %libname
Group: System/Libraries
Summary: A distribution agnostic library for configuring network interfaces

%description -n %libname
A distribution agnostic library for configuring network interfaces

Both libvirt and NetworkManager need this functionality - netcf implements what
is common to both of them.

%package -n %libnamedevel
Group: Development/C
Summary: Development files for a library for configuring network interfaces
Requires: %libname >= %version-%release
Provides: %name-devel = %{version}

%description -n %libnamedevel
Development files for a distribution agnostic library for configuring network 
interfaces.

%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.a %{buildroot}/%{_libdir}/*.la

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%doc README NEWS AUTHORS

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{libmajor}*

%files -n %libnamedevel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc
