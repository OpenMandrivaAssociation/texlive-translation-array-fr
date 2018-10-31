# revision 24344
# category Package
# catalog-ctan /info/translations/array/fr
# catalog-date 2011-10-20 17:00:28 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-array-fr
Version:	20180303
Release:	2
Summary:	French translation of the documentation of array
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/array/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-array-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-array-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A French translation of the documentation of array.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/Copyright
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/README
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/f-array.dtx
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/f-array.pdf
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/ltxdoc.cfg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111020-2
+ Revision: 757077
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111020-1
+ Revision: 719792
- texlive-translation-array-fr
- texlive-translation-array-fr
- texlive-translation-array-fr

