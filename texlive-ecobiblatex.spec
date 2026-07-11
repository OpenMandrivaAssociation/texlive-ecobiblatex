%global tl_name ecobiblatex
%global tl_revision 39233

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Global Ecology and Biogeography BibLaTeX styles for the Biber backend
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/ecobiblatex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecobiblatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecobiblatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides a set of styles for creating bibliographies using
BibLaTeX in the style of the Global Ecology and Biogeography journal. It
comprises styles based on the conventions of John Wiley & Sons Ltd and
Global Ecology and Biogeography Conventions (c).

