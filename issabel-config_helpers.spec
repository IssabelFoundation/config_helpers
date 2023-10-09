%define modname config_helpers

Summary: Issabel Configuration Helpers
Name:    issabel-config_helpers
Version: 5.0.0
Release: 1
License: GPL
Group:   Applications/System
Source0: issabel-%{modname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{modname}-%{version}-root
BuildArch: noarch
#%if 0%{?el7}
#Requires: mysql, mysql-server, dialog
#%else
Requires: mariadb, mariadb-server, dialog
#%endif
Requires: sed, grep, dialog
Requires: /bin/cp
Provides: elastix-config_helpers

%description
This module contains helper scripts for system configuration

%prep
%setup -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp issabel-change-language $RPM_BUILD_ROOT/usr/bin/
cp issabel-change-sip $RPM_BUILD_ROOT/usr/bin/

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/issabel-change-language
/usr/bin/issabel-change-sip

%changelog
