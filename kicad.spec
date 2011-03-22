Name:           kicad
Version:        2011.01.28
Release:        1.rev2765%{?dist}
Summary:        Electronic schematic diagrams and printed circuit board artwork
Summary(fr):    Saisie de schéma électronique et routage de circuit imprimé

Group:          Applications/Engineering
License:        GPLv2+
URL:            https://launchpad.net/kicad

# Source files created from upstream's bazaar repository
# bzr export -r 2765 kicad-2011.01.28
# bzr export -r 109 kicad-libraries-2011.01.28
# bzr export -r 163 kicad-doc-2011.01.28

Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-doc-%{version}.tar.bz2
Source2:        %{name}-libraries-%{version}.tar.bz2
Source3:        %{name}-ld.conf
Source4:        %{name}-2010.05.09.x-kicad-pcbnew.desktop
Source5:        pcbnew.desktop
Source6:        %{name}-icons.tar.bz2

Patch10:        %{name}-%{version}-real-version.patch
Patch11:        %{name}-%{version}-fix-build.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK-devel
BuildRequires:  boost-devel
BuildRequires:  cmake

Requires:       electronics-menu

%description
Kicad is an EDA software to design electronic schematic
diagrams and printed circuit board artwork up to 16 layers.
Kicad is a set of four softwares and a project manager:
- Eeschema: schematic entry
- Pcbnew: board editor
- Gerbview: GERBER viewer (photoplotter documents)
- Cvpcb: footprint selector for components used in the circuit design
- Kicad: project manager

%description -l fr
Kicad est un logiciel open source (GPL) pour la création de schémas
électroniques et le tracé de circuits imprimés jusqu'à 16 couches.
Kicad est un ensemble de quatres logiciels et un gestionnaire de projet :
- Eeschema : saisie de schémas
- Pcbnew : éditeur de circuits imprimés
- Gerbview : visualisateur GERBER (documents pour phototraçage)
- Cvpcb : sélecteur d'empreintes pour les composants utilisés dans le circuit
- Kicad : gestionnaire de projet.


%package        doc
Summary:        Documentations for kicad
Summary(fr):    Documentations pour kicad en anglais
Group:          Applications/Engineering
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc
Documentations and tutorials for kicad in English


%package        doc-de
Summary:        Documentation for Kicad in German
Summary(fr):    Documentations pour kicad en allemand
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-de
Documentation and tutorials for Kicad in German


%package        doc-es
Summary:        Documentation for Kicad in Spanish
Summary(fr):    Documentations pour kicad en espagnol
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-es
Documentation and tutorials for Kicad in Spanish


%package        doc-fr
Summary:        Documentation for Kicad in French
Summary(fr):    Documentations pour kicad en français
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-fr
Documentation and tutorials for Kicad in French


%package        doc-hu
Summary:        Documentation for Kicad in Hungarian
Summary(fr):    Documentations pour kicad en hongrois
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-hu
Documentation and tutorials for Kicad in Hungarian


%package        doc-it
Summary:        Documentation for Kicad in Italian
Summary(fr):    Documentations pour kicad en italien
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-it
Documentation and tutorials for Kicad in Italian


%package        doc-pt
Summary:        Documentation for Kicad in Portuguese
Summary(fr):    Documentations pour kicad en portugais
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-pt
Documentation and tutorials for Kicad in Portuguese


%package        doc-ru
Summary:        Documentation for Kicad in Russian
Summary(fr):    Documentations pour kicad en russe
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-ru
Documentation and tutorials for Kicad in Russian


%package        doc-zh_CN
Summary:        Documentation for Kicad in Chinese
Summary(fr):    Documentations pour kicad en chinois
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
%if 0%{?fedora} >= 11
BuildArch:      noarch
%endif

%description    doc-zh_CN
Documentation and tutorials for Kicad in Chinese


%prep
%setup -q -a 1 -a 2 -a 6

%patch10 -p0 -b .real-version
%patch11 -p1 -b .fix-build

#kicad-doc.noarch: W: file-not-utf8 /usr/share/doc/kicad/AUTHORS.txt
iconv -f iso8859-1 -t utf-8 AUTHORS.txt > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS.txt


#multilibs
%ifarch x86_64 sparc64 ppc64 amd64 s390x
%{__sed} -i "s|KICAD_PLUGINS lib/kicad/plugins|KICAD_PLUGINS lib64/kicad/plugins|" CMakeLists.txt
%{__sed} -i "s|/usr/lib/kicad|/usr/lib64/kicad|" %{SOURCE3}
%endif


%build

#
# Symbols libraries
#
pushd %{name}-libraries-%{version}/
%cmake -DCMAKE_BUILD_TYPE=Release .
%{__make} %{?_smp_mflags} VERBOSE=1
popd


#
# Core components
#
%cmake -DCMAKE_BUILD_TYPE=Release
%{__make} %{?_smp_mflags} VERBOSE=1


%install
%{__rm} -rf %{buildroot}

%{__make} INSTALL="install -p" DESTDIR=%{buildroot} install


# install localization
cd %{name}-doc-%{version}/internat
for dir in ca cs de es fr hu it ko nl pl pt ru sl sv zh_CN
do
  install -m 644 -D ${dir}/%{name}.mo %{buildroot}%{_datadir}/locale/${dir}/%{name}.mo
done
cd ../..


# install desktop
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --remove-category Development              \
  --delete-original                          \
  %{buildroot}%{_datadir}/applications/kicad.desktop

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --remove-category Development              \
  --delete-original                          \
  %{buildroot}%{_datadir}/applications/eeschema.desktop

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --remove-category Development              \
  %{SOURCE5}

# Missing requires libraries
%{__cp} -p ./3d-viewer/lib3d-viewer.so %{buildroot}%{_libdir}/%{name}
%{__cp} -p ./bitmaps/libbitmaps.so %{buildroot}%{_libdir}/%{name}
%{__cp} -p ./common/libcommon.so %{buildroot}%{_libdir}/%{name}
%{__cp} -p ./polygon/kbool/src/libkbool.so %{buildroot}%{_libdir}/%{name}
%{__cp} -p ./common/libpcbcommon.so %{buildroot}%{_libdir}/%{name}
%{__cp} -p ./polygon/libpolygon.so %{buildroot}%{_libdir}/%{name}

#
# Symbols libraries
#
pushd %{name}-libraries-%{version}/
%{__make} INSTALL="install -p" DESTDIR=%{buildroot} install
popd

# install ld.conf
install -m 644 -D -p %{SOURCE3} %{buildroot}%{_sysconfdir}/ld.so.conf.d/kicad.conf

# install template
install -d %{buildroot}%{_datadir}/%{name}/template
install -m 644 template/%{name}.pro %{buildroot}%{_datadir}/%{name}/template

# install new mime type
install -pm 644 %{SOURCE4} %{buildroot}%{_datadir}/mimelnk/application/x-%{name}-pcbnew.desktop

# install mimetype and application icons
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/mimetypes/application-x-kicad-eeschema.png %{buildroot}%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-kicad-eeschema.png
install -m 644 -D -p %{name}-icons/resources/linux/mime/icons/hicolor/32x32/apps/eeschema.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/mimetypes/application-x-kicad-eeschema.png %{buildroot}%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-kicad-eeschema.png
install -m 644 -D -p %{name}-icons/resources/linux/mime/icons/hicolor/24x24/apps/eeschema.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/mimetypes/application-x-kicad-eeschema.png %{buildroot}%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-kicad-eeschema.png
install -m 644 -D -p %{name}-icons/resources/linux/mime/icons/hicolor/22x22/apps/eeschema.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/mimetypes/application-x-kicad-eeschema.png %{buildroot}%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-kicad-eeschema.png
install -m 644 -D -p %{name}-icons/resources/linux/mime/icons/hicolor/16x16/apps/eeschema.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/eeschema.png

install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/mimetypes/application-x-kicad-pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/apps/pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/mimetypes/application-x-kicad-pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/apps/pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/mimetypes/application-x-kicad-pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/apps/pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/mimetypes/application-x-kicad-pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/apps/pcbnew.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/pcbnew.png

install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/apps/kicad.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/kicad.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/apps/kicad.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/kicad.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/apps/kicad.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/kicad.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/apps/kicad.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/kicad.png


# Preparing for documentation pull-ups
%{__rm} -f  %{name}-doc-%{version}/doc/help/CMakeLists.txt
%{__rm} -f  %{name}-doc-%{version}/doc/help/makefile
%{__rm} -f  %{name}-doc-%{version}/doc/tutorials/CMakeLists.txt

%{__cp} -pr %{name}-doc-%{version}/doc/* %{buildroot}%{_docdir}/%{name}
%{__cp} -pr AUTHORS.txt CHANGELOG* version.txt %{buildroot}%{_docdir}/%{name}


%find_lang %{name}


%post
touch --no-create %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

/sbin/ldconfig


%postun
if [ $1 -eq 0 ]
then
  touch --no-create %{_datadir}/icons/hicolor || :
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :
update-mime-database %{_datadir}/mime &> /dev/null || :

/sbin/ldconfig


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_docdir}/%{name}/help/en/kicad.pdf
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}-*.*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-%{name}-*.desktop
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/kicad.conf

%files doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/help/
%dir %{_docdir}/%{name}/tutorials
%doc %{_docdir}/%{name}/*.txt
%doc %{_docdir}/%{name}/scripts
%doc %{_docdir}/%{name}/contrib
%doc %{_docdir}/%{name}/help/en/docs_src/
%doc %{_docdir}/%{name}/help/en/cvpcb.pdf
%doc %{_docdir}/%{name}/help/en/eeschema.pdf
%doc %{_docdir}/%{name}/help/en/gerbview.pdf
%doc %{_docdir}/%{name}/help/en/pcbnew.pdf
%doc %{_docdir}/%{name}/help/file_formats
%doc %{_docdir}/%{name}/tutorials/en

%files doc-de
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/help/de
%doc %{_docdir}/%{name}/tutorials/de

%files doc-es
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/help/es
%doc %{_docdir}/%{name}/tutorials/es

%files doc-fr
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/help/fr
%doc %{_docdir}/%{name}/tutorials/fr

%files doc-hu
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/tutorials/hu

%files doc-it
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/help/it

%files doc-pt
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/help/pt

%files doc-ru
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/help/ru
%doc %{_docdir}/%{name}/tutorials/ru

%files doc-zh_CN
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/tutorials/zh_CN


%changelog
* Tue Mar 22 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-1.rev2765
- New upstream version
- Update versioning patch, all others patches no more needed
- Patch to fix a link time error (with help from Kevin Kofler and Nikola Pajkovsky)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.05.27-10.rev2363
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Dan Horák <dan@danny.cz> - 2010.05.27-9.rev2363
- Add s390x as 64-bit arch

* Sat Jan 29 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-8.rev2363
- Fix 3D view crash with some graphics cards (BZ #664143).

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 2010.05.27-7.rev2363
- rebuilt against wxGTK-2.8.11-2

* Tue Jun 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-6
- Fix some module edition issues (https://bugs.launchpad.net/kicad/+bug/593546,
  https://bugs.launchpad.net/kicad/+bug/593547)

* Fri Jun 11 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-5
- Fix a crash in searching string (https://bugs.launchpad.net/kicad/+bug/592566)

* Tue Jun  8 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-4
- Fix a focus issue (https://bugs.launchpad.net/kicad/+bug/587970)
- Fix an unwanted mouse cursor move when using the t hotkey in pcbnew
- Fix an issue on arcs draw in 3D viewer (https://bugs.launchpad.net/kicad/+bug/588882)

* Mon May 31 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-3
- Fix an undo-redo issue (https://bugs.launchpad.net/kicad/+bug/586032)

* Sun May 30 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-2
- Don't forget icons

* Sat May 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-1
- New packager version
- Update kicad version number patch
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587175
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587176

* Fri May 21 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-3
- Fix the kicad version number
- Fix a problem when trying to modify a footprint value in eeschema
  https://bugs.launchpad.net/kicad/+bug/583939

* Tue May 18 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-2
- No backup of patched files to deleted
- Add noreplace flag to config macro

* Mon May 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-1
- New upstream version
- All previous patches no more needed
- Backward to cmake 2.6 requirement

* Sun May  9 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.05-1
- New upstream version
- All previous patches no more needed
- Fix url: KiCad move from SourceForge.net to LaunchPad.net
- Remove vendor tag from desktop-file-install
- Add x-kicad-pcbnew mimetype
- Add new icons for mimetype

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-9.rev2515
- Fix a minor bug that occurs when changing module orientation or side

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-8.rev2515
- Auto update 3D viewer: fix https://bugs.launchpad.net/kicad/+bug/571089
- Create png from screen (libedit): fix https://bugs.launchpad.net/kicad/+bug/573833

* Sun May  2 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-7.rev2515
- Rename COTATION class (french word) in DIMENSION and fix
  https://bugs.launchpad.net/kicad/+bug/568356 and https://bugs.launchpad.net/kicad/+bug/568357
- Some code cleaning ans enhancements + fix a bug about last netlist file used (LP #567902)

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-6.rev2515
- Make cleanup feature undoable, fix https://bugs.launchpad.net/kicad/+bug/564619
- Fix issues in SVG export, fix https://bugs.launchpad.net/kicad/+bug/565388
- Minor pcbnew enhancements
- Fix minor gerber problems, fix https://bugs.launchpad.net/kicad/+bug/567881

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-5.rev2515
- DRC have to use the local parameters clearance if specified,
  and NETCLASS value only if no local value specified. 

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-4.rev2514
- Fix https://bugs.launchpad.net/bugs/568896 and https://bugs.launchpad.net/bugs/569312

* Thu Apr 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-3.rev2514
- Fix a crash that happens sometimes when opening the design rule dialog

* Mon Apr 26 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-2.rev2514
- Fix https://bugs.launchpad.net/bugs/570074

* Mon Apr 12 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-1.rev2514
- New upstream version
- Patches no more needed

* Mon Apr  5 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-5.rev2463
- Add patch to fix SF #2981759

* Sat Apr  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-4.rev2463
- Apply upstream patch to fix inch/mm ratio
- Provide a source download URL

* Wed Mar 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-3.rev2463
- Patch with svn revision 2463 which fix 2 bugs
- Harmonize identation in %%changelog

* Tue Mar 16 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2010.03.14-2.rev2462
- Link fixes. Really, these libraries should be linked properly so they don't need
  the executable linking calls to be explicitly correct, but cmake gives me a headache.
- Fix demo installation

* Mon Mar 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-1.rev2462
- New upstream version

* Mon Aug 24 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-4.rev1863
- Multilib path correction, BZ 518916.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.07.07-3.rev1863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-2.rev1863
- Dropped eeschema desktop file.
- Moved English kicad.pdf to main rpm.
- Added ls.so.conf file and ldconfig to post, postun to fix libs issue.
- Dropped category Development from desktop file.

* Tue Jul 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2009.07.07-1.rev1863
- svn rev 1863
- documentation splitted into multiple packages
- libraries are now taken directly from SVN rather than from older releases
- build changed to cmake based

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007.07.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2007.07.09-4
- First patch is Patch0 - should fix build in Rawhide.
- Include %%_libdir/kicad directory.
- Drop explicit Requires wxGTK in favour of automatic SONAME dependencies.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2007.07.09-3
- Autorebuild for GCC 4.3

* Mon Oct 15 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-2
  - Update desktop file

* Thu Oct 04 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-1
- New upstream version
- Merge previous patches
- Remove X-Fedora, Electronics and Engineering categories
- Update desktop file

* Mon Aug 27 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-4
- License tag clarification

* Thu Aug 23 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-3
- Rebuild

* Wed Feb 14 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-2
- Fix desktop entry. Fix #228598

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-1
- New upstream version

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-4
- Add patch to build with RPM_OPT_FLAGS and remove -s from LDFLAGS
  Contribution of Ville Skyttä <ville[DOT]skytta[AT]iki[DOT]fi>
  Fix #227757
- Fix typo in french summary

* Thu Dec 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> 2006.08.28-3
- Rebuild with wxGTK 2.8.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2006.08.28-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-1
- New upstream version
- Use macro style instead of variable style
- Install missing modules. Fix #206602

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-6
- FE6 rebuild

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-5
- Removing backup files is no more needed.

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-4
- Remove BR libGLU-devel that is no more needed (bug #197501 is closed)
- Fix files permissions.

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-3
- s/mesa-libGLU-devel/libGLU-devel/

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-2
- BR mesa-libGLU-devel

* Wed Jun 28 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-1
- New upstream version

* Tue Jun 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.04.24-5
- Change name
- Use %%{_docdir} instead of %%{_datadir}/doc
- Use %%find_lang
- Update desktop database
- Convert MSDOS EOL to Unix EOL
- Remove BR utrac

* Mon Jun 12 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-4
- Patch to suppress extra qualification compile time error on FC5
- BR utrac to convert MSDOS files before applying patch
  This will be remove for the next upstream version.

* Tue May 23 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-3
- Install help in /usr/share/doc/kicad/ as the path is hardcoded in gestfich.cpp
- Add desktop file

* Mon May 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-2
- Add a second tarball that contains many things that are not included in
  the upstream source tarball such components and footprints librairies,
  help, localisation, etc.

* Sun May 21 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-1
- Initial Fedora RPM
