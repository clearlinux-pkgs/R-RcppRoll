#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcppRoll
Version  : 0.3.0
Release  : 45
URL      : https://cran.r-project.org/src/contrib/RcppRoll_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcppRoll_0.3.0.tar.gz
Summary  : Efficient Rolling / Windowed Operations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RcppRoll-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
common rolling / windowed operations. Routines for the
    efficient computation of windowed mean, median,
    sum, product, minimum, maximum, standard deviation
    and variance are provided.

%package lib
Summary: lib components for the R-RcppRoll package.
Group: Libraries

%description lib
lib components for the R-RcppRoll package.


%prep
%setup -q -c -n RcppRoll
cd %{_builddir}/RcppRoll

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641090707

%install
export SOURCE_DATE_EPOCH=1641090707
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppRoll
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppRoll
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppRoll
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RcppRoll || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppRoll/DESCRIPTION
/usr/lib64/R/library/RcppRoll/INDEX
/usr/lib64/R/library/RcppRoll/Meta/Rd.rds
/usr/lib64/R/library/RcppRoll/Meta/features.rds
/usr/lib64/R/library/RcppRoll/Meta/hsearch.rds
/usr/lib64/R/library/RcppRoll/Meta/links.rds
/usr/lib64/R/library/RcppRoll/Meta/nsInfo.rds
/usr/lib64/R/library/RcppRoll/Meta/package.rds
/usr/lib64/R/library/RcppRoll/NAMESPACE
/usr/lib64/R/library/RcppRoll/NEWS.md
/usr/lib64/R/library/RcppRoll/R/RcppRoll
/usr/lib64/R/library/RcppRoll/R/RcppRoll.rdb
/usr/lib64/R/library/RcppRoll/R/RcppRoll.rdx
/usr/lib64/R/library/RcppRoll/help/AnIndex
/usr/lib64/R/library/RcppRoll/help/RcppRoll.rdb
/usr/lib64/R/library/RcppRoll/help/RcppRoll.rdx
/usr/lib64/R/library/RcppRoll/help/aliases.rds
/usr/lib64/R/library/RcppRoll/help/paths.rds
/usr/lib64/R/library/RcppRoll/html/00Index.html
/usr/lib64/R/library/RcppRoll/html/R.css
/usr/lib64/R/library/RcppRoll/tests/testthat.R
/usr/lib64/R/library/RcppRoll/tests/testthat/test-weights.R
/usr/lib64/R/library/RcppRoll/tests/testthat/test-zoo.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppRoll/libs/RcppRoll.so
/usr/lib64/R/library/RcppRoll/libs/RcppRoll.so.avx2
/usr/lib64/R/library/RcppRoll/libs/RcppRoll.so.avx512
