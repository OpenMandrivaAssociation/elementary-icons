%define tarname	elementary-icons
%define name	elementary-icons
%define version	2.7.1
%define release %mkrel 4

Summary:	Elementary icons
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
Source1:	rosa-icons-replace-1.0.3.tar.gz
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
%setup -q -a 1

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
%__mkdir -p %{buildroot}%{_datadir}/icons/elementary
%__mkdir -p %{buildroot}%{_datadir}/icons/elementary-mono-dark
cp -rf elementary/* %{buildroot}%{_datadir}/icons/elementary
cp -rf elementary-mono-dark/* %{buildroot}%{_datadir}/icons/elementary-mono-dark
#replace original icons from rosa-icons theme, because original rosa icons not property works
cp -rf rosa-icons-replace-1.0.3/* %{buildroot}%{_datadir}/icons/elementary


%changelog
* Wed Jul 20 2011 Александр Казанцев <kazancas@mandriva.org> 2.7.1-4mdv2011.0
+ Revision: 690688
- sync ROSA icons and fix AUTORS

* Sun Jul 03 2011 Александр Казанцев <kazancas@mandriva.org> 2.7.1-3
+ Revision: 688617
- fix and add trash icons in status place

* Thu Jun 30 2011 Александр Казанцев <kazancas@mandriva.org> 2.7.1-2
+ Revision: 688409
- add pretty icons from ROSA Lab

* Thu Jun 30 2011 Александр Казанцев <kazancas@mandriva.org> 2.7.1-1
+ Revision: 688364
- update to 2.7.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file

* Mon Apr 11 2011 Alex Burmashev <burmashev@mandriva.org> 2.4.1-2
+ Revision: 652630
- import elementary-icons

