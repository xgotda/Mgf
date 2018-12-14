"""
Created on Tue Nov 27 12:56:27 2018

@author: xgotda
""" 

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
        self.searchList = []
        self.initGlycans()
        self.initPeptides()
        self.initPotentials()


    def initGlycans(self):
        for o in self.oxoList:
            aGlycan = pc.FindPep(o, calcTol(o, self.oxo_ppm))
            self.searchList.append(aGlycan)

    def initPeptides(self):
        for p in self.ppList:
            aPep = pc.FindPep(p, calcTol(p, self.pp_ppm), pc._P)
            self.searchList.append(aPep)

    def initPotentials(self):
        for p in self.ppList:
            for n in range(2, 4):
                c = chargedMassVar(p, n)
                aPotential = pc.FindMcPep(p, c, calcTol(c, self.pp_ppm), n)
                self.searchList.append(aPotential)

    def search(self, currVals, ion):
        ''' Adds currVals to fragments dict if equal '''
        [curr_mz, curr_itsy] = currVals

        for s in self.searchList:
            if s.ptype == pc._G:
                if compare(s.mz, curr_mz, s.tol):
                    ion.addFragment(s.mz, curr_itsy, s.chtype)
                    break
            elif s.ptype == pc._P:
                if compare(s.mz, curr_mz, s.tol):
                    curr_itsy = max(curr_itsy, self.isoExists(curr_mz, s.chtype))    
                    ion.addFragment(s.mz, curr_itsy, s.chtype)
                    break
            elif s.ptype == pc._M:
                if compare(s.mz, curr_mz, s.tol):
                    curr_itsy = max(curr_itsy, self.isoExists(curr_mz, s.chtype))
                    ion.addFragment(s.parentPep, curr_itsy, s.chtype)
                    break

    def isoLine(self, aLine, mz, chtype):
        ''' Intensity of the line if it is its isotope.
            @return: intensity or zero
            @rtype: float '''
        returnIntensity = 0
        if 'END' not in aLine and  aLine.strip() != '':
            nextVals = pepLine(aLine)
            if isChargedVar(mz, nextVals[0], chtype):
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

    
        