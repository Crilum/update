Name:           update
Version:        VERSION THE SCRIPT WILL UPDATE THIS!
Release:        1%{?dist}
BuildArch:      noarch
URL:            https://github.com/Crilum/%{name}
Summary:        Updates apps/packages/dependencies from Apt, Pi-Apps, Flatpak, the Snap Store, Homebrew, and NPM.

License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires: bash

%description
Updates apps/packages/dependencies from Apt, Pi-Apps, Flatpak, the Snap Store, Homebrew, and NPM.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

