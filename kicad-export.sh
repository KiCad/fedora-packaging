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
#LIB_REV=$(get_last_rev kicad-library.bzr)
#DOC_REV=$(get_last_rev kicad-doc.bzr)
TIMESTAMP="$MAIN_REV"

cd kicad.bzr
echo "Creating kicad-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-$TIMESTAMP/ HEAD > ../kicad-$TIMESTAMP.tar.gz
#bzr export kicad-$TIMESTAMP
#echo "Creating kicad-$TIMESTAMP.tar.xz ..."
#tar cJf ../kicad-$TIMESTAMP.tar.xz kicad-$TIMESTAMP
#rm -rf kicad-$TIMESTAMP

cd ../kicad-symbols.bzr
echo "Creating kicad-symbols-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-symbols-$TIMESTAMP/ HEAD > ../kicad-symbols-$TIMESTAMP.tar.gz

cd ../kicad-footprints.bzr
echo "Creating kicad-footprints-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-footprints-$TIMESTAMP/ HEAD > ../kicad-footprints-$TIMESTAMP.tar.gz

cd ../kicad-packages3D.bzr
echo "Creating kicad-packages3D-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-packages3D-$TIMESTAMP/ HEAD > ../kicad-packages3D-$TIMESTAMP.tar.gz

cd ../kicad-templates.bzr
echo "Creating kicad-templates-$TIMESTAMP.tar.gz ..."
git archive --format=tar.gz --prefix=kicad-templates-$TIMESTAMP/ HEAD > ../kicad-templates-$TIMESTAMP.tar.gz

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
