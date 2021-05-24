Summary:	Thin wrapper over POSIX syscalls
Name:		libfixposix
Version:	0.4.3
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/sionescu/libfixposix/releases
Source0:	https://github.com/sionescu/libfixposix/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5fbe45bd952977f3298957c6ac109cc4
URL:		https://github.com/sionescu/libfixposix/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake >= 1:1.10
BuildRequires:	libtool >= 2:2.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of libfixposix is to offer replacements for parts of POSIX
whose behaviour is inconsistent across *NIX flavours.

%package devel
Summary:	Header files for libfixposix library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libfixposix library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I config/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfixposix.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libfixposix.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfixposix.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfixposix.so
%{_includedir}/lfp.h
%dir %{_includedir}/lfp
%{_includedir}/lfp/*.h
%{_pkgconfigdir}/libfixposix.pc
