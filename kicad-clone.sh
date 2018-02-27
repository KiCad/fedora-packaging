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

if [ -d kicad-symbols.bzr ]; then
	cd kicad-symbols.bzr
	git fetch origin
	git reset --hard origin/master
	cd ..
else
	git clone https://github.com/KiCad/kicad-symbols.git kicad-symbols.bzr
fi

if [ -d kicad-footprints.bzr ]; then
	cd kicad-footprints.bzr
	git fetch origin
	git reset --hard origin/master
	cd ..
else
	git clone https://github.com/KiCad/kicad-footprints.git kicad-footprints.bzr
fi

if [ -d kicad-packages3D.bzr ]; then
	cd kicad-packages3D.bzr
	git fetch origin
	git reset --hard origin/master
	cd ..
else
	git clone https://github.com/KiCad/kicad-packages3D.git kicad-packages3D.bzr
fi

if [ -d kicad-templates.bzr ]; then
	cd kicad-templates.bzr
	git fetch origin
	git reset --hard origin/master
	cd ..
else
	git clone https://github.com/KiCad/kicad-templates.git kicad-templates.bzr
fi

if [ -d kicad-i18n ]; then
	cd kicad-i18n
	git fetch origin
	git reset --hard origin/master
	cd ..
else
	git clone https://github.com/KiCad/kicad-i18n.git
fi

#TODO(mangelajo): pull the new doc builds
#if [ -d kicad-doc.bzr ]; then
#	cd kicad-doc.bzr
#	bzr update 
#	cd ..
#else
#	bzr branch --stacked lp:~kicad-developers/kicad/doc kicad-doc.bzr
#fi
