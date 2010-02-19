%define name    geeqie
%define version 1.0
%define release %mkrel 1

%define docname %{name}

Name:    %{name}
Version: %{version}
Release: %{release}

BuildRequires:  lcms-devel
BuildRequires:  libexiv-devel
BuildRequires:  intltool 
BuildRequires:  gtk2-devel
BuildRequires:  libchamplain-devel
BuildRequires:  lirc-devel
BuildRequires:  gnome-doc-utils


Summary:        Graphics file browser utility
License:        GPLv2+
Group:          Graphics
Source:         %{name}-%{version}.tar.gz
Patch0:         geeqie_lib64.diff
#patch fixes the libdir for x86_64
URL:            http://sourceforge.net/projects/geeqie/
BuildRoot:      {_tmppath}/%{name}-%{version}-build

%description
Geeqie is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%setup -q
%patch0 -p0


%build
autoreconf
%configure2_5x --with-readmedir="%{_docdir}/%{docname}" --enable-gps --enable-lirc


%make

%install
%__rm -rf "%{buildroot}"
%makeinstall_std

%find_lang %{name}

%clean
%__rm -rf "%{buildroot}"

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README README.lirc 
%{_bindir}/geeqie
%{_datadir}/applications/geeqie.desktop
%{_datadir}/pixmaps/geeqie.png
%{_datadir}/%{name}/applications/*
%{_datadir}/%{name}/template.desktop
%{_libdir}/%{name}/*
%{_mandir}/man1/geeqie*


%changelog

