Name:		texlive-wheelchart
Version:	71928
Release:	1
Summary:	Draw wheelcharts with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wheelchart
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wheelchart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wheelchart.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is based on the package TikZ and can be used to
draw wheelcharts with TikZ. It provides several options to
customize the wheelcharts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/wheelchart
%doc %{_texmfdistdir}/doc/latex/wheelchart

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
