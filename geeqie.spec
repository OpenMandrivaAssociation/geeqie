%define docname %{name}

Summary:	Graphics file browser utility
Name:		geeqie
Version:	1.6
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		https://github.com/BestImageViewer/geeqie
Source0:	https://github.com/BestImageViewer/geeqie/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  intltool 
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(lirc)
BuildRequires:	pkgconfig(clutter-1.0)
#BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(librsvg-2.0)
#BuildRequires:	pkgconfig(libwmf)
BuildRequires:	pkgconfig(poppler-glib)	

%description
Geeqie is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%setup -q
autoreconf -fi

%build
%configure \
	--with-readmedir="%{_docdir}/%{docname}" \
	--enable-gps \
	--enable-lirc

%make_build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}/html
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README.md README.lirc 
%{_datadir}/doc/geeqie/ChangeLog.html
%{_datadir}/doc/geeqie/TODO
#{_datadir}/doc/geeqie/html/*
%{_bindir}/geeqie
%{_datadir}/applications/geeqie.desktop
%{_datadir}/pixmaps/geeqie.png
%{_datadir}/%{name}/applications/*
%{_datadir}/%{name}/template.desktop
%{_datadir}/metainfo/org.geeqie.Geeqie.appdata.xml
/usr/lib/geeqie/geeqie-*
/usr/lib/geeqie/geocode-parameters.awk
/usr/lib/geeqie/lensID
#{_libdir}/%{name}/*
%{_mandir}/man1/geeqie*
