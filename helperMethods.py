#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:51:30 2018

@author: xgotda
"""
import math


def writeToFile(FileName, IonObject):
    if FileName and IonObject:
#        TODO: create a buffer?
        info = (IonObject.scanNo + '\t'
                + str(IonObject.pepmass.m_z) + '\t'
                + str(IonObject.charge) + '\t'
                + str(IonObject.Mass) + '\t'
                + IonObject.RT + '\t'
                + str(max(IonObject.fragmentIntensities())) + '\t'
                + str(IonObject.fragmentCount)
                )

#       TODO: for each item in list of values to find?
        for i in range(IonObject.fragmentCount):
            info = info + '\t' + str(IonObject.fragmentValues()[i])

        FileName.write(info + '\n')
    else:
        print('invalid objects')


def stripLine(aline):
    return aline.split('=')[1].strip()


def pepLine(aLine):
    ''' Split the string of a fragment into it's m/z 
        and intensity values. 
        @return: list with an m/z and intensity value
        @rtype: list of two float values'''
    aLine = aLine.split(' ')
    m_z = float(aLine[0])
    intensity = float(aLine[1])
    return [m_z, intensity]


def compare(tofind, value, tolerance):
    ''' Compare wether two values are within
        the given tolerance. 
        @return: True if within the tolerance, False if not.
        @rtype: boolean '''
    return math.fabs(value - tofind) < tolerance
