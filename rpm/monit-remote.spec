Name:   	monit-remote
Version:	%{VERSION}
Release:	%{RELEASE}1%{?dist}
Summary:	monit remote configuration python web app
Group:  	Applications/Internet
License:	BSD
URL:		http://github.com/hurdad/monit-remote
Source0:    monit-remote-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	python-webpy
Requires:	python-paramiko
Requires:	daemonize

%description
monit remote configuration python web app

%prep
%setup -q

#sysconfig default port 3809
echo -e "PORT=3809" > monit-remote.sysconfig

%install
%{__rm} -rf %{buildroot}

#build folders
%{__mkdir} -p %{buildroot}%{_datadir}/monit-remote
%{__mkdir} -p %{buildroot}%{_initddir}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
%{__mkdir} -p %{buildroot}%{_sysconfdir}/logrotate.d
%{__mkdir} -p %{buildroot}%{_sysconfdir}/monit.d
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/monit-remote

#app
%{__cp} -av controllers %{buildroot}%{_datadir}/monit-remote
%{__cp} -av db %{buildroot}%{_datadir}/monit-remote
%{__cp} -av lib %{buildroot}%{_datadir}/monit-remote
%{__cp} -av models %{buildroot}%{_datadir}/monit-remote
%{__cp} -av static %{buildroot}%{_datadir}/monit-remote
%{__cp} -av templates %{buildroot}%{_datadir}/monit-remote
%{__install} -m 755 app.py %{buildroot}%{_datadir}/monit-remote

#scripts
%{__install} -m 755 %{_topdir}/init.d/monit-remote %{buildroot}%{_initddir}
%{__install} -m 644 %{_topdir}/logrotate.d/monit-remote %{buildroot}%{_sysconfdir}/logrotate.d/
%{__install} -m 644 %{_topdir}/monit.d/monit-remote %{buildroot}%{_sysconfdir}/monit.d/
%{__install} -m 644 monit-remote.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/monit-remote

%clean
%{__rm} -rf %{buildroot}

%preun
/etc/init.d/monit-remote stop

%files
%defattr(-,root,root,-)
%{_datadir}
%{_sysconfdir}
%{_localstatedir}
%{_localstatedir}

%changelog
* Wed Jan 10 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
