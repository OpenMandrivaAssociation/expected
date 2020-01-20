Name: expected
Version: 1.0.0
Release: 1%{?dist}

License: CC0
Summary: C++11/14/17 std::expected with functional-style extensions
URL: https://github.com/TartanLlama/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# Backported upstream patch with cmake fixes.
Patch100: %{name}-cmake.patch

BuildRequires: ninja
BuildRequires: cmake

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Header-only %{summary}.

std::expected is proposed as the preferred way to represent objec
which will either have an expected value, or an unexpected value
giving information about why something failed. Unfortunately,
chaining together many computations which may fail can be verbose,
as error-checking code will be mixed in with the actual programming
logic. This implementation provides a number of utilities to make
coding with expected cleaner.

%prep
%autosetup -p1
mkdir -p %{_target_platform}

%build
%cmake -G Ninja \
-DCMAKE_BUILD_TYPE=Release \
-DEXPECTED_BUILD_TESTS=OFF \
-DEXPECTED_BUILD_PACKAGE=OFF \

%ninja_build

%install
%ninja_install -C build

%files devel
%doc README.md
%license COPYING
%{_includedir}/tl
%{_datadir}/cmake/tl-%{name}
