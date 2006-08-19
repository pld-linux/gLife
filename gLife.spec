Summary:	An artificial life simulator
Summary(pl):	Symulator sztucznej inteligencji.
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
ExclusiveArch:	%{ix86}
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

%description -l pl
gLife to próba uosobienia zasad rz±dz±cych w sztucznym ¿yciu. Sztuczne
¿ycie jest rodzajem sztucznej inteligencji. Ten program przypomina
"Conway's Game of Life" jednak znacznie siê od niego ró¿ni. gLife
ukazuje sztuczn± spo³eczno¶æ (ludzk±). To oznacza, ¿e jest o wiele
bardziej zró¿nicowane i z³o¿one od "Conway's Game of Life". Pod uwagê
brane s± takie rzeczy jak teren, wiek, p³eæ, kultura, przemieszczanie
itp.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glife/
%{_datadir}/gnome/*
