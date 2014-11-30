#!/bin/sh
set -e

fps () { sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p' \
	kicad-library.bzr/template/fp-lib-table.for-github \
	kicad-library.bzr/kicad-libraries-*/template/fp-lib-table.for-github
}

# Deleted footprints
(fps; fps; ls footprints) |sort |uniq -u |while read FP
do
	rm -r footprints/$FP
done

# Update existing ones
fps |while read FP
do
	if [ -d footprints/$FP ]
	then
		cd footprints/$FP
		git pull
		cd ../..
	else
		git clone https://github.com/KiCad/$FP footprints/$FP ||
			print "$FP missing, possibly gone from GitHub now"
	fi
done
