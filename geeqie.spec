%define name    geeqie
%define version 1.0
# define prerelease beta2
%define svnrel	   1895
# define release %mkrel 0.%{prerelease}.2
%define release %mkrel 0.svn%{svnrel}.1

Name:    %{name}
Version: %{version}
Release: %{release}

BuildRequires:  lcms-devel
%define docname %{name}
BuildRequires:  libexiv-devel
BuildRequires:  intltool 
BuildRequires:	gtk2-devel
BuildRequires:	libchamplain-devel
BuildRequires:	lirc-devel
Requires:	libchamplain0.4_0

Summary:        Graphics file browser utility
License:        GPLv2+
Group:          Graphics
Source:         %{name}.tar.gz
# Patch0:		geeqie_64.patch
URL:		http://sourceforge.net/projects/geeqie/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Geeqie is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%setup -q -n %{name}

./autogen.sh

%build

%configure2_5x --with-readmedir="%{_docdir}/%{docname}" --enable-gps --enable-lirc


%make

%install
%__rm -rf "%{buildroot}"
%makeinstall_std

%__install -m 644 AUTHORS COPYING ChangeLog NEWS README README.lirc "%{buildroot}/%{_docdir}/%{docname}/"

%find_lang %{name}

%clean
%__rm -rf "%{buildroot}"

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_docdir}/%{docname}
%{_bindir}/geeqie
%{_datadir}/applications/geeqie.desktop
%{_datadir}/pixmaps/geeqie.png
%{_datadir}/%{name}/applications/*
%{_datadir}/%{name}/template.desktop
%{_libdir}/%{name}/*
%{_mandir}/man1/geeqie*


%changelog
* Sun Jul 19 2009 Petr 'Petos'Safarik <petos@mandrivalinux.cz> 1.0beta2-1pts2009.1
- Version 1.0beta2 first release
 
* Thu May 12 2009 Petos <petos@physics.muni.cz> 1.0alpha2-2pts2009.1
- Rebuild for 2009 Spring
 
* Mon Apr 20 2009 Petos <petos@physics.muni.cz> 1.0alpha2-2pts2009.0
- New version 1.0alpha2 or release 2pts2009.0
 
* Mon Dec 02 2008 Petos <petos@physics.muni.cz> 1.0alpha2-1pts2009.0
- New version 1.0alpha2 or release 1pts2009.0
