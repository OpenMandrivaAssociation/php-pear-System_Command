%define		_class		System
%define		_subclass	Command
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.8
Release:	2
Summary:	Commandline execution interface
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/System_Command/
Source0:	http://download.pear.php.net/package/System_Command-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Running functions from the commandline can be dangerous if the proper
precautions are not taken to escape the shell arguments and reaping
the exit status properly. This class give a formal interface to both,
so that you can run a system command as comfortably as you would run a
PHP function, which full pear error handling as results on failure.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3mdv2012.0
+ Revision: 742281
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2
+ Revision: 679585
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 594502
- update to new version 1.0.7

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-5mdv2010.1
+ Revision: 467091
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.6-4mdv2010.0
+ Revision: 441621
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-3mdv2009.1
+ Revision: 322666
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2009.0
+ Revision: 237071
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.0.6-1mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 28 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-1mdv2008.0
+ Revision: 18936
- 1.0.6


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdv2007.0
+ Revision: 82699
- Import php-pear-System_Command

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdk
- 1.0.5

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdk
- 1.0.4
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- 1.0.2

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package (PLD import)


