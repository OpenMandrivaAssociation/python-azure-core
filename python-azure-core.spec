%define module azure-core
%define oname  azure_core

Name:		python-azure-core
Version:	1.38.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Microsoft Azure Core Library for Python
URL:		https://pypi.org/project/azure-core/
License:	MIT License
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Microsoft Azure Core Library for Python

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%{py_sitedir}/azure
%{py_sitedir}/%{oname}-%{version}.dist-info
