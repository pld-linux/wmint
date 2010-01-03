Summary:	Dockable Interrupts Monitor for WindowMaker
Summary(pl.UTF-8):	Monitor przerwań dla Doku WindowMakera
Name:		wmint
Version:	0.9
Release:	7
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://team.gcu-squad.org/~slix/wmint/%{name}-%{version}.tar.gz
# Source0-md5:	fa897484a9e68168526f681939154f85
Source1:	%{name}.desktop
Source2:	%{name}.Makefile
URL:		http://team.gcu-squad.org/~slix/wmint/
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmint is a simple dockable Interrupts Monitor for Window Maker.

%description -l pl.UTF-8
wmint jest prostym, dokowalnym monitorem przerwań dla WindowMakera.

%prep
%setup -q

awk '/OBJS *=/{p=1} {if(p)print} !/\\$/{p=0}' wmint/Makefile > wmint/Makefile.include

cat << 'EOF' >> wmint/Makefile.include
NAME = %{name}
DOCKLETFILE = %{SOURCE1}
CC = %{__cc}
OPTCFLAGS = %{rpmcflags}
LDFLAGS = %{rpmldflags}
EOF

install %{SOURCE2} wmint/Makefile

%build
%{__make} -C wmint clean
%{__make} -C wmint

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C wmint install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/%{name}.desktop
