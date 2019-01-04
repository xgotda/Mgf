"""
Created on Tue Nov 27 12:56:27 2018

@author: xgotda
"""

import numpy as np
import PeptideClass as pc
from helperMethods import *


class DoSearch:
    """docstring for DoSearch."""

    def __init__(self, glycans=[], glycan_ppm=0,
                 peptides=[], peptide_ppm=0):
        glycans.sort()
        peptides.sort()
        self.oxoList = glycans
        self.oxo_ppm = glycan_ppm
        self.ppList = peptides
        self.pp_ppm = peptide_ppm
        self.mcList = []
        self.findList = []
        self.initGlycans()
        self.initPeptides()
        self.initPotentials()

    def setMinMax(self):
        n = 2.5
        self.min = min(self.oxoList + self.mcList + self.ppList) - n
        self.max = max(self.oxoList + self.mcList + self.ppList) + n

    def initGlycans(self):
        for o in self.oxoList:
            aGlycan = pc.FindPep(o, calcTol(o, self.oxo_ppm))
            self.findList.append(aGlycan)

    def initPeptides(self):
        for p in self.ppList:
            aPep = pc.FindPep(p, calcTol(p, self.pp_ppm), pc._P)
            self.findList.append(aPep)

    def initPotentials(self):

        for parent in self.ppList:
            for n in range(2, 4):
                mz = chargedMassVar(parent, n)
                self.mcList.append(mz)
                aPotential = pc.FindMcPep(parent, mz, calcTol(mz, self.pp_ppm), n)
                self.findList.append(aPotential)
        print(self.mcList)

    def reduceSearchList(self, npArray):
        self.setMinMax()
        npTop = npArray[np.nonzero(self.min < npArray[:, 0])[0],:]
        npReduced = npTop[np.nonzero(npTop[:, 0] < self.max)[0],:]
        return npReduced

    def search(self, npArray, anIon):
        for currVals in npArray:
            self.lookInFindList(currVals, anIon)

    def lookInFindList(self, currVals, ion):
        [curr_mz, curr_itsy] = currVals
        for s in self.findList:
            if compare(s.mz, curr_mz, s.tol):
                # print(' ' + str(curr_mz))
                mz_Key = s.mz
                if s.ptype == pc._P:
                    curr_itsy = max(curr_itsy, self.isoExists(curr_mz, s.chtype))
                if s.ptype == pc._M:
                    curr_itsy = max(curr_itsy, self.isoExists(curr_mz, s.chtype))
                    mz_Key = s.parentPep
                ion.addFragment(mz_Key, curr_itsy, s)
                break


    def isoLine(self, aLine, mz, chtype):
        ''' Intensity of the line if it is its isotope.
            @return: intensity or zero
            @rtype: float '''
        returnIntensity = 0
        if 'BEGIN' not in aLine and aLine.strip() != '':
            nextVals = pepLine(aLine)
            # print(nextVals)
            # if isChargedVar(mz, nextVals[0], chtype):
            if isIsotope(mz, nextVals[0], chtype):
                returnIntensity = nextVals[1]
        return returnIntensity

    def isoExists(self, mz, chtype):
        ''' @return: The intensity of the isotope if found and
                    zero if no isotope is found.
            @rtype: float '''
        toReturn = 0
        if self.file:  # TODO: Better error handling here
            nextLines = readXlines(self.file, 2, True)
            toReturn = max(self.isoLine(nextLines[0], mz, chtype),
                           self.isoLine(nextLines[1], mz, chtype))
        return toReturn

    def isoOldExists(self, mz, searchP, depth=1):
        ''' Checks if the n'th line (depth) in the file is
            an isotope of mz. Uses searchP (a Peptide object)
            for charge type (chtype).
            @return: The intensity of the isotope if found and
                    zero if no isotope is found.
            @rtype: float '''
        toReturn = 0
        nextLine = readXlines(self.file, depth)
        if 'END' not in nextLine:
            nextVals = pepLine(nextLine)
            if isChargedVar(mz, nextVals[0], searchP.chtype):
                toReturn = nextVals[1]
        return toReturn
