%define name	perl-Term-ReadKey
%define version 2.30
%define release %mkrel 11

Summary:	Term::ReadKey Perl module
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/TermReadKey/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This module, ReadKey, provides ioctl control for terminals so the
input modes can be changed (thus allowing reads of a single character
at a time), and also provides non-blocking reads of stdin, as well as
several other terminal related features, including
retrieval/modification of the screen size, and retrieval/modification
of the control characters.

%prep
%setup -q -n TermReadKey-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*

