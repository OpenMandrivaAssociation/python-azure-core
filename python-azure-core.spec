Name:		python-azure-core
Version:	1.37.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/azure-core/azure_core-%{version}.tar.gz
Summary:	Microsoft Azure Core Library for Python
URL:		https://pypi.org/project/azure-core/
License:	MIT License
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Microsoft Azure Core Library for Python

%prep
%autosetup -p1 -n azure_core-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/azure
%{py_sitedir}/azure_core-*.*-info
