%define		module  Rabbyt
Summary:	Library for Python to game development
Summary(pl.UTF-8):	Biblioteka dla Pythona do rozwoju gier
Name:		python-%{module}
Version:	0.0.5
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/R/Rabbyt/%{module}-%{version}.tar.gz
# Source0-md5:	320be0f9e88eb28d439f2d0ac9012f7a
URL:		http://matthewmarshall.org/projects/rabbyt/
BuildRequires:	ncurses-devel
BuildRequires:	python-devel
BuildRequires:	python-Pyrex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rabbyt is a sprite library for Python with game development in mind.
It has two goals: 
1. Be fast, without sacrificing ease of use. 
2. Be easy to use, without sacrificing speed.

%description -l pl.UTF-8
Rabbyt jest małą biblioteką dla Pythona służącą do rozwoju
gier. Posiada dwa cele: 
1. Być szybką bez utraty prostoty użycia.
2. Być prostą w użyciu bez utraty szybkości.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples
%{py_sitescriptdir}/*
