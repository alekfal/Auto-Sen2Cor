# Auto-Sen2Cor
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A. This script works with anaconda and Sen2Cor algorithm, so they must be installed in your computer.


Sen2Cor 2.3.1 installation on Linux:

1.Open terminal (Ctrl+Alt+T)

2.3.Anaconda 4.2.0 installation:
$ wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh

$ bash Anaconda2-4.2.0-Linux-x86_64.sh

3.Sen2Cor 2.3.1 installation:
$ wget http://step.esa.int/thirdparties/sen2cor/2.3.1/sen2cor-2.3.1.tar.gz

$ tar -xvzf sen2cor-2.3.1.tar.gz && cd sen2cor-2.3.1

$ which python (Command should return:/home/username/anaconda2/bin/python; if not, try to change pythonpath)

$ python setup.py install

Installation successful!

4.Setting up Sen2Cor environmental variables:

$ export export SEN2COR_HOME=/home/username/sen2cor

$ export SEN2COR_BIN=/home/username/anaconda2/lib/python2.7/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor

$ export GDAL_DATA=/home/username/anaconda2/lib/python2.7/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor/cfg/gdal_data

Try:
$ L2A_Process --help
Should return:
usage: L2A_Process [-h] [--resolution {10,20,60}] [--sc_only] [--cr_only]
                   [--refresh] [--GIP_L2A GIP_L2A] [--GIP_L2A_SC GIP_L2A_SC]
                   [--GIP_L2A_AC GIP_L2A_AC]
                   directory

Sentinel-2 Level 2A Prototype Processor (Sen2Cor). Version: 2.3.0, created:
2016.11.18, supporting Level-1C product version: 14.

positional arguments:
  directory             Directory where the Level-1C input files are located

optional arguments:
  -h, --help            show this help message and exit
  --resolution {10,20,60}
                        Target resolution, can be 10, 20 or 60m. If omitted,
                        all resolutions will be processed
  --sc_only             Performs only the scene classification at 60 or 20m
                        resolution
  --cr_only             Performs only the creation of the L2A product tree, no
                        processing
  --refresh             Performs a refresh of the persistent configuration
                        before start
  --GIP_L2A GIP_L2A     Select the user GIPP
  --GIP_L2A_SC GIP_L2A_SC
                        Select the scene classification GIPP
  --GIP_L2A_AC GIP_L2A_AC
                        Select the atmospheric correction GIPP

Possible error messages:

$ L2A_Process home/username/.../S2A_OPER_PRD_MSIL1C_PDMC_20161008T183126_R051_V20161008T105022_20161008T105022.SAFE
Traceback (most recent call last):
File "home/case/anaconda2/Scripts/L2A_Process-script.py", line 11, in
load_entry_point('sen2cor==2.3.1', 'console_scripts', 'L2A_Process')()
File "home/username/anaconda2/lib/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor/L2A_Process.py", line 169, in main
config.setSchemes()
File "home/username/anaconda2/lib/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor/L2A_Config.py", line 3072, in setSchemes
self.logger.fatal('wrong identifier for xml structure: ' + product)
AttributeError: 'NoneType' object has no attribute 'fatal'

Solution:

The problem is that sen2cor looks for config and other data in the root of the sen2cor package, in a subdirectory called cfg... actually that folder is inside another directory called sen2cor in the package, so you have to copy-paste it. In your case:
The package is installed in the folder:
"/home/username/anaconda2/lib/site-packages/sen2cor-2.3.0-py2.7.egg/
In that directory there should be another directory named cfg (with all config data and other things), but there is not...
As a matter of fact, that directory is in this other folder:
"home/username/anaconda2/lib/site-packages/sen2cor-2.3.0-py2.7.egg/sen2cor/
so, you just have to copy the whole "cfg" folder (with all its contents) from this last path to the first one.

Known issues:
1.Spaces cause problem to Sen2Cor algorithm. Please avoid using spaces in the absolute path to images.
2.The processor is able to perform a 10 m image without background pixels (a full scene) with a memory of about 6 GB. Below the value of 6GB it might work, but this is dependent on the amount of existing non background pixels. The reason for this huge memory consumption is the fact, that for some of the atmospheric calculations (AOT) a collection of full arrays of size 10.000 x 10.000 must be kept in memory, as otherwise artifacts due to tiling will occur. So in your case, the size of 5 GB seems to be a bit to low. The memory errors you observe occur in a function call of the scipy Rect.BivariateSpline function, outside of the sen2cor code.
