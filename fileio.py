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
fileRead = 'small.mgf'
# 'QEHF_180716_15.mgf'
# 'small.mgf'
# 'Text.txt'
fileWrite = 'sec.txt'


aTolerance = 1.000
linesRead = 1
i = 0

with open(fileRead, 'r') as rf:
    with open(fileWrite, 'w') as wf:
        # re_CL = compiled to only find strings that contain capital letters
        re_CL = re.compile('[A-Z]+')
        for line in rf:
            linesRead += 1
            t = re_CL.search(line)
            if t:
                startPos = t.end()+1  # Starting position of wanted string
                if t.group() in 'BEGIN':
                    newIon = Ion()
                    i += 1
                elif t.group() in 'TITLE':
                    newIon.title = line[startPos:]
                elif t.group() in 'PEPMASS':
                    newIon.pepmass.initFromLine(startPos, line)
                elif t.group() in 'CHARGE':
                    newIon.charge = line[startPos:]
                elif t.group() in 'RTINSECONDS':
                    newIon.RT = line[startPos:]
                elif t.group() in 'SCANS':
                    newIon.scans = line[startPos:]
                elif t.group() in 'END':
                    hm.writeToFile(wf, newIon)
                    del newIon
            # TODO: put while loop here (within if t:)
            # while !re.search(r'\bEND', line):
            # look at each mz & intensity and if it matches: save
            else:
                # Read lines with numbers only
#                o = re.search(r'[1-9]', line)
                o = re.findall(r'\S[0-9.]+[^ A-Za-z=]', line)
                if o:
#                    print(o[0])
                    newIon.addPep(line)

    wf.close()
rf.close()

print('Lines read: ' + str(linesRead))
print(i)
