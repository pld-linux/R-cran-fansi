%define		fversion	%(echo %{version} |tr r -)
%define		modulename	fansi
Summary:	ANSI control sequence aware string functions
Name:		R-cran-%{modulename}
Version:	1.0.7
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	0914da4f7908ade99adfa06371df71b9
URL:		https://cran.r-project.org/package=%{modulename}
BuildRequires:	R

Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANSI control sequence aware string functions.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
