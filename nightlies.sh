#!/bin/sh
set -e
set -x

WORKSPACE_URL=$1
./kicad-clone.sh
./kicad-export.sh
./update-spec.sh
./srpm-to-copr.sh $WORKSPACE_URL

