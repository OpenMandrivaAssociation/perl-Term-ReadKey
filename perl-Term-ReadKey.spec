%undefine _debugsource_packages

Summary:	Term::ReadKey Perl module
Name:		perl-Term-ReadKey
Version:	2.38
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/Term::ReadKey
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils
Obsoletes:	%{name} = 2.380.0

%description
This module, ReadKey, provides ioctl control for terminals so the
input modes can be changed (thus allowing reads of a single character
at a time), and also provides non-blocking reads of stdin, as well as
several other terminal related features, including
retrieval/modification of the screen size, and retrieval/modification
of the control characters.

%prep
%autosetup -p1 -n TermReadKey-%{version}
perl Makefile.PL INSTALLDIRS=vendor </dev/null

%build
%make_build

%install
%make_install

%files
%doc README
%{perl_vendorarch}/*
%{_mandir}/man3/*
