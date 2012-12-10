%define docname %{name}

Summary:	Graphics file browser utility
Name:		geeqie
Version:	1.1
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		http://sourceforge.net/projects/geeqie/
Source0:	%{name}-%{version}.tar.gz
# sent upstream 2010/02/19 
# http://sourceforge.net/tracker/?func=detail&aid=2954914&group_id=222125&atid=1054680
Patch0:         geeqie_lib64.diff
Patch1:		geeqie-1.0-champlain0.8.patch

BuildRequires:  intltool 
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lcms)
BuildRequires:  pkgconfig(liblircclient0)

%description
Geeqie is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
autoreconf -fi

%build
%configure2_5x \
	--with-readmedir="%{_docdir}/%{docname}" \
	--enable-gps \
	--enable-lirc

%make

%install
mkdir -p %{buildroot}%{_docdir}/%{name}/html
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README README.lirc 
%{_bindir}/geeqie
%{_datadir}/applications/geeqie.desktop
%{_datadir}/pixmaps/geeqie.png
%{_datadir}/%{name}/applications/*
%{_datadir}/%{name}/template.desktop
%{_libdir}/%{name}/*
%{_mandir}/man1/geeqie*



%changelog
* Wed Sep 05 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1-1
+ Revision: 816396
- update to 1.1

* Fri May 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.0-6
+ Revision: 800724
- rebuild for new libchamplain
- cleaned up spec

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.0-4mdv2011.0
+ Revision: 604403
- rebuild for new exiv2

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 1.0-3mdv2011.0
+ Revision: 574695
- build with new libchamplain

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1.0-2mdv2011.0
+ Revision: 565538
- rebuild for new exiv2

* Fri Feb 19 2010 Michael Scherer <misc@mandriva.org> 1.0-1mdv2010.1
+ Revision: 508122
- readd BuildRoot, as youri ask for it even if not used and deprecated

  + Peťoš Šafařík <petos@mandriva.org>
    - Spec cleaning
    - Cleaning of SPEC
    - Fixed mix of <tabs> and <spaces> in SPEC
    - Removed old source tarball
    - Final stable version 1.0

* Thu Jan 28 2010 Peťoš Šafařík <petos@mandriva.org> 1.0-0.svn1895.3mdv2010.1
+ Revision: 497619
- BuildRequires fixed
- 64bit patch adds
- Libdir patched with lib64.diff patch
- Update to SVN branch.

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0-0.beta2.2mdv2010.1
+ Revision: 484195
- Rebuild for new libexiv2

* Mon Dec 28 2009 Götz Waschk <waschk@mandriva.org> 1.0-0.beta2.1mdv2010.1
+ Revision: 482955
- fix summary

  + Peťoš Šafařík <petos@mandriva.org>
    - import geeqie


* Thu Dec 24 2009 Petr 'Petos'Safarik <petos@mandrivalinux.cz> 1.0beta2-1pts2010.0
- Version 1.0beta2 first release