# NOTE:		Please keep in sync with aumix.
Summary:	curses and X11/Gtk ased audio mixer
Summary(de):	Audio-Mixer auf curses- und X11/Gtk-Basis
Summary(pl):	Mikser audio bazuj�cy na curses i Gtk+
Name:		aumix-gtk
Version:	2.7
Release:	5
License:	GPL
Group:		Applications/Sound
Source0:	http://www.jpj.net/~trevor/aumix/aumix-%{version}.tar.gz
Source2:	aumix.desktop
Patch0:		aumix-home_etc.patch
Patch1:		aumix-xaumix.patch
Patch2:		aumix-ac250.patch
URL:		http://www.jpj.net/~trevor/aumix.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gpm-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	aumix
Obsoletes:	aumix
Conflicts:	aumix

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program provides a tty- and X11/Gtk-based, interactive method of
controlling a sound card's mixer. It lets you adjust the input levels
from the CD, microphone, and onboard synthesizers as well as the
output volume.

%description -l de
Dieses Programm bietet eine interaktive Methode auf tty- und
X11/Gtk-Basis zur Steuerung eines Soundkarten-Mixers. Sie k�nnen damit
die Eingangspegel der CD, des Mikrophons und von Synthesizer-Karten
sowie auch die Ausgabelautst�rke regeln.

%description -l pl
Ten program przynosi bazuj�c� na tty oraz X11/Gtk, interaktywn� metod�
kontrolowania miksera karty d�wi�kowej. aumix pozwala zmienia� poziom
sygna�u nadchodz�cego z CD, mikrofonu i syntetyzer�w tak samo jak
poziom sygna�u wyj�ciowego.

%prep
%setup -q -n aumix-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -rf missing acinclude.m4
%{__gettextize}
aclocal
%{__autoconf}
%{__automake}

CPPFLAGS="-I/usr/include/ncurses" \
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/aumix/*xpm $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

touch $RPM_BUILD_ROOT%{_sysconfdir}/aumixrc

%find_lang aumix

%clean
rm -rf $RPM_BUILD_ROOT

%files -f aumix.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%config(noreplace,missingok) %verify(not size mtime md5) %{_sysconfdir}/aumixrc

%attr(755,root,root) %{_bindir}/aumix

%{_pixmapsdir}/*.xpm
%{_applnkdir}/Multimedia/aumix.desktop

%{_datadir}/aumix
%{_mandir}/man1/*
