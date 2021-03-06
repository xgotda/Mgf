#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:06:52 2018

@author: xgotda
"""

import sys
from IonClass import Ions
from helperMethods import *
from SearchClass import DoSearch
import numpy as np
from distutils.util import strtobool


# --- VARIABLES ---
# fileRead = 'mgfFiles/small.mgf'
fileRead = 'mgfFiles/QEHF_180716_15.mgf'
# 'small.mgf'
# 'smallProb.mgf'
fileWrite = 'temp/PP.txt'

#  oxo = oxonium (glycan)
oxo_ppm = 5
findOxo = [204.08667, 274.0921, 366.1395]

# #  pp = peptide (larger fragment)
pp_ppm = 5
findPP = [1786.9487, 1990.0281, 2136.086]


# print(sys.argv[:])
# Convert to correct type.
[fileRead, fileWrite, findOxo, oxo_ppm, findPP, pp_ppm,
dblCharged, tplCharged] = sys.argv[1:]

temp = [float(val) for val in findOxo.split('\n') if val]
findOxo = temp
temp = [float(val) for val in findPP.split('\n') if val]
findPP = temp
if oxo_ppm:
    oxo_ppm = int(oxo_ppm)
if pp_ppm:
    pp_ppm = int(pp_ppm)
dblCharged = bool(strtobool(dblCharged))
tplCharged = bool(strtobool(tplCharged))


aSearch = DoSearch(findOxo, oxo_ppm, findPP, pp_ppm)

def ProcessMgf():
    linesRead = 0
    addedIon = 0
    records = 0
    toPrint = []

    with open(fileRead, 'r') as rf:
        with open(fileWrite, 'w') as wf:
            line = 'start'
            while line:
                line = rf.readline()
                linesRead += 1
                if 'BEGIN' in line:
                    records += 1
                    newIon = Ions()
                    tempArr = []
                    line = rf.readline()
                    while 'END' not in line:
                        if '=' in line:
                            if 'TITLE' in line:
                                newIon.title = stripLine(line)
                            elif 'PEPMASS' in line:
                                newIon.pepmass.frLine(line.split('=')[1])
                            elif 'CHARGE' in line:
                                newIon.charge = int(stripLine(line)[0])
                            elif 'RTINSECONDS' in line:
                                newIon.RT = stripLine(line)
                            elif 'SCANS' in line:
                                newIon.scanNo = stripLine(line)
                        else:
                            tempArr.append(pepLine(line))
                        line = rf.readline()

                    npStart = np.array(tempArr)
                    newIon.MaxInts = max(npStart[:, 1])
                    newIon.npWorking = aSearch.reduceSearchList(npStart)
                    aSearch.search(newIon)

                    if newIon.valid:
                        addedIon += 1
                        newIon.calculateMass()
                        toPrint.append(newIon)
                    del newIon
            writeHeaders(wf, aSearch)
            npAll = np.array(processIons(toPrint, aSearch))
            for ion in toPrint:
                writeToFile(wf, ion, aSearch)
            # wf.write(str(npAll))

    print('Lines read: ' + str(linesRead))
    print('Records: ' + str(records))
    print('Added: ' + str(addedIon))


# main - call methods to be executed
ProcessMgf()
print('Done in MgfMain.py!')
