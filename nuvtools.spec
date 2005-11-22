Summary:	MythTV nuv video file conversion script
Name:		nuvtools
Version:	0.0.2
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://mythtv.beirdo.ca/files/%{name}-%{version}.tar.gz
# Source0-md5:	f2b207666c5af83ac4a6d0726076068d
URL:		http://mythtv.beirdo.ca/nuvtools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nuvtools includes: 
- nuvscan - shows the contents of every frame in the NUV file (very
  verbose)
- nuv2avi - converts NUV files to AVI with minimal recoding

%prep
%setup -q

%build
%{__make} -C libavcodec CC="%{__cc}" OPTFLAGS="%{rpmcflags}"
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
