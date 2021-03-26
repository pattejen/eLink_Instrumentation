#!/usr/bin/env python

import subprocess

# WARNING:
# Write file names ending in .vna
# Do not include .txt (do not use .vna.txt)

options = [
           #['Redo_VNA', 'TP_1p4m_35_ChD0.vna'],
           #['Redo_VNA', 'TP_1p4m_35_ChD1_redo_v1.vna'],
           #['Redo_VNA', 'TP_1p4m_35_ChCMD_redo_v1.vna'],

           #['Redo_VNA', 'TP_35cm_60_ChD0_redo.vna'],
           #['Redo_VNA', '082820_TP_60_35cm_ChD1_KA.vna'],
           #['Redo_VNA', 'TP_35cm_60_ChCMD_redo.vna'],
            
            # using Cu calibration plate
            #['data', '9_feb_2021_test1_1.vna'],
            #['data', '9_feb_2021_test1_2.vna'],
            #['data', '9_feb_2021_test1_3.vna'],
            #['data', '9_feb_2021_test1_4.vna'],
            #['data', '9_feb_2021_test1_5.vna'],
            
            # cable 100
            #['data', 'TP_35cm_100_test1_1.vna'],
            
            # calibration
            #['data', 'calibration_test.vna'],
            #['data', 'small_SMA.vna'],
            #['data', 'straight_SMA.vna'],
            
            # cable 129
            # ['data', 'TP_0p35m_129_ChCMD.vna'],
            # ['data', 'TP_0p35m_129_ChD0.vna'],
            # ['data', 'TP_0p35m_129_ChD1.vna'],
            # ['data', 'TP_0p35m_129_ChD2.vna'],
            # ['data', 'TP_0p35m_129_ChD3.vna'],
            ['data', 'TP_trial2_0tpi.vna'],
            ['data', 'TP_trial2_2tpi.vna'],
            ['data', 'TP_trial2_4tpi.vna'],
            ['data', 'TP_trial2_6tpi.vna'],
            ['data', 'TP_trial2_8tpi.vna'],
    
	  ]

command = 'python3 python/readVNADataSKRF.py --data_directory={0:s} --basename={1:s}'

for opt in options:
    s = command.format(opt[0], opt[1])
    print(s)
    subprocess.call( [s, ""], shell=True )	

