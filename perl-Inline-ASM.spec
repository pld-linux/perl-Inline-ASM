#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	ASM
Summary:	Inline::ASM Perl module
Summary(cs):	Modul Inline::ASM pro Perl
Summary(da):	Perlmodul Inline::ASM
Summary(de):	Inline::ASM Perl Modul
Summary(es):	Módulo de Perl Inline::ASM
Summary(fr):	Module Perl Inline::ASM
Summary(it):	Modulo di Perl Inline::ASM
Summary(ja):	Inline::ASM Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::ASM ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Inline::ASM
Summary(pl):	Modu³ Perla Inline::ASM
Summary(pt):	Módulo de Perl Inline::ASM
Summary(pt_BR):	Módulo Perl Inline::ASM
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::ASM
Summary(sv):	Inline::ASM Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::ASM
Summary(zh_CN):	Inline::ASM Perl Ä£¿é
Name:		perl-Inline-ASM
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	af0241d8d9993598fc146eab4be247b2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
%{perl_vendorlib}/Inline/ASM.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
