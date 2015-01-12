#!/bin/sh
set -e
set -x
./kicad-clone.sh
./kicad-export.sh
./update-spec.sh
./srpm-to-copr.sh

