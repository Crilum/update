Name:           update
Version:        VERSION THE SCRIPT WILL UPDATE THIS!
Release:        1%{?dist}
BuildArch:      noarch
URL:            https://github.com/Crilum/%{name}
Summary:        Updates apps/packages/dependencies from Apt, Pi-Apps, Flatpak, the Snap Store, Homebrew, and NPM.

License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires: bash
Requires: curl
Requires: wget

%description
Updates apps/packages/dependencies from Apt, Pi-Apps, Flatpak, the Snap Store, Homebrew, and NPM.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}

%post
[[ -L %{_bindir}/up ]] && rm -rf %{_bindir}/up
ln -v -s %{_bindir}/update %{_bindir}/up

%postun
[[ -L %{_bindir}/up ]] && rm -rf %{_bindir}/up

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

