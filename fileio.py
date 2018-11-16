#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:06:52 2018

@author: xgotda
"""

# import sys
# sys.path.append('../plymgf')
# import re
from IonClass import Ions
# import helperMethods as hm
from helperMethods import *
import staticVariables as sV


# main - call methods to be executed
fileRead = 'mgfFiles/smallProb.mgf'
# 'smallProb.mgf'
# 'QEHF_180716_15.mgf'
# 'small.mgf'
# 'Text.txt'
fileWrite = 'sec.txt'


mass_accuracy_ppm = 0.010
findMZ = [204.08667, 274.0921, 366.1395]


def ProcessMgf():
    linesRead = 0
    i = 0
    records = 0

    with open(fileRead, 'r') as rf:
        with open(fileWrite, 'w') as wf:
    #        TODO: write headings
            wf.write('scanNo \t'
                     + 'pep.m_z \t'
                     + 'charge \t'
                     + 'calculated mass \t'
                     + 'RT \t'
                     + 'max \t'
                     + 'fragments   \t'
                     + '\n')
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
                                newIon.charge = int(line.split('=')[1][0])
                            elif 'RTINSECONDS' in line:
                                newIon.RT = stripLine(line)
                            elif 'SCANS' in line:
                                newIon.scanNo = stripLine(line)
                        else:
                            tempVals = pepLine(line)
#                            count = 0
                            for toFind in findMZ:
                                if compare(toFind, tempVals[0], mass_accuracy_ppm):
                                    newIon.addFragment(tempVals)
                        line = rf.readline()

                    if newIon.fragments:
                        i += 1
                        newIon.calculateMass()
                        writeToFile(wf, newIon)
                    del newIon
        wf.close()
    rf.close()

    print('Lines read: ' + str(linesRead))
    print('Records: ' + str(records))
    print('Added: ' + str(i))
