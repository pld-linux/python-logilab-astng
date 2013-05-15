%define	module	logilab-astng
Summary:	Python Abstract Syntax Tree New Generation
Summary(pl.UTF-8):	Abstrakcyjne drzewa składniowe Pythona nowej generacji
Name:		python-logilab-astng
Version:	0.24.3
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.logilab.org/pub/astng/%{module}-%{version}.tar.gz
# Source0-md5:	11d9a33a00790dc30b851afbeaf1fb4e
URL:		http://www.logilab.org/projects/astng
BuildRequires:	python-devel
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-logilab-common >= 0.53.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of this module is to provide a common base representation of
Python source code for projects such as pychecker, pyreverse,
pylint... Well, actually the development of this library is essentialy
governed by pylint's needs.

%description -l pl.UTF-8
Celem tego modułu jest dostarczenie wspólnej bazowej reprezentacji
kodu źródłowego Pythona dla projektów takich jak pychecker, pyreverse,
pylint... Właściwie tworzenie tej biblioteki jest istotnie kierowane
potrzebami pylinta.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitescriptdir}/logilab/astng
%{py_sitescriptdir}/logilab_astng-%{version}-py*.egg-info
%{py_sitescriptdir}/logilab_astng-%{version}-py*-nspkg.pth
