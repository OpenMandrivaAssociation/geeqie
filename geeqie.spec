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
BuildRequires:  pkgconfig(lcms2)
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
%configure \
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
