Summary:	Dockable Interrupts Monitor for WindowMaker
Summary(pl):	Monitor przerwañ dla Doku WindowMakera
Name:		wmint
Version:	0.9
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://team.gcu-squad.org/~slix/%{name}-%{version}.tar.gz
# Source0-md5:	fa897484a9e68168526f681939154f85
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://team.gcu-squad.org/~slix/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmint is a simple dockable Interrupts Monitor for Window Maker.

%description -l pl
wmint jest prostym, dokowalnym monitorem przerwañ dla WindowMakera.

%prep
%setup -q
%patch0 -p1

%build
cd wmint

%{__make} clean
%{__make} %{name} \
	FLAGS="%{rpmcflags} -I%{_includedir}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1}         $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}

#%%{_applnkdir}/DockApplets/%{name}.desktop
