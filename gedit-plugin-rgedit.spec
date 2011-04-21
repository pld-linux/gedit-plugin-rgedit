# 
# TODO:
#	- update Requires
#
Summary:	rgedit plugin for gedit
Summary(pl.UTF-8):	Wtyczka rgedit dla gedita
Name:		gedit-plugin-rgedit
Version:	0.7.1.0
Release:	3
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://downloads.sourceforge.net/rgedit/rgedit-%{version}.tar.bz2
# Source0-md5:	87ae1727a0c5cd854bb888448643ead9
URL:		http://sourceforge.net/projects/rgedit/
BuildRequires:  rpm-pythonprov
Requires:	R
Requires:	gedit2 >= 2.22.0
Requires:	python-modules
Requires:	python-vte
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gedit plug-in allowing it to become an easy-to-use and yet
light-weight IDE for the statistical programming environment, R.

%description -l pl.UTF-8
Wtyczka dla gedita zamieniające edytor w proste i lekkie IDE dla
systemu R do obliczeń statystycznych i grafiki.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/gedit-2/plugins

cp -a RCtrl.py $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/
cp -a RCtrl.gedit-plugin $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/
cp -a RCtrl $RPM_BUILD_ROOT%{_datadir}/gedit-2/plugins/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe.txt
%{_libdir}/gedit-2/plugins/RCtrl.py
%{_libdir}/gedit-2/plugins/RCtrl.gedit-plugin
%{_datadir}/gedit-2/plugins/RCtrl
