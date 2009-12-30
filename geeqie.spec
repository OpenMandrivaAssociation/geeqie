%define name    geeqie
%define version 1.0
%define prerelease beta2
%define release %mkrel 0.%{prerelease}.2

Name:    %{name}
Version: %{version}
Release: %{release}

BuildRequires:  lcms-devel
%define docname %{name}
BuildRequires:  libexiv-devel
BuildRequires:  intltool 
BuildRequires:	gtk2-devel

Summary:        Graphics file browser utility
License:        GPLv2+
Group:          Graphics
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}%{prerelease}/geeqie-%{version}%{prerelease}.tar.gz
Patch0:		geeqie_64.patch
URL:		http://sourceforge.net/projects/geeqie/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Geeqie is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%setup -q -n %{name}-%{version}%{prerelease}

%ifarch x86_64
%patch0 -p0
autoconf
%endif

%build

%configure2_5x --with-readmedir="%{_docdir}/%{docname}"


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


