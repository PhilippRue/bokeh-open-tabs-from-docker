#!/bin/bash -e

# This script is executed whenever the docker container is (re)started.

#===============================================================================
# debuging
set -x

#===============================================================================

# now serve the app (uses bokeh server in the background)
panel serve test-app/app1 test-app/app2 \
    --port 5007                 \
    --log-level debug           \
    --allow-websocket-origin "*" \
    --use-xheaders

#===============================================================================

#EOF
