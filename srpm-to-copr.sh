#!/bin/sh
set -x
set -e

SRPM_FILE=$(fedpkg --dist master srpm | grep Wrote | cut -d\  -f 2)
SRPM_FILENAME=$(basename $SRPM_FILE)
if [ "$( whoami )"=="jenkins" ]; then
        copr-cli build kicad http://ci.kicad-pcb.org/job/fedora-nightlies/ws/$SRPM_FILENAME
else
        scp $SRPM_FILE mangelajo@fedorapeople.org:~/public_html/copr/
        copr-cli build kicad https://mangelajo.fedorapeople.org/copr/$SRPM_FILENAME
fi
