%define tarname	elementary-icons
%define name	elementary-icons
%define version	2.7.1
%define release %mkrel 4

Summary:	Elementary icons
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch

%description
Elementary icons theme.

%files
%defattr(-,root,root)
%{_iconsdir}/*

#--------------------------------------------------------------------

%prep
%setup -q

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
%__mkdir -p %{buildroot}%{_datadir}/icons/elementary
%__mkdir -p %{buildroot}%{_datadir}/icons/elementary-mono-dark
cp -rf elementary/* %{buildroot}%{_datadir}/icons/elementary
cp -rf elementary-mono-dark/* %{buildroot}%{_datadir}/icons/elementary-mono-dark
