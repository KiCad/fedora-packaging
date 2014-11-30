#!/bin/sh
set -e

TIMESTAMP="2014.03.13"
MAIN_REV=4744
LIB_REV=333
DOC_REV=560

cd kicad.bzr
bzr export -r $MAIN_REV kicad-$TIMESTAMP
echo "Creating kicad-$TIMESTAMP.tar.xz ..."
tar cJf kicad-$TIMESTAMP.tar.xz kicad-$TIMESTAMP
cd ../kicad-library.bzr
bzr export -r $LIB_REV kicad-libraries-$TIMESTAMP
echo "Creating kicad-libraries-$TIMESTAMP.tar.xz ..."
tar cJf kicad-libraries-$TIMESTAMP.tar.xz kicad-libraries-$TIMESTAMP
cd ../kicad-doc.bzr
bzr export -r $DOC_REV kicad-doc-$TIMESTAMP
echo "Creating kicad-doc-$TIMESTAMP.tar.xz ..."
tar cJf kicad-doc-$TIMESTAMP.tar.xz kicad-doc-$TIMESTAMP
cd ../footprints
echo "Creating kicad-footprints-$TIMESTAMP.tar.xz ..."
rm -rf kicad-footprints-$TIMESTAMP
mkdir -p kicad-footprints-$TIMESTAMP
>kicad-footprints-$TIMESTAMP/VERSIONS.footprints
sed -n 's|.*\${KIGITHUB}/\([^)]*\)).*|\1|p' \
	../kicad-library.bzr/kicad-libraries-$TIMESTAMP/template/fp-lib-table.for-github |
	while read FP
	do
		if [ -d $FP ]
		then
			cd $FP
			REV=$(git rev-list -n 1 --before="$TIMESTAMP" master)
			if [ -z $REV ]
			then
				echo "$FP did not exist at $TIMESTAMP!"
				REV=$(git rev-list -n 1 master)
			fi
			git archive --prefix=$FP/ $REV |tar xf - -C ../kicad-footprints-$TIMESTAMP
			echo $FP $REV >>../kicad-footprints-$TIMESTAMP/VERSIONS.footprints
			cd ..
		else
			echo "$FP missing now. Update libraries snapshot or patch it away from fp-lib-table!"
		fi
	done
tar -cJf kicad-footprints-$TIMESTAMP.tar.xz kicad-footprints-$TIMESTAMP
cd ..
