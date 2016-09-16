#!/bin/sh

get_last_rev()
{
 cd $1
 printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
 cd ..
}


KICAD_REV=$(get_last_rev kicad.bzr)

sed s/REVISION_NUMBER/$KICAD_REV/g kicad.spec.template > kicad.spec
md5sum *.gz > sources

