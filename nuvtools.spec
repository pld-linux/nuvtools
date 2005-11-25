# TODO
# - find (make) system librtjpeg package and use it
#
# Conditional build:
%bcond_with	system_ffmpeg	# use system ffmpeg (bundled one doesn't compile under amd64)
#
Summary:	MythTV NUV video file conversion script
Summary(pl):	Skrypty do konwersji obrazu NUV dla MythTV
Name:		nuvtools
Version:	0.0.3
%define	_snap 20051122
Release:	0.%{_snap}.1
License:	GPL v2
Group:		Applications/Multimedia
#Source0:	http://mythtv.beirdo.ca/files/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	850c9499b2fcfee18658f511e33f0a0f
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-ffmpeg.patch
URL:		http://mythtv.beirdo.ca/nuvtools/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with system_ffmpeg}
BuildRequires:	ffmpeg-devel
%else
BuildRequires:	lame-libs-devel
BuildRequires:	xvid-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nuvtools includes:
- nuvscan - shows the contents of every frame in the NUV file (very
  verbose)
- nuv2avi - converts NUV files to AVI with minimal recoding

%description -l pl
Pakiet nuvtools zawiera programy:
- nuvscan - pokazuj±cy zawarto¶æ ka¿dej klatki w pliku NUV (bardzo
  szczegó³owo),
- nuv2avi - konwertuj±cy pliki NUV do AVI z minimalnym
  przekodowywaniem.

%prep
%setup -q %{?_snap:-n %{name}}
%patch0 -p1
%if %{with system_ffmpeg}
%patch1 -p1
rm -rf ffmpeg
%endif

%build
%if %{without system_ffmpeg}
cd ffmpeg
%configure \
	--enable-pthreads \
	--enable-gpl \
	--enable-mp3lame \
	--enable-xvid \
	--disable-vhook \
	--disable-zlib \
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags} -fomit-frame-pointer" \
	--extra-ldflags="%{rpmldflags}" \
	--disable-debug \
	--disable-opts \
	--tune=generic
cd ..
%endif

cd librtjpeg
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
cd ..

%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
