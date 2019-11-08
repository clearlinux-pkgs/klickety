#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : klickety
Version  : 19.08.3
Release  : 14
URL      : https://download.kde.org/stable/applications/19.08.3/src/klickety-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/klickety-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/klickety-19.08.3.tar.xz.sig
Summary  : An adaptation of the Clickomania game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: klickety-bin = %{version}-%{release}
Requires: klickety-data = %{version}-%{release}
Requires: klickety-license = %{version}-%{release}
Requires: klickety-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
Klickety used KNotify with just two standard KDE sounds.
I ported it to KgSound but just copied those used
standard KDE sounds into Klickety. Here is what was copied:

%package bin
Summary: bin components for the klickety package.
Group: Binaries
Requires: klickety-data = %{version}-%{release}
Requires: klickety-license = %{version}-%{release}

%description bin
bin components for the klickety package.


%package data
Summary: data components for the klickety package.
Group: Data

%description data
data components for the klickety package.


%package doc
Summary: doc components for the klickety package.
Group: Documentation

%description doc
doc components for the klickety package.


%package license
Summary: license components for the klickety package.
Group: Default

%description license
license components for the klickety package.


%package locales
Summary: locales components for the klickety package.
Group: Default

%description locales
locales components for the klickety package.


%prep
%setup -q -n klickety-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573171780
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573171780
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/klickety
cp %{_builddir}/klickety-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/klickety/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/klickety-19.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/klickety/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang klickety

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/klickety

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.klickety.desktop
/usr/share/applications/org.kde.ksame.desktop
/usr/share/icons/hicolor/128x128/apps/klickety.png
/usr/share/icons/hicolor/128x128/apps/ksame.png
/usr/share/icons/hicolor/16x16/apps/klickety.png
/usr/share/icons/hicolor/16x16/apps/ksame.png
/usr/share/icons/hicolor/22x22/apps/klickety.png
/usr/share/icons/hicolor/22x22/apps/ksame.png
/usr/share/icons/hicolor/32x32/apps/klickety.png
/usr/share/icons/hicolor/32x32/apps/ksame.png
/usr/share/icons/hicolor/48x48/apps/klickety.png
/usr/share/icons/hicolor/48x48/apps/ksame.png
/usr/share/icons/hicolor/64x64/apps/klickety.png
/usr/share/icons/hicolor/64x64/apps/ksame.png
/usr/share/kconf_update/klickety-2.0-inherit-ksame-highscore.pl
/usr/share/kconf_update/klickety.upd
/usr/share/klickety/klickety.kcfg
/usr/share/klickety/themes/classic.svg
/usr/share/klickety/themes/classic_preview.png
/usr/share/klickety/themes/default.desktop
/usr/share/klickety/themes/ksame.desktop
/usr/share/klickety/themes/ksame.svg
/usr/share/klickety/themes/ksame_old.desktop
/usr/share/klickety/themes/ksame_old.svg
/usr/share/klickety/themes/ksame_old_preview.png
/usr/share/klickety/themes/ksame_preview.png
/usr/share/kxmlgui5/klickety/klicketyui.rc
/usr/share/metainfo/org.kde.klickety.appdata.xml
/usr/share/metainfo/org.kde.ksame.appdata.xml
/usr/share/sounds/klickety/game-finished.ogg
/usr/share/sounds/klickety/remove.ogg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/klickety/index.cache.bz2
/usr/share/doc/HTML/de/klickety/index.docbook
/usr/share/doc/HTML/en/klickety/config-background.png
/usr/share/doc/HTML/en/klickety/config-customgame.png
/usr/share/doc/HTML/en/klickety/config-general.png
/usr/share/doc/HTML/en/klickety/config-theme.png
/usr/share/doc/HTML/en/klickety/gamescreen.png
/usr/share/doc/HTML/en/klickety/highscore.png
/usr/share/doc/HTML/en/klickety/index.cache.bz2
/usr/share/doc/HTML/en/klickety/index.docbook
/usr/share/doc/HTML/en/klickety/ksamemode.png
/usr/share/doc/HTML/en/klickety/numbered.png
/usr/share/doc/HTML/es/klickety/index.cache.bz2
/usr/share/doc/HTML/es/klickety/index.docbook
/usr/share/doc/HTML/et/klickety/index.cache.bz2
/usr/share/doc/HTML/et/klickety/index.docbook
/usr/share/doc/HTML/fr/klickety/config-background.png
/usr/share/doc/HTML/fr/klickety/config-customgame.png
/usr/share/doc/HTML/fr/klickety/config-general.png
/usr/share/doc/HTML/fr/klickety/config-theme.png
/usr/share/doc/HTML/fr/klickety/gamescreen.png
/usr/share/doc/HTML/fr/klickety/highscore.png
/usr/share/doc/HTML/fr/klickety/index.cache.bz2
/usr/share/doc/HTML/fr/klickety/index.docbook
/usr/share/doc/HTML/fr/klickety/ksamemode.png
/usr/share/doc/HTML/fr/klickety/numbered.png
/usr/share/doc/HTML/fr/klickety/shortcuts.png
/usr/share/doc/HTML/it/klickety/index.cache.bz2
/usr/share/doc/HTML/it/klickety/index.docbook
/usr/share/doc/HTML/nl/klickety/index.cache.bz2
/usr/share/doc/HTML/nl/klickety/index.docbook
/usr/share/doc/HTML/pt/klickety/index.cache.bz2
/usr/share/doc/HTML/pt/klickety/index.docbook
/usr/share/doc/HTML/pt_BR/klickety/index.cache.bz2
/usr/share/doc/HTML/pt_BR/klickety/index.docbook
/usr/share/doc/HTML/sv/klickety/index.cache.bz2
/usr/share/doc/HTML/sv/klickety/index.docbook
/usr/share/doc/HTML/uk/klickety/config-background.png
/usr/share/doc/HTML/uk/klickety/config-customgame.png
/usr/share/doc/HTML/uk/klickety/config-general.png
/usr/share/doc/HTML/uk/klickety/config-theme.png
/usr/share/doc/HTML/uk/klickety/gamescreen.png
/usr/share/doc/HTML/uk/klickety/highscore.png
/usr/share/doc/HTML/uk/klickety/index.cache.bz2
/usr/share/doc/HTML/uk/klickety/index.docbook
/usr/share/doc/HTML/uk/klickety/ksamemode.png
/usr/share/doc/HTML/uk/klickety/numbered.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/klickety/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/klickety/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f klickety.lang
%defattr(-,root,root,-)

