%define Werror_cflags %nil
%global debug_package %{nil}

Name: range-v3
Summary: Experimental range library for C++11/14/17
# do not update it
# util you check that telegram-desktop still buildable
Version: 0.12.0
Release: 1
License: Boost
URL: https://github.com/ericniebler/range-v3
Source0: https://github.com/ericniebler/range-v3/archive/%{version}.tar.gz
BuildRequires: cmake ninja
# Add "forgotten"(?) header to all.hpp - without this, telegram fails
# to compile
Patch1: range-v3-0.9.1-fix-all.hpp.patch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%set_build_flags
%cmake -DRANGES_CXX_COMPILER_CLANGCL=ON -DRANGE_V3_TESTS=OFF -G Ninja
%ninja_build

%install
%ninja_install -C build

%files devel
%doc README.md CREDITS.md TODO.md
%{_includedir}/concepts
%{_includedir}/meta
%{_includedir}/range
%{_includedir}/std
%{_includedir}/module.modulemap
%{_libdir}/cmake/range-v3
