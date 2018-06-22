"""
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A. For more details read 'Read Me.txt' given with this software.
Created by		: Falagas Alexandros, S.R.S.E - N.T.U.A, 16/06/2017
E-mail			: alek.falagas@gmail.com
Latest update	: 23/06/2018
Version			: Version 0.0.4 | Sen2Cor version 2.5.5

"""

import os
from os import walk
import fnmatch
import subprocess
import time
import getpass

cwd=os.getcwd()
print 'Current Working Directory:',cwd
username = getpass.getuser()
print username
im=0
starttime=time.time()
for (dirpath, dirnames, filenames) in walk(cwd):
	for file in os.listdir(dirpath):
		if fnmatch.fnmatch(str(file), '*.SAFE'):
			im=im+1
			print "Sentinel 2 Data found:",dir
			cmd='/home/{}/Sen2Cor-02.05.05-Linux64/bin/L2A_Process {}/{}'.format(str(username),str(dirpath),str(file)) # You can set Sen2Cor resolution by adding after L2A_Process --resolution=60 for 60m or 20 for 20m or 10 for 10m. By default resolution is all.
			print "Running...", cmd
			os.system(cmd)
elapsedtime=time.time()-starttime
mins, secs = divmod(elapsedtime, 60)
hours, mins = divmod(mins, 60)
image='image'
if im>1:
	image="images"
print "S.A.C algorithm completed for:", im, image, "in: {}:{}:{}".format(int(hours), int(mins), round(secs,2))
