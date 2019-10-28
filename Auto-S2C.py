"""
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A. For more details read 'Read Me.txt' given with this software.
Created by		: Falagas Alexandros, S.R.S.E - N.T.U.A, 16/06/2017
E-mail			: alek.falagas@gmail.com
Latest update	: 28/09/2019
Version			: Version 0.0.5 | Sen2Cor version 02.08.00

"""

import os
from os import walk
import sys
import fnmatch
import subprocess
import time
import getpass

cwd=os.getcwd()
print ('Current Working Directory: {}'.format(cwd))
username = getpass.getuser()
print ('Username:{}'.format(username))
images = 0
starttime = time.time()
print ('Starting searching to the tree of folders...')
for (dirpath, dirnames, filenames) in walk(cwd):
	for file in os.listdir(dirpath):
		if fnmatch.fnmatch(str(file), '*.SAFE'):
			images = images + 1
			print ("Raw data found (*.SAFE files): {}".format(str(file)))
			if sys.platform.startswith('windows'):
				# On Windows x64. NOT TESTED!
				sentinelfile = os.path.join(dirpath,str(file))
				cmd = 'C:\\Users\\{}\\AppData\\Local\\Sen2Cor-02.08.00-win64\\L2A_Process.bat {}'.format(username,sentinelfile)
				os.system(cmd)
			elif sys.platform.startswith('linux'):
				sentinelfile = os.path.join(dirpath,str(file))
				# Works only if Sen2Cor is installed to home folder! In other case replace the correct path to Sen2Cor.
				cmd='/home/{}/Sen2Cor-02.08.00-Linux64/bin/L2A_Process {}'.format(username,sentinelfile) # You can set Sen2Cor resolution by adding after L2A_Process --resolution=60 for 60m or 20 for 20m or 10 for 10m. By default resolution is all.
				print ("Running...", cmd)
				os.system(cmd)
elapsedtime=time.time()-starttime
mins, secs = divmod(elapsedtime, 60)
hours, mins = divmod(mins, 60)
if images == 1:
	image = 'image'
else:
	image = "images"

print ("Algorithm completed for:", images, image, "in: {}:{}:{}".format(int(hours), int(mins), round(secs,2)))
