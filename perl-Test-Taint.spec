#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Taint
Version  : 1.06
Release  : 16
URL      : http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-Taint-1.06.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-Taint-1.06.tar.gz
Summary  : 'Checks for taintedness of variables'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Taint-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package dev
Summary: dev components for the perl-Test-Taint package.
Group: Development
Requires: perl-Test-Taint-lib = %{version}-%{release}
Provides: perl-Test-Taint-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-Taint package.


%package lib
Summary: lib components for the perl-Test-Taint package.
Group: Libraries

%description lib
lib components for the perl-Test-Taint package.


%prep
%setup -q -n Test-Taint-1.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/Test/Taint.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Taint.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/Test/Taint/Taint.so
