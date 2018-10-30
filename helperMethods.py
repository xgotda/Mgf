#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:51:30 2018

@author: xgotda
"""
import math


def writeToFile(FileName, IonObject):
    if FileName and IonObject:
        FileName.write('TITLE: ' + IonObject.title + '\t'
                       + 'fragments:   ' + str(len(IonObject.fragsMZs()))
                       + '\t'
                       + IonObject.pepmass.pepStr()
                       + '\n'
                       + '\t \t maxIntensity:'
                       + str(max(IonObject.fragsIntens()))
                       + '\n'
                       )
    else:
        print('invalid objects')


def stripLine(aline):
    return aline.split('=')[1].strip()


def pepLine(aLine):
    aLine = aLine.split(' ')
    m_z = float(aLine[0])
    intensity = float(aLine[1])
    return [m_z, intensity]


def compare(tofind, value, tolerance):
    return math.fabs(value - tofind) < tolerance
