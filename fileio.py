#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:06:52 2018

@author: xgotda
"""

# import sys
import re
from IonClass import Ion
import helperMethods as hm


# main - call methods to be executed
fileRead = 'smallProb.mgf'
# 'QEHF_180716_15.mgf'
# 'small.mgf'
# 'Text.txt'
fileWrite = 'sec.txt'


aTolerance = 1.000
linesRead = 0
i = 0
find = [111.04450, 111.08083, 113.06006, 115.07567, 119.08573,
        121.10140, 123.08068, 125.05994, 125.09627, 127.03926]


def stripLine(aline):
    return aline.split('=')[1].strip()

with open(fileRead, 'r') as rf:
    with open(fileWrite, 'w') as wf:
        for line in rf:
            linesRead += 1
            if 'BEGIN' in line:
                newIon = Ion()
                i += 1
                line = rf.readline()
                while 'END' not in line:
                    if '=' in line:
                        if 'TITLE' in line:
                            newIon.title = stripLine(line)
                        elif 'PEPMASS' in line:
                            newIon.pepmass.initFromLine(0, line.split('=')[1])
                        elif 'CHARGE' in line:
                            newIon.charge = stripLine(line)
                        elif 'RTINSECONDS' in line:
                            newIon.RT = stripLine(line)
                        elif 'SCANS' in line:
                            newIon.scans = stripLine(line)
                    else:
                        newIon.addPep(line)
                    line = rf.readline()

                hm.writeToFile(wf, newIon)
                del newIon

    wf.close()
rf.close()

print('Lines read: ' + str(linesRead))
print(i)
