#!/bin/env python

# Convert model parameter info to csv format

import os, sys, csv

finput = 'addons/models/dim6top_LO_UFO/parameters.py'

if not os.path.isfile(finput):
    print('File does not exist.')
    sys.exit()
    
with open(finput) as f:
    info = f.read().splitlines()
    with open('parameters.csv', 'w') as fout:
        csvw = csv.writer(fout)
        for iline, line in enumerate(info):            
            if 'Parameter(' in line:
                par = line.lstrip().split(' ')[0]
                nature, typ, texname, lhablock = ('NA' for _ in range(4))
                if par not in ['ZERO', 'Lambda', 'G', 'Gstrong', 'vev', 'MW', 'aEWM1', 'aEW', \
                'sw2', 'cw', 'sw', 'ee', 'g1', 'gw', 'lam', 'yb', 'yt', 'ytau', 'muH', \
                'Gf', 'aS', 'ymb', 'ymt', 'ymtau', 'MZ', 'MTA', 'MT', 'MB', 'MH', 'WZ', 'WW', 'WT', 'WH', 'sq2']:
                    while line != "":
                        iline = iline+1
                        line = info[iline].strip().strip('"').strip(',').replace('\'', '')
                        if 'nature' in line: nature = line.replace('nature = ', '')
                        elif 'type' in line: typ = line.replace('type = ', '')
                        elif 'texname' in line: texname = line.replace('texname = ', '')
                        elif 'lhablock' in line: lhablock = line.replace('lhablock = ', '')
                    csvw.writerow([par, nature, typ, texname, lhablock])
