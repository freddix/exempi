Summary:	Implementation of XMP
Name:		exempi
Version:	2.2.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	4657deb13b77c2a0e30e144857d2ff7a
BuildRequires:	autoconf
BuildRequires:	automake
# some tests
BuildRequires:	boost-devel
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Adobe XMP.

%package devel
Summary:	Header files for exempi library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for exempi library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-static=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/exempi
%attr(755,root,root) %ghost %{_libdir}/libexempi.so.3
%attr(755,root,root) %{_libdir}/libexempi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexempi.so
%{_libdir}/libexempi.la
%{_includedir}/exempi-2.0
%{_pkgconfigdir}/*.pc

