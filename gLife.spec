# TODO: desktop patch, icon
Summary:	An artificial life simulator
Summary(pl.UTF-8):   Symulator sztucznej inteligencji
Name:		gLife
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/glife/%{name}-%{version}.tar.gz
# Source0-md5:	1176413bec7aad8410f492d8fda43706
URL:		http://glife.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-gnome-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gLife is an attempt to emobdy the rules that are found in artificial
life. Artificial life is a subset of artificial intelligence. This
program is similiar to "Conway's Game of Life" but yet it is very
different. It takes "Conway's Game of Life" and applies it to a
society (human society). This means there is a very different (and
much larger) ruleset than in the original game. Things need to be
taken into account such as the terrain, age, sex, culture, movement,
etc.

%description -l pl.UTF-8
gLife to próba uosobienia zasad rządzących w sztucznym życiu. Sztuczne
życie jest rodzajem sztucznej inteligencji. Ten program przypomina
"Conway's Game of Life" jednak znacznie się od niego różni. gLife
ukazuje sztuczną społeczność (ludzką). To oznacza, że jest o wiele
bardziej zróżnicowane i złożone od "Conway's Game of Life". Pod uwagę
brane są takie rzeczy jak teren, wiek, płeć, kultura, przemieszczanie
itp.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

%find_lang glife --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f glife.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glife
%{_desktopdir}/glife.desktop
