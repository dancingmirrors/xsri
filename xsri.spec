# Note that this is NOT a relocatable package
Summary:   X Set Root Image
Name:      xsri
Version:   2.1.0
Release:   1
Epoch:     1
License:   GPL
Group:     System Environment/Base
Source0:   %{name}-%{PACKAGE_VERSION}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: gtk2-devel >= 1.3.13
BuildPrereq: popt

%description
X Set Root Image - displays images on the root window with 
parameters. Does nothing much more.

%prep
%setup

%build
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%{_bindir}/*

%changelog
* Mon Feb 11 2002 Owen Taylor <otaylor@redhat.com>
- Version 2.1.0

* Wed Aug 15 2001 Owen Taylor <otaylor@redhat.com>
- Version 2.0.3

* Fri Aug 03 2001 Owen Taylor <otaylor@redhat.com>
- Version 2.0.2

* Sun Jul 08 2001 Owen Taylor <otaylor@redhat.com>
- Version 2.0.1

* Sun Jul 08 2001 Owen Taylor <otaylor@redhat.com>
- Epoch is 1

* Sun Jul 08 2001 Owen Taylor <otaylor@redhat.com>
- Version 2.0.0

* Sun Jul  8 2001 Owen Taylor <otaylor@redhat.com>
- Completely new version

* Tue Apr 6 1999 The Rasterman <raster@redhat.com>
- made rpm
