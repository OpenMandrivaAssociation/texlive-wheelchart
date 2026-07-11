%global tl_name wheelchart
%global tl_revision 78755

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.0
Release:	%{tl_revision}.1
Summary:	Diagrams with circular or other shapes using TikZ and LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/wheelchart
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wheelchart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wheelchart.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is based on the package TikZ and can be used to draw
various kinds of diagrams such as bar charts, doughnut charts,
infographics, pie charts, ring charts, square charts, sunburst charts,
waffle charts and wheel charts. It provides several options to customize
the diagrams. It is also possible to specify a plot for the shape of the
chart. Furthermore a legend can be added and the table of contents can
be displayed as one of these diagrams.

