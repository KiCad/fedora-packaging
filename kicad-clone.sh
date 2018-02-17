#!/bin/sh
set -e
set -x
if [ -d kicad.bzr ]; then
	cd kicad.bzr
	git fetch origin
	git reset --hard origin/master
	cd ..
else 
	git clone https://git.launchpad.net/kicad kicad.bzr
fi

if [ -d kicad-library.bzr ]; then
	cd kicad-library.bzr
	git fetch origin
	git reset --hard origin/master
	cd ..
else
	git clone https://github.com/KiCad/kicad-library.git kicad-library.bzr
fi

if [ -d kicad-i18n ]; then
    cd kicad-i18n
    git fetch origin
    git reset --hard origin/master
    cd ..
else
    git clone https://github.com/KiCad/kicad-i18n.git
fi

if [ -d kicad-footprints ]; then
    cd kicad-footprints
    git fetch origin
    git reset --hard origin/master
    cd ..
else
    git clone https://github.com/KiCad/kicad-footprints.git
fi

#TODO(mangelajo): pull the new doc builds
#if [ -d kicad-doc.bzr ]; then
#	cd kicad-doc.bzr
#	bzr update 
#	cd ..
#else
#	bzr branch --stacked lp:~kicad-developers/kicad/doc kicad-doc.bzr
#fi
