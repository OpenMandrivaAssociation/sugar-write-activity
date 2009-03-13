# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-write-activity
Version: 63
Release: %mkrel 1
Summary: Word processor for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Write/Write-63.tar.bz2

Requires: abiword >= 2.6.8
Requires: python-abiword  
Requires: sugar-toolkit >= 0.84.0

BuildRequires: gettext  
BuildRequires: sugar-toolkit >= 0.84.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
The Write activity provides a word processor for the Sugar interface.

%prep
%setup -q -n Write-63


%build
python  \
	setup.py \
	build

%install
rm -rf %{buildroot}
[ -f setup.py ] && chmod 0755 setup.py
python  \
	setup.py \
	install \
	--prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.AbiWordActivity

%clean
rm -rf %{buildroot}

%files -f org.laptop.AbiWordActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc NEWS

