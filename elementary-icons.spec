Summary:	Elementary icons
Name:		elementary-icons
Version:	3.1
Release:	4
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://danrabbit.deviantart.com/art/elementary-Icons-65437279
Source0:	elementaryicons%{version}.tar.gz
Source1:	rosa-icons-replace-1.0.3.tar.gz
BuildArch:	noarch

%description
Elementary icons theme.

%prep
%setup -q -n elementaryicons%{version} -a 1

%install
mkdir -p %{buildroot}%{_iconsdir}/elementary
cp -rf * %{buildroot}%{_iconsdir}/elementary
#replace original icons from rosa-icons theme, because original rosa icons not property works
mv -f rosa-icons-replace-1.0.3/AUTHORS *.ROSA
cp -rf rosa-icons-replace-1.0.3/* %{buildroot}%{_iconsdir}/elementary
rm -rf %{buildroot}%{_iconsdir}/elementary/rosa-icons-replace-1.0.3

%files
%{_iconsdir}/*

