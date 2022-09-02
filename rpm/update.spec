Name:           update
Version:        1.4.5
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
[[ $(ls -l $(command -v up)) =~ "/usr/bin/update" ]] || ln -v -s /usr/bin/update "/usr/bin/up"

%postun
[[ -L %{_bindir}/up ]] && rm -rf %{_bindir}/up
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

