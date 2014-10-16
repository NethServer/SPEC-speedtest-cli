Name: speedtest-cli
Version: 0.3.1
Release: 1%{?dist}
Summary: Command line interface for testing internet bandwidth

License: ASL 2.0 
URL: https://github.com/sivel/speedtest-cli
Source0: https://github.com/sivel/%{name}/archive/v%{version}.tar.gz

BuildRequires: python2-devel
BuildRequires: python-setuptools
Requires: python
Requires: python-setuptools
BuildArch: noarch

%description
Command line interface for testing internet bandwidth using speedtest.net

%prep
%setup -q
sed -i -e '/^#!\//, 1d' *.py

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
gzip speedtest-cli.1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 speedtest-cli.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/speedtest-cli.1.gz
rm -f $RPM_BUILD_ROOT%{_bindir}/speedtest

%check
%{__python2} setup.py test

%files
%{_bindir}/speedtest-cli
%{python2_sitelib}/speedtest_cli.py*
%{python2_sitelib}/speedtest_cli-%{version}-py2.7.egg-info
%{_mandir}/man1/speedtest-cli.1.gz
%doc CONTRIBUTING.md  LICENSE  README.rst 

%changelog
* Wed Oct 15 2014 Matias Kreder <delete@fedoraproject.org> 0.3.1-1
- Updated to 0.3.1, added python-setuptools as a dependency

* Mon Jul 14 2014 Matias Kreder <delete@fedoraproject.org> 0.3.0-1
- Initial spec

