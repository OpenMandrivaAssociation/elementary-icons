%define tarname	elementary-icons
%define name	elementary-icons
%define version	2.7.1
%define release %mkrel 5

Summary:	Elementary icons
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		https://launchpad.net/elementaryicons/
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch

%description
Icons theme set from Elementary project.

%prep
%setup -q

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_iconsdir}
cp -a elementary %{buildroot}%{_iconsdir}/
cp -a elementary-mono-dark %{buildroot}%{_iconsdir}/

%files
%defattr(-,root,root)
%{_iconsdir}/*
