# NOTE:		Please keep in sync with aumix.
Summary:	curses and X11/Gtk ased audio mixer
Summary(de):	Audio-Mixer auf curses- und X11/Gtk-Basis
Summary(pl):	Mikser audio bazuj±cy na curses
Name:		aumix-gtk
Version:	2.7
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.jpj.net/~trevor/aumix/aumix-%{version}.tar.gz
Source2:	aumix.desktop
Patch0:		aumix-home_etc.patch
Patch1:		aumix-xaumix.patch
URL:		http://www.jpj.net/~trevor/aumix.html
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gpm-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	aumix
Obsoletes:	aumix

%define		_prefix		/usr/X11R6
%define		_manpath	%{_prefix}/man

%description
This program provides a tty- and X11/Gtk-based, interactive method of
controlling a sound card's mixer. It lets you adjust the input levels
from the CD, microphone, and onboard synthesizers as well as the
output volume.

%description -l de
Dieses Programm bietet eine interaktive Methode auf tty- und
X11/Gtk-Basis zur Steuerung eines Soundkarten-Mixers. Sie können damit
die Eingangspegel der CD, des Mikrophons und von Synthesizer-Karten
sowie auch die Ausgabelautstärke regeln.

%description -l pl
Ten program przynosi bazuj±c± na tty oraz X11/Gtk, interaktywn± metodê
kontrolowania miksera karty d¼wiêkowej. aumix pozwala zmieniaæ poziom
sygna³u nadchodz±cego z CD, mikrofonu i syntetyzerów tak samo jak
poziom sygna³u wyj¶ciowego.

%prep
%setup -q -n aumix-%{version}
%patch0 -p1
%patch1 -p1

%build
automake
autoconf
gettextize --copy --force

CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pixmaps} \
	$RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/aumix/*xpm \
$RPM_BUILD_ROOT%{_datadir}/pixmaps

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

touch $RPM_BUILD_ROOT%{_sysconfdir}/aumixrc

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS BUGS ChangeLog NEWS README 

%find_lang aumix

%clean
rm -rf $RPM_BUILD_ROOT

%files -f aumix.lang
%defattr(644,root,root,755)
%config(noreplace,missingok) %{_sysconfdir}/aumixrc
%doc {AUTHORS,BUGS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) %{_bindir}/aumix

%{_pixmapsdir}/*.xpm
%{_applnkdir}/Multimedia/aumix.desktop

%{_datadir}/aumix
%{_mandir}/man1/*
