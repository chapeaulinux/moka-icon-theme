# Spec file for package moka-icon-theme
#
# Copyright (c) 2016 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:		moka-icon-theme
Version:	5.3
Release:	3
Summary:	Moka Icon theme
Group:		System/GUI/Other
License:    CC-BY-SA-4.0
Group:      System/GUI/GNOME
Url:        https://snwh.org/moka
Source0:	%{name}-%{version}.tar.gz
Requires:	faba-icon-theme
BuildArch:	noarch

%description
Moka is simple and modern icon theme with material design influences, this particular package is a custom build for Chapeau Linux

%prep
%setup -q

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Moka/ $RPM_BUILD_ROOT%{_datadir}/icons/

%clean
# Delete dead icon symlinks
# find -L . -type l -delete

%files
#%doc AUTHORS COPYING
%{_datadir}/icons/Moka/

