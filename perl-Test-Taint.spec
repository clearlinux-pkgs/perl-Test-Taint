#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Taint
Version  : 1.06
Release  : 8
URL      : http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-Taint-1.06.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-Taint-1.06.tar.gz
Summary  : 'Checks for taintedness of variables'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Taint-doc

%description
No detailed description available

%package doc
Summary: doc components for the perl-Test-Taint package.
Group: Documentation

%description doc
doc components for the perl-Test-Taint package.


%prep
%setup -q -n Test-Taint-1.06

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/Test/Taint.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Test/Taint/Taint.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
