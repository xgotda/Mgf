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
        # re_s = compiled to only find strings that contain capital letters
        re_CL = re.compile('[A-Z]+')
        for line in rf:
            linesRead += 1
            t = re_CL.search(line)
            if t:
                startPos = t.end()+1
                if t.group() == 'BEGIN':
                    newIon = Ion()
                    i += 1
                elif t.group() == 'TITLE':
                    newIon.title = line[startPos:]
                elif t.group() == 'PEPMASS':
                    newIon.pepmass.initFromLine(startPos, line)
                elif t.group() == 'CHARGE':
                    newIon.charge = line[startPos:]
                elif t.group() == 'RTINSECONDS':
                    newIon.RT = line[startPos:]
                elif t.group() == 'SCANS':
                    newIon.scans = line[startPos:]
                elif t.group() == 'END':
                    hm.writeToFile(wf, newIon)
                    del newIon
#                   print(str(i))
            # TODO: put while loop here (within if t:)
            # while !re.search(r'\bEND', line):
            # look at each mz & intensity and if it matches: save
            else:
                o = re.search(r'[1-9]', line)
                if o:
                    newIon.addPep(line)


#       print(i)

    wf.close()
rf.close()

print('Lines read: ' + str(linesRead))
print(i)
