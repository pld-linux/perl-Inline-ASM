%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	ASM
Summary:	Inline::ASM perl module
Summary(pl):	Modu³ perla Inline::ASM
Name:		perl-Inline-ASM
Version:	0.03
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	binutils
Requires:	gcc
# module itself isn't arch-dependent (but asm syntax is)
# examples are for x86, but... they are only examples :)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::ASM - Write Perl Subroutines in assembler.

%description -l pl
Modu³ Inline::ASM - pozwalaj±cy pisaæ funkcje Perla w asemblerze.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf examples/{5005.pl,as,gasp} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Inline/ASM.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
