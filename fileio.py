#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:06:52 2018

@author: xgotda
"""

from IonClass import Ions
from helperMethods import *
#import staticVariables as sV


#  Variables
fileRead = 'mgfFiles/small.mgf'
# 'smallProb.mgf'
# 'QEHF_180716_15.mgf'
# 'small.mgf'
fileWrite = 'sec.txt'

#  oxo = oxonium (glycan)
oxo_ppm = 5
findOxo = [204.08667, 274.0921, 366.1395]
oxo_tolPairs = ppm_tolerance(findOxo, oxo_ppm)

#  pp = peptide (larger fragment)
pp_ppm = 5
findPP = [1786.9487, 1990.0281, 2136.086]
pp_tolPairs = ppm_tolerance(findPP, pp_ppm)

# cm = (doubly or triply ) charged mass
cm = []
for f in findPP:
    for n in range(2, 4):
        cm.append(chargedMassVar(f, n))

cm_tolPairs = ppm_tolerance(cm, pp_ppm)

mz_tolPairs = cm_tolPairs.copy()
mz_tolPairs.extend(pp_tolPairs)
print(str(oxo_tolPairs))
print(str(pp_tolPairs))
print(mz_tolPairs)


def ProcessMgf():
    linesRead = 0
    i = 0
    records = 0

    with open(fileRead, 'r') as rf:
        with open(fileWrite, 'w') as wf:
            writeHeaders(wf)
            for line in rf:
                linesRead += 1
                if 'BEGIN' in line:
                    records += 1
                    newIon = Ions()
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
                            tempVals = pepLine(line)
                            for mz, tolerance in oxo_tolPairs:
                                if compare(mz, tempVals[0], tolerance):
                                    newIon.addFragment(mz, tempVals)
                                    newIon.valid = True
                        line = rf.readline()

                    if newIon.valid:
                        i += 1
                        newIon.calculateMass()
                        writeToFile(wf, newIon)
                    del newIon
        wf.close()
    rf.close()

    print('Lines read: ' + str(linesRead))
    print('Records: ' + str(records))
    print('Added: ' + str(i))

# main - call methods to be executed
ProcessMgf()
