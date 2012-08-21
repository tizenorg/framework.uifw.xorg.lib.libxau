Name:    libXau
Summary: X.Org X11 libXau runtime library
Version: 1.0.7
Release: 1
Group:   System/Libraries
License: MIT
URL:     http://www.x.org/
Source0: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}
This is a very simple mechanism for providing individual access to an X Window
System display.It uses existing core protocol and library hooks for specifying
authorization data in the connection setup block to restrict use of the display
to only those clients that show that they know a server-specific key
called a "magic cookie".

%package devel
Summary:  Development components for the libXau library
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxau-devel

%description devel
Description: %{summary}


%prep
%setup -q


%build

./autogen.sh
%reconfigure --disable-static

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# remove *.la files
rm -f %{buildroot}%{_libdir}/*.la

%remove_docs

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%{_includedir}/X11/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
