#!/bin/sh
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
cd ..
