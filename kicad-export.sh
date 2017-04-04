#!/bin/sh
set -e
set -x
get_last_rev()
{
 cd $1 
 printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
 cd ..
}

MAIN_REV=$(get_last_rev kicad.bzr)
LIB_REV=$(get_last_rev kicad-library.bzr)
#DOC_REV=$(get_last_rev kicad-doc.bzr)
TIMESTAMP="$MAIN_REV"

cd kicad.bzr
echo "Creating kicad-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-$TIMESTAMP/ HEAD > ../kicad-$TIMESTAMP.tar.gz
#bzr export kicad-$TIMESTAMP
#echo "Creating kicad-$TIMESTAMP.tar.xz ..."
#tar cJf ../kicad-$TIMESTAMP.tar.xz kicad-$TIMESTAMP
#rm -rf kicad-$TIMESTAMP

cd ../kicad-library.bzr
echo "Creating kicad-libraries-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-libraries-$TIMESTAMP/ HEAD > ../kicad-libraries-$TIMESTAMP.tar.gz


cd ../kicad-i18n
echo "Creating kicad-i18n-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-i18n-$TIMESTAMP/ HEAD > ../kicad-i18n-$TIMESTAMP.tar.gz

#TODO(mangelajo): new docs?
#cd ../kicad-doc.bzr
#rm -rf kicad-doc-$TIMESTAMP
#bzr export kicad-doc-$TIMESTAMP
#echo "Creating kicad-doc-$TIMESTAMP.tar.xz ..."
#tar cJf ../kicad-doc-$TIMESTAMP.tar.xz kicad-doc-$TIMESTAMP
#rm -rf kicad-doc-$TIMESTAMP
#cd ..

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
