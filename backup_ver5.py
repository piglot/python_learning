#!/age:\sr/bin/python
# Filename: backup_ver3.py
# This program could not work, for too long name with no '\'

import os
import time
import sys

# 1. The files and directories to be backed up are specified in a list.
source = []
source = sys.argv[1:]
print 'source list is', source
if len(source) == 0:
	print 'Error !!!\nUsage:\n	python backup_ver5.py [source_list] '

# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/home/backup/' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
	target = target_dir + today + '_' + now + '.tar'
else:
#	target = today + os.sep + now + '_' +\
#	comment.replace(' ', '_') + '.zip'
	dir =  target_dir + comment.replace(' ', '_')
	target = dir + os.sep + today + '_' +\
	now + '.tar'

mkdir_command = "mkdir -p %s" % dir
os.system(mkdir_command)
# Create the subdirectory if it isn't already there
#if not os.path.exists(dir):
#	os.mkdir(dir) # make directory
#	print 'Successfully created directory', dir

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
tar_command = 'tar -cvzf %s %s ' % (target, ' '.join(source))

# Run the backup
if os.system(tar_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
