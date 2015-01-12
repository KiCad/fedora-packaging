#!/bin/sh
set -e
set -x
get_last_rev()
{
 cd $1 
 bzr log | head -2 | tail -1 | cut -d\  -f 2
 cd ..
}

TIMESTAMP="nightlies"
MAIN_REV=$(get_last_rev kicad.bzr)
LIB_REV=$(get_last_rev kicad-library.bzr)
DOC_REV=$(get_last_rev kicad-doc.bzr)

cd kicad.bzr
rm -rf kicad-$TIMESTAMP
bzr export kicad-$TIMESTAMP
echo "Creating kicad-$TIMESTAMP.tar.xz ..."
tar cJf ../kicad-$TIMESTAMP.tar.xz kicad-$TIMESTAMP
rm -rf kicad-$TIMESTAMP

cd ../kicad-library.bzr
rm -rf kicad-libraries-$TIMESTAMP
bzr export kicad-libraries-$TIMESTAMP
echo "Creating kicad-libraries-$TIMESTAMP.tar.xz ..."
tar cJf ../kicad-libraries-$TIMESTAMP.tar.xz kicad-libraries-$TIMESTAMP
rm -rf kicad-libraries-$TIMESTAMP

cd ../kicad-doc.bzr
rm -rf kicad-doc-$TIMESTAMP
bzr export kicad-doc-$TIMESTAMP
echo "Creating kicad-doc-$TIMESTAMP.tar.xz ..."
tar cJf ../kicad-doc-$TIMESTAMP.tar.xz kicad-doc-$TIMESTAMP
rm -rf kicad-doc-$TIMESTAMP
cd ..

exit 0


cd footprints
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
rm -rf kicad-footprints-$TIMESTAMP
cd ..
