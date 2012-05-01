Name: hyphen-es
Summary: Spanish hyphenation rules
%define upstreamid 20040810
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_es_ES.zip
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hyphen

%description
Spanish hyphenation rules.

%prep
%setup -q -c

%build
chmod -x README_hyph_es_ES.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
es_ES_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_ES_aliases; do
        ln -s hyph_es_ES.dic hyph_$lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hyph_es_ES.txt
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20040810-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040810-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040810-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2008 Caolan McNamara <caolanm@redhat.com> - 0.20040810-1
- initial version
