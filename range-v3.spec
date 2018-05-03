Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.3.5
Release: 2%{?dist}

License: Boost
URL: https://github.com/ericniebler/%{name}
Source0: %{url}/archive/%{version}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%{buildroot}%{_includedir}/%{name}"
cp -a include/* "%{buildroot}%{_includedir}/%{name}"

%files devel
%doc README.md CREDITS.md TODO.md
%{_includedir}/%{name}
