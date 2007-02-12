Summary:	Dockable Interrupts Monitor for WindowMaker
Summary(pl.UTF-8):   Monitor przerwań dla Doku WindowMakera
Name:		wmint
Version:	0.9
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://team.gcu-squad.org/~slix/wmint/%{name}-%{version}.tar.gz
# Source0-md5:	fa897484a9e68168526f681939154f85
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://team.gcu-squad.org/~slix/wmint/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmint is a simple dockable Interrupts Monitor for Window Maker.

%description -l pl.UTF-8
wmint jest prostym, dokowalnym monitorem przerwań dla WindowMakera.

%prep
%setup -q
%patch0 -p1

%build
cd wmint

%{__make} clean
%{__make} %{name} \
	FLAGS="%{rpmcflags} -I%{_includedir}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/%{name}.desktop
