"""
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A. For more details read 'Read Me.txt' given with this software.
Created by		: Falagas Alexandros, S.R.S.E - N.T.U.A, 16/06/2017
E-mail			: alek.falagas@gmail.com
Latest update	: 31/10/2019
Version			: Version 0.0.7 | Sen2Cor version 02.09.00

"""

import os
from os import walk
import sys
import fnmatch
import subprocess
import time
import getpass
from optparse import OptionParser

if __name__ == "__main__":


	# Parsing argument resolution. Output resolution must be either 10, 20 ,60. Default option is all.
	parser = OptionParser()
	parser.add_option("-r", "--resolution", dest = "resolution", help = "Output resolution of Sen2Cor.", default = None, type = "int")
	(options, args) = parser.parse_args()
	if options.resolution == None:
		print ('Output resolution is all.')
		resolution = None
	elif options.resolution == 10:
		print ('Output resolution is 10 meters.')
		resolution = 10
	elif options.resolution == 20:
		print ('Output resolution is 20 meters.')
		resolution = 20
	elif options.resolution == 60:
		print ('Output resolution is 60 meters.')
		resolution = 60
	else:
		# Raise error if the parsed argument is wrong.
		raise ValueError("Output resolution must be either 10, 20 ,60. Default option is all.")

	# Getting working directory
	cwd=os.getcwd()
	print ('Current Working Directory: {}'.format(cwd))
	# Getting username
	username = getpass.getuser()
	print ('Username:{}'.format(username))
	# Start time and image counting
	images = 0
	starttime = time.time()
	print ('Starting searching to the tree of folders...')
	# Search to folders
	for (dirpath, dirnames, filenames) in walk(cwd):
		for file in os.listdir(dirpath):
			# Find data
			if fnmatch.fnmatch(str(file), '*.SAFE'):
				images = images + 1
				print ("Raw data found (*.SAFE files): {}".format(str(file)))
				# Windows NOT TESTED
				if sys.platform.startswith('windows'):
					# On Windows x64. NOT TESTED!
					sentinelfile = os.path.join(dirpath,str(file))
					# Resolution: all
					if resolution is None:
						# Run Sen2Cor
						cmd = 'C:\\Users\\{}\\AppData\\Local\\Sen2Cor-02.09.00-win64\\L2A_Process.bat {}'.format(username,sentinelfile)
						print ("Running...", cmd)
						os.system(cmd)
					# In other case resolution must be either 10 or 20 or 60 meters.
					else:
						# Run Sen2Cor
						cmd = 'C:\\Users\\{}\\AppData\\Local\\Sen2Cor-02.09.00-win64\\L2A_Process.bat {} --resolution {}'.format(username,sentinelfile, resolution)
						print ("Running...", cmd)
						os.system(cmd)
				# Linux Tested
				elif sys.platform.startswith('linux'):
					sentinelfile = os.path.join(dirpath,str(file))
					# Works only if Sen2Cor is installed to home folder! In other case replace the correct path to Sen2Cor.
					# Resolution: all
					if resolution is None:
						# Run Sen2Cor
						cmd = '/home/{}/Sen2Cor-02.09.00-Linux64/bin/L2A_Process {}'.format(username,sentinelfile) # You can set Sen2Cor resolution by adding after L2A_Process --resolution=60 for 60m or 20 for 20m or 10 for 10m. By default resolution is all.
						print ("Running...", cmd)
						os.system(cmd)
					# In other case resolution must be either 10 or 20 or 60 meters.
					else:
						# Run Sen2Cor
						cmd = '/home/{}/Sen2Cor-02.09.00-Linux64/bin/L2A_Process {} --resolution {}'.format(username,sentinelfile, resolution) # You can set Sen2Cor resolution by adding after L2A_Process --resolution=60 for 60m or 20 for 20m or 10 for 10m. By default resolution is all.
						print ("Running...", cmd)
						os.system(cmd)
	# Calculating total time elapsed in hours, minutes and seconds.			
	elapsedtime=time.time()-starttime
	mins, secs = divmod(elapsedtime, 60)
	hours, mins = divmod(mins, 60)
	# Plural
	if images == 1:
		image = 'image'
	else:
		image = "images"

	print ("Algorithm completed for:", images, image, "in: {}:{}:{}".format(int(hours), int(mins), round(secs,2)))
