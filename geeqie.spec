%define docname %{name}

Summary:	Graphics file browser utility
Name:		geeqie
Version:	2.2
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		https://github.com/BestImageViewer/geeqie
Source0:	https://github.com/BestImageViewer/geeqie/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  intltool 
BuildRequires:	pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(lirc)
BuildRequires:	pkgconfig(clutter-1.0)
#BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(librsvg-2.0)
#BuildRequires:	pkgconfig(libwmf)
BuildRequires:	pkgconfig(poppler-glib)	
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	yelp-tools
BuildRequires:	meson
# Really xxd
BuildRequires:	vim

%description
Geeqie is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%autosetup -p1
sed -i -e 's,lua5.3,lua,g' meson.build
%meson \
	-Dheif=disabled

%build
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
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
%doc %{_docdir}/%{name}
