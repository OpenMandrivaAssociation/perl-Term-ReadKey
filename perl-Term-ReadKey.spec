Summary:	Term::ReadKey Perl module
Name:		perl-Term-ReadKey
Version:	2.30
Release:	20
License:	GPL
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/TermReadKey/
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
%setup -q -n TermReadKey-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*

%changelog
* Wed Dec 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.30-18
- rebuild for new perl-5.16.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30-15
+ Revision: 765671
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30-14
+ Revision: 764182
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30-13
+ Revision: 763100
- rebuild

* Thu Jan 19 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.30-12
+ Revision: 762827
- Build for perl 5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30-11
+ Revision: 667321
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.30-10mdv2011.0
+ Revision: 564583
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.30-9mdv2011.0
+ Revision: 555289
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.30-8mdv2010.1
+ Revision: 426592
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.30-7mdv2009.1
+ Revision: 351716
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.30-6mdv2009.0
+ Revision: 224096
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.30-5mdv2008.1
+ Revision: 151342
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 2.30-4mdv2008.0
+ Revision: 64808
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.30-3mdv2008.0
+ Revision: 23317
- rebuild


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.30-2mdk
- Rebuild

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 2.30-1mdk
- New release 2.30

* Mon Nov 15 2004 Austin Acton <austin@mandrake.org> 2.21-5mdk
- rebuild

* Thu Apr 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.21-4mdk
- rebuild for new perl

* Fri Aug 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.21-3mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.21-2mdk
- rebuild for new auto{prov,req}

* Fri Jan 17 2003 Austin Acton <aacton@yorku.ca> 2.21-1mdk
- initial package

