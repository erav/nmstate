%?python_enable_dependency_generator
%define srcname nmstate
%define libname libnmstate

Name:           nmstate
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Summary:        Declarative network manager API
License:        GPLv2+
URL:            https://github.com/%{srcname}/%{srcname}
Source0:        https://github.com/%{srcname}/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-%{libname} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Nmstate is a library with an accompanying command line tool that manages host
networking settings in a declarative manner and aimed to satisfy enterprise
needs to manage host networking through a northbound declarative API and multi
provider support on the southbound.


%package -n python3-%{libname}
Summary:        nmstate Python 3 API library
Requires:       python3-dbus
Requires:       NetworkManager-libnm >= 1:1.12
# Use Recommends for NetworkManager because only access to NM DBus is required,
# but NM could be running on a different host
Recommends:     NetworkManager
# Use Suggests for NetworkManager-ovs since it is only required for OVS support
Suggests:       NetworkManager-ovs


%description -n python3-%{libname}
This package contains the Python 3 library for Nmstate.

%prep
%setup -q
sed -i -e '/^dbus-python$/d' requirements.txt

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%doc examples/
%{python3_sitelib}/nmstatectl
%{_bindir}/nmstatectl

%files -n python3-%{libname}
%license LICENSE
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
@CHANGELOG@
- snapshot build
