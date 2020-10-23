#!/usr/bin/env python3

from lssh.databasemgmt import *
# Changing folder to the same folder as the server runs in. For images
# and such to appear in the right place.
os.chdir('lssh')
resetDB()
fillTestDB()
