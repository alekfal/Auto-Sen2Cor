# Auto-Sen2Cor
This Software is created for the automatic atmospheric correction of Sentinel 2 Data using Sen2Cor algorithm given freely by E.S.A.

### Sen2Cor 02.08.00 installation on Linux:

1.Open terminal (Ctrl+Alt+T)

2.Sen2Cor 02.08.08 installation:

```bash
$wget http://step.esa.int/thirdparties/sen2cor/2.8.0/Sen2Cor-02.08.00-Linux64.run
```

```bash
sh Sen2Cor-02.08.08-Linux64.run
```
Installation successful!

### Try:

```bash
/home/USERNAME/Sen2Cor-02.08.08-Linux64/bin/L2A_Process --help

usage: L2A_Process.py [-h] [--mode MODE] [--resolution {10,20,60}]
                      [--datastrip DATASTRIP] [--tile TILE]
                      [--output_dir OUTPUT_DIR] [--work_dir WORK_DIR]
                      [--img_database_dir IMG_DATABASE_DIR]
                      [--res_database_dir RES_DATABASE_DIR]
                      [--processing_centre PROCESSING_CENTRE]
                      [--archiving_centre ARCHIVING_CENTRE]
                      [--processing_baseline PROCESSING_BASELINE] [--raw]
                      [--tif] [--sc_only] [--cr_only] [--debug]
                      [--GIP_L2A GIP_L2A] [--GIP_L2A_SC GIP_L2A_SC]
                      [--GIP_L2A_AC GIP_L2A_AC] [--GIP_L2A_PB GIP_L2A_PB]
                      input_dir

Sentinel-2 Level 2A Processor (Sen2Cor). Version: 2.8.0, created: 2019.02.20,
supporting Level-1C product version 14.2 - 14.5.

positional arguments:
  input_dir             Directory of Level-1C input

optional arguments:
  -h, --help            show this help message and exit
  --mode MODE           Mode: generate_datastrip, process_tile
  --resolution {10,20,60}
                        Target resolution, can be 10, 20 or 60m. If omitted,
                        only 20 and 10m resolutions will be processed
  --datastrip DATASTRIP
                        Datastrip folder
  --tile TILE           Tile folder
  --output_dir OUTPUT_DIR
                        Output directory
  --work_dir WORK_DIR   Work directory
  --img_database_dir IMG_DATABASE_DIR
                        Database directory for L1C input images
  --res_database_dir RES_DATABASE_DIR
                        Database directory for results and temporary products
  --processing_centre PROCESSING_CENTRE
                        Processing centre as regex: ^[A-Z_]{4}$, e.g "SGS_"
  --archiving_centre ARCHIVING_CENTRE
                        Archiving centre as regex: ^[A-Z_]{4}$, e.g. "SGS_"
  --processing_baseline PROCESSING_BASELINE
                        Processing baseline in the format: "dd.dd", where
                        d=[0:9]
  --raw                 Export raw images in rawl format with ENVI hdr
  --tif                 Export raw images in TIFF format instead of JPEG-2000
  --sc_only             Performs only the scene classification at 60 or 20m
                        resolution
  --cr_only             Performs only the creation of the L2A product tree, no
                        processing
  --debug               Performs in debug mode
  --GIP_L2A GIP_L2A     Select the user GIPP
  --GIP_L2A_SC GIP_L2A_SC
                        Select the scene classification GIPP
  --GIP_L2A_AC GIP_L2A_AC
                        Select the atmospheric correction GIPP
  --GIP_L2A_PB GIP_L2A_PB
                        Select the processing baseline GIPP
```

### Call script:

Help:

```bash
python3 Auto-S2C.py -h
```

------------------------------------------

Resolution option: all

```bash
python3 Auto-S2C.py
```
------------------------------------------

Resolution option: 10 meters

```bash
python3 Auto-S2C.py -r 10
```

------------------------------------------

Resolution option: 20 meters

```
$python3 Auto-S2C.py -r 20
```

------------------------------------------

Resolution option: 60 meters

```
$python3 Auto-S2C.py -r 60
```

### Notes:

Note 1: In order for the script to work make sure that paths to Sen2Cor (Linux: lines 81 & 87, Window: lines 65 & 71) are correct.
