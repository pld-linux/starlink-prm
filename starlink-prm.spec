Summary:	PRIMDAT - Processing of Primitive Numerical Data
Summary(pl.UTF-8):   PRIMDAT - przetwarzanie prostych danych numerycznych
Name:		starlink-prm
Version:	1.3_1.218
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/primdat/prm.tar.Z
# Source0-md5:	2745c7bc1ee10efcd3b656c0d4ad5cdb
Patch0:		%{name}-make.patch
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_PRIMDAT.html
BuildRequires:	gcc-g77
BuildRequires:	starlink-ems-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
PRIMDAT package is a collection of Fortran functions and subroutines
providing support for ``primitive data processing''. Routines from
this package may be used to perform arithmetic, mathematical
operations, type conversion and inter-comparison of any of the
primitive numerical data types supported by the Starlink Hierarchical
Data System (HDS).

%description -l pl.UTF-8
Pakiet PRIMDAT to zbiór funkcji fortranowych dających obsługę
przetwarzania prostych danych. Funkcje z tego pakietu mogą być używane
do wykonywania operacji arytmetycznych i matematycznych, konwersji
typów i porównywania dowolnych prostych typów danych numerycznych
obsługiwanych przez hierarchiczny system danych Starlink (HDS).

%package devel
Summary:	Header files for PRIMDAT library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki PRIMDAT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for PRIMDAT library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PRIMDAT.

%package static
Summary:	Static Starlink PRIMDAT library
Summary(pl.UTF-8):   Statyczna biblioteka Starlink PRIMDAT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink PRIMDAT library.

%description static -l pl.UTF-8
Statyczna biblioteka Starlink PRIMDAT.

%prep
%setup -q -c
%patch0 -p1

%build
OPT="%{rpmcflags}" \
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir} \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc prm.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/prm_dev
%attr(755,root,root) %{stardir}/bin/prm_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
