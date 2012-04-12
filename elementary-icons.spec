%define tarname	elementary-icons
%define name	elementary-icons
%define version	2.7.1
%define release %mkrel 4

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
%{__mkdir} -p %{buildroot}%{_iconsdir}/elementary
%{__mkdir} -p %{buildroot}%{_iconsdir}/elementary-mono-dark
cp -rf elementary/* %{buildroot}%{_iconsdir}/elementary
cp -rf elementary-mono-dark/* %{buildroot}%{_iconsdir}/elementary-mono-dark

%files
%defattr(-,root,root)
%{_iconsdir}/*
