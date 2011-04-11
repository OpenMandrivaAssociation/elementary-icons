%define tarname	elementary-icons
%define name	elementary-icons
%define version	2.4.1
%define release %mkrel 2

Summary:	Elementary icons
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Elementary icons theme.

%prep
%setup -q

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
%__mkdir -p %{buildroot}%{_datadir}/icons/elementary
%__mkdir -p %{buildroot}%{_datadir}/icons/elementary-mono-dark
cp -rf elementary/* %{buildroot}%{_datadir}/icons/elementary
cp -rf elementary-mono-dark/* %{buildroot}%{_datadir}/icons/elementary-mono-dark

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/icons/*

