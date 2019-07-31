%define docname %{name}

Summary:	Graphics file browser utility
Name:		geeqie
Version:	1.5
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
