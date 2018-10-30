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

with open(fileRead, 'r') as rf:
    with open(fileWrite, 'w') as wf:
        # re_CL = compiled to only find strings that contain capital letters
        re_CL = re.compile('[A-Z]{2,}')
        for line in rf:
            linesRead += 1
            t = re_CL.search(line)
            if t:
                startPos = t.end()+1  # Starting position of wanted string
                if 'BEGIN' in t.group():
                    newIon = Ion()
                    i += 1
                elif 'TITLE' in t.group():
                    newIon.title = line[startPos:]
                elif 'PEPMASS' in t.group():
                    newIon.pepmass.initFromLine(startPos, line)
                elif 'CHARGE' in t.group():
                    newIon.charge = line[startPos:]
                elif 'RTINSECONDS' in t.group():
                    newIon.RT = line[startPos:]
                elif 'SCANS' in t.group():
                    newIon.scans = line[startPos:]
                elif 'END' in t.group():
                    hm.writeToFile(wf, newIon)
                    del newIon
            # TODO: put while loop here (within if t:)
            # while !re.search(r'\bEND', line):
            # look at each mz & intensity and if it matches: save
            else:
                # Read lines with numbers only
                valueArray = re.findall(r'\S[0-9.+-Ee]+[^ A-DF-Za-df-z=]', line)
                if valueArray:
#                    print(o[0])
                    newIon.addFr(valueArray)

    wf.close()
rf.close()

print('Lines read: ' + str(linesRead))
print(i)
