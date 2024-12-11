%define major 0
%define libname %mklibname jaylink
%define devname %mklibname jaylink -d

Name: libjaylink
Version: 0.4.0
Release: 1
Source0: https://gitlab.zapb.de/libjaylink/libjaylink/-/archive/%{version}/libjaylink-%{version}.tar.bz2
Summary: Library for accessing SEGGER J-Link and compatible devices
URL: https://githlab.zapb.de/libjaylink
License: GPL-2.0+
Group: System/Libraries
BuildRequires: autoconf
BuildRequires: make
BuildRequires: pkgconfig(libusb)
BuildRequires: doxygen
BuildRequires: slibtool

%description
libjaylink is a shared library written in C to access SEGGER J-Link and compatible devices.

%package -n %{libname}
Summary: Library for accessing SEGGER J-Link and compatible devices
Group: System/Libraries

%description -n %{libname}
libjaylink is a shared library written in C to access SEGGER J-Link and compatible devices.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

libjaylink is a shared library written in C to access SEGGER J-Link and compatible devices.

%prep
%autosetup -p1
./autogen.sh

%conf
%configure

%build
%make_build LIBTOOL=slibtool-shared

%install
%make_install LIBTOOL=slibtool-shared

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
