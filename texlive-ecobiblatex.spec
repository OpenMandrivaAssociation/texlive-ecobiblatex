Name:		texlive-ecobiblatex
Version:	39233
Release:	2
Summary:	Global Ecology and Biogeography BibLaTeX styles for the Biber backend
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ecobiblatex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecobiblatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecobiblatex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides a set of styles for creating
bibliographies using BibLaTeX in the style of the Global
Ecology and Biogeography journal. It comprises styles based on
the conventions of John Wiley & Sons Ltd and Global Ecology and
Biogeography Conventions (c).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ecobiblatex
%doc %{_texmfdistdir}/doc/latex/ecobiblatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
