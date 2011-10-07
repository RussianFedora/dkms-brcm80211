%define module_name brcm80211
%define _srcdir %{_prefix}/src

Name:		dkms-%{module_name}
Version:  	3.1.0
Release:	1%{?dist}.R
Summary:	Kernel module for broadcom wireless devices

Group:		System Environment/Kernel
License:	GPLv2
URL:		http://linuxwireless.org/en/users/Drivers/brcm80211
Source0:	%{module_name}.tar.bz2
Source1:	dkms.conf.brcm80211
Source2:	%{module_name}-blacklist.conf
Patch1:		%{module_name}-includes.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	dkms kernel-devel gcc
BuildArch:	noarch

%description
Kernel module source for backlight support some of samsung laptops

%prep
%setup -q -n %{module_name}
%patch1 -p1 -b .includes-patch

#build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_srcdir}
mkdir -p $RPM_BUILD_ROOT%{_srcdir}/%{module_name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/
cp -r %{_builddir}/%{module_name}/* $RPM_BUILD_ROOT%{_srcdir}/%{module_name}-%{version}/
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_srcdir}/%{module_name}-%{version}/dkms.conf
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{module_name}-dkms-blacklist.conf


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_srcdir}/%{module_name}-%{version}/*
%{_sysconfdir}/modprobe.d/*
%doc README

%post
/usr/sbin/dkms add -m %{module_name} -v %{version}

%preun
/usr/sbin/dkms remove -m %{module_name} -v %{version} --all

%changelog
* Thu Oct  6 2011 Alexei Panov <me AT elemc DOT name> - 3.1.0-1
- Initial build



