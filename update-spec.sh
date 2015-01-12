#!/bin/sh

get_last_rev()
{
 cd $1
 bzr log | head -2 | tail -1 | cut -d\  -f 2
 cd ..
}


KICAD_REV=$(get_last_rev kicad.bzr)

sed s/REVISION_NUMBER/$KICAD_REV/g kicad.spec.template > kicad.spec
md5sum *.xz > sources

