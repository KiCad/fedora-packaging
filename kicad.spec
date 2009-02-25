Name: 		kicad
Version:	2007.07.09
Release:	5%{?dist}
Summary: 	Electronic schematic diagrams and printed circuit board artwork
Summary(fr): 	Saisie de schéma électronique et tracé de circuit imprimé

Group: 		Applications/Engineering
License: 	GPLv2+
Url: 		http://www.lis.inpg.fr/realise_au_lis/kicad/
Source:		ftp://iut-tice.ujf-grenoble.fr/cao/sources/kicad-sources--2007-07-09.zip
Source1:	http://linuxelectronique.free.fr/download/kicad-src-extras-2007-07-09.tar.bz2
Source2:	%{name}.desktop
Patch0:		%{name}-%{version}.destdir.locale.rpmoptflags.diff
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	desktop-file-utils, wxGTK-devel

%description
Kicad is an open source (GPL) software for the creation of electronic schematic
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

%prep
%setup -q -n kicad-dev -a 1
%{__cp} -a kicad-src-extras-2007-07-09/* .
%{__rm} -rf kicad-src-extras-2007-07-09

# Convert MSDOS EOL to Unix EOL before applying patches

for f in 3d-viewer/{3d_struct.h,3d_viewer.h} \
eeschema/libcmp.h \
include/{pcbstruct.h,wxstruct.h} \
kicad/kicad.h \
pcbnew/{autorout.h,class_cotation.h,class_equipot.h,class_mire.h,class_module.h,class_pcb_text.h,class_text_mod.h,class_track.h,track.cpp}
do
  %{__sed} -i -e 's/\r$//' $f
done

%patch0 -p1

%build

# These files are not scripts
for f in {copyright,gpl,licendoc,version}.txt
do
  %{__chmod} -x $f
done

# Convert MSDOS EOL to Unix EOL
for f in {author,contrib,copyright,doc_conv_orcad*,gpl,licendoc}.txt
do
  %{__sed} -i -e 's/\r$//' $f
done

for f in help/fr/{contents.hhc,kicad.hhp,cvpcb/cvpcb-fr.html,eeschema/eeschema.html,eeschema/eeschema.pdf,file_formats/file_formats.html,gerbview/gerbview.html,kicad/kicad.html,pcbnew/pcbnew.html}
do
  %{__sed} -i -e 's/\r$//' $f
done

for f in help/en/{contents.hhc,kicad.hhp,cvpcb/cvpcb-en.html,eeschema/eeschema.html,file_formats/file_formats.html,gerbview/gerbview.html,kicad/kicad.html,pcbnew/pcbnew.html}
do
  %{__sed} -i -e 's/\r$//' $f
done

for f in help/es/{contents.hhc,kicad.hhp,cvpcb/cvpcb-es.html,eeschema/eeschema-es.html,file_formats/file_formats-es.html,gerbview/gerbview.html,kicad/kicad-es.html,pcbnew/pcbnew-es.html}
do
  %{__sed} -i -e 's/\r$//' $f
done

for f in help/pt/{contents.hhc,kicad.hhp,cvpcb/cvpcb-pt.html,eeschema/eeschema-pt.html,eeschema/eeschema_pt_BR.html,file_formats/file_formats.html,gerbview/gerbview.html,kicad/kicad_pt_BR.html,kicad/kicad-pt.html,pcbnew/pcbnew.html,pcbnew/pcbnew_pt_BR.html}
do
  %{__sed} -i -e 's/\r$//' $f
done

for f in help/ru/{contents.hhc,kicad.hhp,eeschema/eeschema_ru.html}
do
  %{__sed} -i -e 's/\r$//' $f
done

make -f makefile.gtk %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_datadir}/%{name}

# install demos files
install -d %{buildroot}%{_datadir}/%{name}/demos
for dir in electric interf_u microwave pic_programmer pspice sonde_xilinx test_xil_95108 video
do
  install -d %{buildroot}%{_datadir}/%{name}/demos/${dir}
  for f in demos/${dir}/*
  do
    install -m 644 ${f} %{buildroot}%{_datadir}/%{name}/${f}
  done
done

# install help files
install -d %{buildroot}%%{_docdir}
install -d %{buildroot}%{_docdir}/%{name}/
for dir in en es fr pt
do
  install -d %{buildroot}%{_docdir}/%{name}/${dir}
  for subdir in cvpcb eeschema file_formats gerbview kicad pcbnew
  do
    install -d %{buildroot}%{_docdir}/%{name}/${dir}/${subdir}
    cd help
    install -m 644 ${dir}/kicad.hhp %{buildroot}%{_docdir}/%{name}/${dir}/kicad.hhp
    install -m 644 ${dir}/contents.hhc %{buildroot}%{_docdir}/%{name}/${dir}/contents.hhc
    for f in ${dir}/${subdir}/*
    do
      install -m 644 ${f} %{buildroot}%{_docdir}/%{name}/${f}
    done
    cd ..
  done
done

# install ru help files
install -d %{buildroot}%%{_docdir}
install -d %{buildroot}%{_docdir}/%{name}/
for dir in ru
do
  install -d %{buildroot}%{_docdir}/%{name}/${dir}
  for subdir in eeschema pcbnew
  do
    install -d %{buildroot}%{_docdir}/%{name}/${dir}/${subdir}
    cd help
    install -m 644 ${dir}/kicad.hhp %{buildroot}%{_docdir}/%{name}/${dir}/kicad.hhp
    install -m 644 ${dir}/contents.hhc %{buildroot}%{_docdir}/%{name}/${dir}/contents.hhc
    for f in ${dir}/${subdir}/*
    do
      install -m 644 ${f} %{buildroot}%{_docdir}/%{name}/${f}
    done
    cd ..
  done
done

# install librairies
install -d %{buildroot}%{_datadir}/%{name}/library
for f in library/*
do
  install -m 644 ${f} %{buildroot}%{_datadir}/%{name}/${f}
done

# install localization
install -d %{buildroot}%{_datadir}/locale
cd locale
for dir in de es fr hu it ko pl pt sl
do
  install -d %{buildroot}%{_datadir}/locale/${dir}
  install -m 644 ${dir}/%{name}.mo %{buildroot}%{_datadir}/locale/${dir}/%{name}.mo
done
cd ..

# install modules
install -d %{buildroot}%{_datadir}/%{name}/modules
install -d %{buildroot}%{_datadir}/%{name}/modules/packages3d
for dir in conn_DBxx connectors conn_europe device dil discret divers pga pin_array smd support
do
  install -d %{buildroot}%{_datadir}/%{name}/modules/packages3d/${dir}
  for f in modules/packages3d/${dir}/*
  do
    install -m 644 ${f} %{buildroot}%{_datadir}/%{name}/${f}
  done
done
for f in modules/*.*
do
  install -m 644 ${f} %{buildroot}%{_datadir}/%{name}/${f}
done


# install template
install -d %{buildroot}%{_datadir}/%{name}/template
install -m 644 template/%{name}.pro %{buildroot}%{_datadir}/%{name}/template

# install binaries
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}/%{name}/plugins
make -f makefile.gtk install DESTDIR=%{buildroot}

# install desktop
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor=fedora \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# install icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 kicad_icon.png %{buildroot}%{_datadir}/pixmaps/kicad_icon.png

%find_lang %{name}

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]
then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%postun
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]
then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc author.txt contrib.txt copyright.txt doc_conv_orcad_to_kicad_spanish.txt
%doc doc_conv_orcad_to_kicad.txt gpl.txt licendoc.txt news.txt version.txt
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugins/
%{_datadir}/%{name}/
%{_docdir}/%{name}/
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/pixmaps/kicad_icon.png

%changelog
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
  - Install help in /usr/share/doc/kicad/ as the path is hardcoded
    in gestfich.cpp
  - Add desktop file

* Mon May 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-2
  - Add a second tarball that contains many things that are not included in
    the upstream source tarball such components and footprints librairies,
    help, localisation, etc.

* Sun May 21 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-1
  - Initial Fedora RPM
