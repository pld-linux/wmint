Summary:	Dockable Interrupts Monitor for WindowMaker
Summary(pl):	Monitor przerwañ dla Doku WindowMakera 
Name:		wmint
Version:	0.9
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.gcu-squad.org/wmint/%{name}-%{version}.tar.gz
Source1:	wmint.desktop
URL:		http://www.gcu-squad.org/wmint/
BuildRequires:	XFree86-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
wmint is a simple dockable Interrupts Monitor for Window Maker.

%description -l pl
wmint jest prostym, dokowalnym monitorem przerwañ dla WindowMakera.

%prep
%setup -q

rm -f %{name}/wmint.o

%build
%{__make} -C %{name} \
	FLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}         $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS HINTS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,HINTS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/%{name}.desktop
