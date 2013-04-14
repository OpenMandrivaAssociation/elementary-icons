Summary:	Elementary icons
Name:		elementary-icons
Version:	2.7.1
Release:	6
License:	GPLv2
Group:		Graphical desktop/Other
Source0:	%{name}-%{version}.tar.gz
Source1:	rosa-icons-replace-1.0.3.tar.gz
BuildArch:	noarch

%description
Elementary icons theme.

%prep
%setup -q -a 1

%install
mkdir -p %{buildroot}%{_iconsdir}/elementary{,-mono-dark}
cp -rf elementary/* %{buildroot}%{_iconsdir}/elementary
cp -rf elementary-mono-dark/* %{buildroot}%{_iconsdir}/elementary-mono-dark
#replace original icons from rosa-icons theme, because original rosa icons not property works
cp -rf rosa-icons-replace-1.0.3/* %{buildroot}%{_iconsdir}/elementary

%files
%{_iconsdir}/*

