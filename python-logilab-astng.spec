
%define	module	astng
Summary:	Python Abstract Syntax Tree New Generation
Summary(pl):	Abstrakcyjne drzewa sk³adniowe Pythona nowej generacji
Name:		python-logilab-astng
Version:	0.13.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/astng/%{module}-%{version}.tar.gz
# Source0-md5:	57b899fb6caf7b88f33161b89ee1e6fa
URL:		http://www.logilab.org/projects/astng
BuildRequires:	python-devel
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.112
%pyrequires_eq	python-modules
Requires:	python-logilab-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of this module is to provide a common base representation of
Python source code for projects such as pychecker, pyreverse,
pylint... Well, actually the development of this library is essentialy
governed by pylint's needs.

%description -l pl
Celem tego modu³u jest dostarczenie wspólnej bazowej reprezentacji
kodu ¼ród³owego Pythona dla projektów takich jak pychecker, pyreverse,
pylint... W³a¶ciwie tworzenie tej biblioteki jest istotnie kierowane
potrzebami pylinta.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

# see install section of python-logilab-common for explanation
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/__init__.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitescriptdir}/logilab/astng
