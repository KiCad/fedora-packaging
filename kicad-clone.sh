#!/bin/sh
set -e

bzr checkout lp:kicad kicad.bzr
bzr checkout lp:~kicad-product-committers/kicad/library kicad-library.bzr
bzr branch --stacked lp:~kicad-developers/kicad/doc kicad-doc.bzr

fps () { sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p'  kicad-library.bzr/template/fp-lib-table.for-github }

mkdir -p footprints
fps |while read FP
	do
		git clone https://github.com/KiCad/$FP footprints/$FP ||
			print "$FP missing, possibly gone from GitHub now"
	done
