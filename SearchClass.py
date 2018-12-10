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
        self.oxoList = glycans # glycans.sort()
        self.oxo_ppm = glycan_ppm
        self.ppList = peptides # peptides.sort()
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
        curr_mz = currVals[0]
        for s in self.searchList:
            if s.ptype == pc._G:
                if compare(s.mz, curr_mz, s.tol):
                    ion.addFragment(s.mz, currVals)
                    break
            elif s.ptype == pc._P:
                if compare(s.mz, curr_mz, s.tol):
                    if self.file:  # TODO: Better error handling here
                        isoIntensity = self.isoExists(curr_mz, s)
                        if isoIntensity:
                        # if the first iso exists, check for second and save max
                            isoIntensity_2 = self.isoExists(curr_mz+1, s, 2)
                            currVals[1] = max(currVals[1],
                                              isoIntensity, isoIntensity_2)
                    ion.addFragment(s.mz, currVals)
                    # Check for potentials!
                    break
            elif s.ptype == pc._M:
                # if compare(s.mz, curr_mz, s.tol):
                #     if self.file:  # TODO: Better error handling here
                #         isoIntensity = self.isoExists(curr_mz, s)
                #         if isoIntensity:
                #         # if the first iso exists, check for second and save max
                #             isoIntensity_2 = self.isoExists(curr_mz, s, 2)
                #             currVals[1] = max(currVals[1],
                #                               isoIntensity, isoIntensity_2)
                #     #ion.addFragment(s.mz, currVals)
                #     break
                pass

    def isoExists(self, mz, searchP, depth=1):
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

    
        