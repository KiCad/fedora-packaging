#!/bin/sh
set -x
set -e

WORKSPACE_URL=$1

SRPM_FILE=$(fedpkg --dist master srpm | grep Wrote | cut -d\  -f 2)
SRPM_FILENAME=$(basename $SRPM_FILE)
if [ "$( whoami )" == "jenkins" ]; then
        SRPM_URL="$WORKSPACE_URL$SRPM_FILENAME"	
else
        scp $SRPM_FILE mangelajo@fedorapeople.org:~/public_html/copr/
        SRPM_URL="https://mangelajo.fedorapeople.org/copr/$SRPM_FILENAME"
fi

set +x
echo starting the remote copr build, check the waiting queue here:
echo https://copr.fedoraproject.org/status/waiting/
echo and the status of the build, here:
echo https://copr.fedoraproject.org/coprs/mangelajo/kicad/builds/ 
set -x

copr-cli build @kicad/kicad $SRPM_URL

set +x
echo DONE, check installation instructions here: 
echo     https://copr.fedoraproject.org/coprs/mangelajo/kicad/
