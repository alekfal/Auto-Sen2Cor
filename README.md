# Auto-Sen2Cor
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A. 

Sen2Cor 2.5.5 installation on Linux:

1.Open terminal (Ctrl+Alt+T)

2.Sen2Cor 2.5.5 installation:
$ wget http://step.esa.int/thirdparties/sen2cor/2.5.5/Sen2Cor-02.05.05-Linux64.run

$ sh Sen2Cor-02.05.05-Linux64.run

Installation successful!

Try:
$ /home/USERNAME/Sen2Cor-02.05.05-Linux64/bin/L2A_Process --help

Should return:
usage: L2A_Process.py [-h] [--resolution {10,20,60}] [--sc_only] [--cr_only]
                      [--refresh] [--GIP_L2A GIP_L2A]
                      [--GIP_L2A_SC GIP_L2A_SC] [--GIP_L2A_AC GIP_L2A_AC]
                      [--GIP_L2A_PB GIP_L2A_PB]
                      directory

Sentinel-2 Level 2A Processor (Sen2Cor). Version: 2.5.5, created: 2018.03.19,
supporting Level-1C product version <= 14.5.

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
  --GIP_L2A_PB GIP_L2A_PB
                        Select the processing baseline GIPP
