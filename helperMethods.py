#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:51:30 2018

@author: xgotda
"""
import math
import staticVariables as sV


''' -----------------------------------------------------------
        Functions for file and string processing.
    ----------------------------------------------------------- '''

def writeToFile(FileName, IonObject):
    ''' Print details from the IonObject to file. '''
    if FileName and IonObject:
        info = (IonObject.scanNo + '\t'
                + str(IonObject.pepmass.mz) + '\t'
                + str(IonObject.charge) + '\t'
                + str(IonObject.Mass) + '\t'
                + IonObject.RT + '\t'
                + str(max(IonObject.fragments.values())) + '\t'
                + str(IonObject.fragmentCount)
                )
        info = info + '\t' + str(list(IonObject.fragments.items()))

#        for k in IonObject.fragments:
#            info = info + '\t '+ str([k, IonObject.fragments[k]])
        FileName.write(info + '\n')
    else:
        print('invalid objects')

def writeHeaders(FileName):
    ''' Hardcoded headers.
        @return: None
        #   TODO: print from built list'''
    if FileName:
        header = ('scanNo \t'
                  + 'pep.m_z \t'
                  + 'charge \t'
                  + 'calc mass \t'
                  + 'RT \t'
                  + 'maxInts \t'
                  + 'fragmentNo   \t'
                  + ' \n')
        FileName.write(header)
    else:
        print('Invalid filename: ' + str(FileName))

def stripLine(aline):
    return aline.split('=')[1].strip()

def pepLine(aLine):
    ''' Split the string of a fragment into it's m/z
        and intensity float values.
        @return: list with an m/z and intensity value
        @rtype: list '''
    aLine = aLine.split(' ')
    return [float(aLine[0]), float(aLine[1])]


''' -----------------------------------------------------------
    Functions for mathematical and list processing.
    ----------------------------------------------------------- '''

def compare(tofind, value, tolerance):
    ''' Compare whether two values are within
        the given tolerance.
        @return: True if within the tolerance, False if not.
        @rtype: boolean '''
    return math.fabs(value - tofind) < tolerance

def ppm_tolerance(valuesList, ppm):
    ''' Calculate the tolerance for each value in valuesList
        for the given ppm.
        @return: list of values, tolerance pairs
        @rtype: list '''
    pp = 1000000/ppm
    pairs = []
    for mz in valuesList:
        pairs.append([mz, mz/pp])
    return pairs

def chargedMassVar(mz, n):
    ''' Calculating the theoretical n (doubly or triply)
        charged mass variation of passed in m/z value
        @return: n-charged mass
        @rtype: float'''
    return (mz + (sV._Hplus * (n-1)))/ n

def isChargedVar(curr, pot, n):
    ''' Compares curr(ent) and pot(ential) to see
        if pot is the n charged mass variation of curr.
        @return: true if pot is a variation of curr
        of charge n.
        @rtype: boolean '''
        # curr + 0.5 +- tolerance
        # 1/1 = chtuype1, 1/2 = chType2 etc
    return curr + sV.chType[n] < pot < curr + sV.chType[n]


def isoExists(file, val):
    ''' Checks if the next line in the file is
        an isotope of valself.
        @return: The intensity of the isotope if found and
                zero if no isotope is found.
        @rtype: float '''
    currPos = file.tell()
    nextLine = file.readline()
    file.seek(currPos)
    nextVals = pepLine(nextLine)

    # if isChargedVar(val, nextVals[0], type)
    if (val + 0.99 < nextVals[0] < val + 1.003):
        return nextVals[1]
    else:
        return 0
