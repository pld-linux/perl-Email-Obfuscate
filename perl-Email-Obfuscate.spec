#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Obfuscate
Summary:	Email::Obfuscate - obfuscates email addresses
Summary(pl):	Email::Obfuscate - ukrawanie adresów e-mail
Name:		perl-Email-Obfuscate
Version:	1.13
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc2dfd650cd83d1f2bad9bec60cf45a2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides for the obfuscation of email address in an,
ostensibly superficial, attempt to thwart email address harvesters.

Currently, there are eight different "types" of email address
obfuscation transformations that this module employs. One of these
transformations is randomly selected and used as a basis for
obfuscation when obfuscate_email_address() is called.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/0-signature.t{,.blah}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
