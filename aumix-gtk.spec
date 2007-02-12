# NOTE:		Please keep in sync with aumix.
#
# Conditional build:
%bcond_with	gtk1	# build with GTK+ instead of GTK+2
#
Summary:	curses and X11/GTK+ based audio mixer
Summary(de.UTF-8):	Audio-Mixer auf curses- und X11/GTK+-Basis
Summary(es.UTF-8):	Mezclador de audio basado en curses y X11/GTK+
Summary(pl.UTF-8):	Mikser audio bazujący na curses i GTK+
Summary(ru.UTF-8):	Аудио микшер на базе библиотеки curses и GTK+
Summary(uk.UTF-8):	Аудіо мікшер, базований на біблиотеці curses і GTK+
Name:		aumix-gtk
Version:	2.8
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://www.jpj.net/~trevor/aumix/aumix-%{version}.tar.bz2
# Source0-md5:	dc3fc7209752207c23e7c94ab886b340
Source3:	%{name}.desktop
Source4:	aumix.png
Patch0:		aumix-home_etc.patch
Patch1:		aumix-xaumix.patch
Patch2:		aumix-ac250.patch
URL:		http://www.jpj.net/~trevor/aumix.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
%if %{with gtk1}
BuildRequires:	gtk+-devel >= 1.2.0
%else
BuildRequires:	gtk+2-devel >= 1:2.0.0
%endif
BuildRequires:	ncurses-devel >= 5.0
Provides:	aumix
Obsoletes:	aumix
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program provides a tty- and X11/GTK+-based, interactive method of
controlling a sound card's mixer. It lets you adjust the input levels
from the CD, microphone, and onboard synthesizers as well as the
output volume.

%description -l de.UTF-8
Dieses Programm bietet eine interaktive Methode auf tty- und
X11/GTK+-Basis zur Steuerung eines Soundkarten-Mixers. Sie können
damit die Eingangspegel der CD, des Mikrophons und von
Synthesizer-Karten sowie auch die Ausgabelautstärke regeln.

%description -l es.UTF-8
Este programa nos ofrece un método interactivo basado en tty y
X11/GTK+ de control de mezclas de tarjetas de sonido. Deja que se
ajuste los niveles de entrada del CD, micrófono, y sintetizadores, así
como el volumen de salida.

%description -l pl.UTF-8
Ten program przynosi bazującą na tty oraz X11/GTK+, interaktywną
metodę kontrolowania miksera karty dźwiękowej. aumix pozwala zmieniać
poziom sygnału nadchodzącego z CD, mikrofonu i syntetyzerów tak samo
jak poziom sygnału wyjściowego.

%description -l ru.UTF-8
Эта программа - консольный и X11/GTK+, интерактивный регулятор уровней
микшера звуковой карты. Она позволяет изменять как входные уровни
сигналов с CD, микрофона, синтезаторов на звуковой плате, так и
выходной уровень.

%description -l uk.UTF-8
Ця програма - консольний і X11/GTK+, інтерактивний регулятор рівней
мікшеру звукової картки. Вона дозволяє змінювати як вхідні рівні
сигналів з CD, мікрофону, синтезаторів на звуковій платі, так і
вихідний рівень.

%prep
%setup -q -n aumix-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#%%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

CPPFLAGS="-I/usr/include/ncurses"
%configure \
%if %{with gtk1}
	--without-gtk
%else
	--without-gtk1
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/aumix.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/aumix/aumix.xpm

:> $RPM_BUILD_ROOT%{_sysconfdir}/aumixrc

%find_lang aumix

%clean
rm -rf $RPM_BUILD_ROOT

%files -f aumix.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/aumixrc

%attr(755,root,root) %{_bindir}/aumix
%{_mandir}/man1/*
%{_datadir}/aumix

%{_pixmapsdir}/*.png
%{_desktopdir}/aumix.desktop
