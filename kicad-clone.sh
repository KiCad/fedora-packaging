#!/bin/sh
set -e
set -x
if [ -d kicad.bzr ]; then
	cd kicad.bzr
	bzr update 
	cd ..
else 
	bzr checkout lp:kicad kicad.bzr
fi

if [ -d kicad-library.bzr ]; then
	cd kicad-library.bzr
	bzr update 
	cd ..
else
	bzr checkout lp:~kicad-product-committers/kicad/library kicad-library.bzr
fi

if [ -d kicad-i18n ]; then
    cd kicad-i18n
    git pull
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


exit 0

sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p'  kicad-library.bzr/template/fp-lib-table.for-github > footprint.list

mkdir -p footprints
cat footprint.list |while read FP
	do
		git clone https://github.com/KiCad/$FP footprints/$FP ||
			print "$FP missing, possibly gone from GitHub now"
	done


