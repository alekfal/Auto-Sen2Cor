
"""
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A. This script
works with anaconda and Sen2Cor algorithm, so they must be installed in your computer. For more details read 'Read Me.txt' given with this software.
Created by	: Falagas Alexandros
E-mail		: alek.falagas@gmail.com
Begin		: S.R.S.E - N.T.U.A, 16/06/2017
Version		: Version 0.0.3

Run this script under the umbrella of Anaconda.
Known issues:
1.Spaces cause problem to Sen2Cor algorithm. Please avoid using spaces in the absolute path to images.
2.The processor is able to perform a 10 m image without background pixels (a full scene) with a memory of about 6 GB. Below the value of 6GB it might work, but this is dependent on the amount of existing non background pixels. The reason for this huge memory consumption is the fact, that for some of the atmospheric calculations (AOT) a collection of full arrays of size 10.000 x 10.000 must be kept in memory, as otherwise artifacts due to tiling will occur.
"""

import os
from os import walk
import fnmatch
import subprocess
import time

cwd=os.getcwd()
print 'Current Working Directory:',cwd
username=os.system("whoami")
os.system("export SEN2COR_HOME=/home/{}/sen2cor".format(username))
os.system("export SEN2COR_BIN=/home/{}/anaconda2/lib/python2.7/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor".format(username))
os.system("export GDAL_DATA=/home/{}/anaconda2/lib/python2.7/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor/cfg/gdal_data".format(username)
im=0
starttime=time.time()
for (dirpath, dirnames, filenames) in walk(cwd):
	for file in os.listdir(dirpath):
		if fnmatch.fnmatch(str(file), '*.SAFE'):
			im=im+1
			print "Sentinel 2 Data found:",dir
		cmd=str("L2A_Process "+str(dirpath)+"/"+str(file)) # You can set Sen2Cor resolution by adding after L2A_Process --resolution=60 for 60m or 20 for 20m or 10 for 10m. By default resolution is all.
		print "Running...", cmd
		os.system(cmd)
elapsedtime=time.time()-starttime
mins, secs = divmod(elapsedtime, 60)
hours, mins = divmod(mins, 60)
image='image'
if im>1:
	image="images"
print "S.A.C algorithm completed for:", im, image, "in: {}:{}:{}".format(int(hours), int(mins), round(secs,2))
