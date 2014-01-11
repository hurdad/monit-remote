Name:		monit-remote
Version:	
Release:	1%{?dist}
Summary:	monit remote configuration python web app
Group:		Applications/Internet
License:	BSD
URL:		http://github.com/hurdad/monit-remote
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
Requires:	python-webpy
Requires:	python-paramiko

%description
monit remote configuration python web app

%prep
%setup -q

%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}

%changelog
* Wed Jan 10 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
