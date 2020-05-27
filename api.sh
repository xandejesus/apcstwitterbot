#!/usr/bin/env sh

######################################################################
# @author      : xander (xander@DESKTOP-F49A7DE)
# @file        : api
# @created     : Tuesday May 26, 2020 13:53:38 PDT
#
# @description : 
######################################################################
./reset.sh
# u have to manually run this because it is not working.
export GOOGLE_APPLICATION_CREDENTIALS=~fun/creds.json
python3 api.py

