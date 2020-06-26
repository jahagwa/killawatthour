#/usr/bin/python3.8

#Required to use commands that are OS dependent
import os

#Required to get $USER
import getpass

#Setting Variable for $USER
USER = getpass.getuser()

#This gets the current $USER and tests to see if they have a .bashrc file in their home directory.

if os.path.isfile('/home/'+ USER +'/.bashrc'):
    print('Your .bashrc file exists.')
else:
    print('Your .bashrc file doesn\'t exist')