#!/bin/sh
set -x
set -e

SRPM_FILE=$(fedpkg srpm | grep Wrote | cut -d\  -f 2)
scp $SRPM_FILE mangelajo@fedorapeople.org:~/public_html/copr/
SRPM_FILENAME=$(basename $SRPM_FILE)
copr-cli build kicad https://mangelajo.fedorapeople.org/copr/$SRPM_FILENAME

