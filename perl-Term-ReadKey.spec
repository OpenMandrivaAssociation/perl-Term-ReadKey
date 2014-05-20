Summary:	Term::ReadKey Perl module

Name:		perl-Term-ReadKey
Version:	%perl_convert_version 2.32
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/TermReadKey/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/TermReadKey-2.32.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils

%description
This module, ReadKey, provides ioctl control for terminals so the
input modes can be changed (thus allowing reads of a single character
at a time), and also provides non-blocking reads of stdin, as well as
several other terminal related features, including
retrieval/modification of the screen size, and retrieval/modification
of the control characters.

%prep
%setup -qn TermReadKey-2.32

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*



