#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-django_babel
Version  : 0.6.2
Release  : 42
URL      : https://files.pythonhosted.org/packages/87/e2/a009668c03148a62bc1d9cb6a30769de1eeab12e70824b609d5b405b5f6e/django-babel-0.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/87/e2/a009668c03148a62bc1d9cb6a30769de1eeab12e70824b609d5b405b5f6e/django-babel-0.6.2.tar.gz
Summary  : Utilities for using Babel in Django
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-django_babel-license = %{version}-%{release}
Requires: pypi-django_babel-python = %{version}-%{release}
Requires: pypi-django_babel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(babel)
BuildRequires : pypi(django)

%description
=================================
        
        This package contains various utilities for integration of `Babel`_ into the

%package license
Summary: license components for the pypi-django_babel package.
Group: Default

%description license
license components for the pypi-django_babel package.


%package python
Summary: python components for the pypi-django_babel package.
Group: Default
Requires: pypi-django_babel-python3 = %{version}-%{release}

%description python
python components for the pypi-django_babel package.


%package python3
Summary: python3 components for the pypi-django_babel package.
Group: Default
Requires: python3-core
Provides: pypi(django_babel)
Requires: pypi(babel)
Requires: pypi(django)

%description python3
python3 components for the pypi-django_babel package.


%prep
%setup -q -n django-babel-0.6.2
cd %{_builddir}/django-babel-0.6.2
pushd ..
cp -a django-babel-0.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671047169
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . django
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . django
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-django_babel
cp %{_builddir}/django-babel-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-django_babel/ef9326d4a7684b004c434fcae02325c57b86d2e8 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} django
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-django_babel/ef9326d4a7684b004c434fcae02325c57b86d2e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
