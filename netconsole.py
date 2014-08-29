#!/usr/bin/python
# Filename: netconsole.sh

import time
import sys
import os

today = time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
	print 'Please input a comment !\n'

dir = '/home/netconsole_log/' + comment.replace(' ','_') + '/' 
file_path = dir  + today + '_' + now + '.log'

mkdir_command = "mkdir -p %s" % dir 
if os.system(mkdir_command) == 0:
	print 'Successfully created directory', dir
#if not os.path.exists(dir):
#	os.mkdir(dir)     #make directory
#	print 'Successfully created directory', dir

#nc -l -u  6666 | tee /home/netconsole_log/netconsola_'date +%D_%T'.log
#nc_command = "nc -l -u 6666 | tee  /home/netconsole_log/netconsole_`date +%Y_%m_%d_%T`.log"
nc_command = "nc -l -u 6666 | tee %s " % file_path
if os.system(nc_command) == 0:
	print 'Success load remote netconsole server !\nLog file will be in /home/'
