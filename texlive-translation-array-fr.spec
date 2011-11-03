# revision 24344
# category Package
# catalog-ctan /info/translations/array/fr
# catalog-date 2011-10-20 17:00:28 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-array-fr
Version:	20111020
Release:	1
Summary:	French translation of the documentation of array
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/array/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-array-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-array-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A French translation of the documentation of array.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/Copyright
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/README
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/f-array.dtx
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/f-array.pdf
%doc %{_texmfdistdir}/doc/latex/translation-array-fr/ltxdoc.cfg
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}