Name:		texlive-translation-array-fr
Version:	24344
Release:	2
Summary:	French translation of the documentation of array
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/array/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-array-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-array-fr.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
