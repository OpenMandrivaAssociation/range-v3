Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.3.7
Release: 1
License: Boost
URL: https://github.com/ericniebler/range-v3
Source0: https://github.com/ericniebler/range-v3/archive/%{version}.tar.gz
BuildArch: noarch
BuildRequires: cmake ninja

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files devel
%doc README.md CREDITS.md TODO.md
%{_includedir}/meta
%{_includedir}/range
%{_prefix}/lib/cmake/range-v3
