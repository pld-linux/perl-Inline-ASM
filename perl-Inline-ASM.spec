#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Inline
%define		pnam	ASM
Summary:	Inline::ASM Perl module
Summary(cs.UTF-8):	Modul Inline::ASM pro Perl
Summary(da.UTF-8):	Perlmodul Inline::ASM
Summary(de.UTF-8):	Inline::ASM Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::ASM
Summary(fr.UTF-8):	Module Perl Inline::ASM
Summary(it.UTF-8):	Modulo di Perl Inline::ASM
Summary(ja.UTF-8):	Inline::ASM Perl モジュール
Summary(ko.UTF-8):	Inline::ASM 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::ASM
Summary(pl.UTF-8):	Moduł Perla Inline::ASM
Summary(pt.UTF-8):	Módulo de Perl Inline::ASM
Summary(pt_BR.UTF-8):	Módulo Perl Inline::ASM
Summary(ru.UTF-8):	Модуль для Perl Inline::ASM
Summary(sv.UTF-8):	Inline::ASM Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::ASM
Summary(zh_CN.UTF-8):	Inline::ASM Perl 模块
Name:		perl-Inline-ASM
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af0241d8d9993598fc146eab4be247b2
URL:		http://search.cpan.org/dist/Inline-ASM/
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	binutils
Requires:	gcc
# module itself isn't arch-dependent (but asm syntax is)
# examples are for x86, but... they are only examples:)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::ASM - Write Perl Subroutines in assembler.

%description -l pl.UTF-8
Moduł Inline::ASM - pozwalający pisać funkcje Perla w asemblerze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
