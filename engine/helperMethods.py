#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:51:30 2018

@author: xgotda
"""
import math
import staticVariables as sV
import PeptideClass as p


''' -----------------------------------------------------------
        Functions for file and string processing.
    ----------------------------------------------------------- '''

def processIons(toPrint, search):
    aRow = []
    allRows = []
    for ion in toPrint:
        aRow = [ion.scanNo, ion.pepmass.mz, ion.charge,
                ion.Mass, ion.RT, ion.MaxInts]
        fList = ion.fragments
        for o in search.oxoList:
            if fList.get(o, False):
                aRow.append(fList[o][1])
            else:
                aRow.append(0)

        for ap in search.ppList:
            for i in range(1, 4):
                # if fList.get(ap, False) and if fList[ap].get(i, False):
                #     aRow.append(fList[ap][i])
                # else:
                #     aRow.append(0)
                # This instead of the code below. check if does the same thing!
                if fList.get(ap, False):
                    if fList[ap].get(i, False):
                        aRow.append(fList[ap][i])
                    else:
                        aRow.append(0)
                else:
                    aRow.append(0)
        allRows.append(aRow)
    return allRows

def writeToFile(FileName, IonObject, theSearch):
    ''' Print details from the IonObject to file. '''
    if FileName and IonObject:
        deci = "{0:.4f}"  # number of decimal points
        info = (IonObject.scanNo + '\t'
                + deci.format(IonObject.pepmass.mz) + '\t'
                + str(IonObject.charge) + '\t'
                + deci.format(IonObject.Mass) + '\t'
                + IonObject.RT + '\t'
                + str(IonObject.MaxInts) + '\t'
                + str(IonObject.fragmentCount)
                )

        fList = IonObject.fragments
        for o in theSearch.oxoList:
            if fList.get(o, False):
                info =  info + '\t' + str(fList[o][1])
            else:
                info = info + '\t' + str(0)

        for ap in theSearch.ppList:
            for i in range(1, 4):
                if fList.get(ap, False):
                    if fList[ap].get(i, False):
                        info = info + '\t' + str(fList[ap][i])
                    else:
                        info = info + '\t' + str(0)
                else:
                    info = info + '\t' + str(0)

        FileName.write(info + '\n')
    else:
        print('invalid objects')

def writeHeaders(FileName, theSearch):
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
                  )
                  #+ ' \n')

        for o in theSearch.oxoList:
            header = (header + str(o) + '\t ')
        for p in theSearch.ppList:
            header = (header + str(p) + '\t _2 \t _3 \t ')
        # header = (header + '1786.9487 \t _2 \t _3 \t 1990.0281 \t _2 \t _3 \t 2136.086 \t _2 \t _3')
        header = (header + ' \n')


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

def calcTol(m_z, ppm):
    ''' Calculate the tolerance for given m_z.
        @return: tolerance
        @rtype: float '''
    pp = 1000000/ppm
    return m_z/pp

def ppm_tolerance(valuesList, ppm):
    ''' Calculate the tolerance for each value in valuesList
        for the given ppm.
        @return: list of values, tolerance pairs
        @rtype: list '''
    # pp = 1000000/ppm
    pairs = []
    for m_z in valuesList:
        pairs.append([m_z, calcTol(m_z, ppm)])
    return pairs

def chargedMassVar(mz, n):
    ''' Calculating the theoretical n-charged (doubly or triply)
        mass variation of passed in m/z value
        @return: n-charged mass
        @rtype: float'''
    return (mz + (sV._Hplus * (n-1))) / n

def isIsotope(curr, pot, n):
    ''' Compares curr(ent) and pot(ential) to see
        if pot is an isotope of curr.
        @return: true if pot is curr's isotope.
        @rtype: boolean '''
        # e.g. curr + 0.5 +- tolerance
    temp = math.fabs(pot-curr)
    return math.fabs(temp-sV.chType[n]) < sV._variance
