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

    def search(self, anIon):
        for i in range(len(anIon.npWorking)):
            [curr_mz, curr_itsy] = anIon.npWorking[i]
            for s in self.findList:
                if compare(s.mz, curr_mz, s.tol):
                    mz_Key = s.mz
                    if s.ptype != pc._G:
                        curr_itsy = max(curr_itsy, self.check(anIon, i, s.chtype))
                    if s.ptype == pc._M:
                        mz_Key = s.parentPep
                    anIon.addFragment(mz_Key, curr_itsy, s)
                    break

    def check(self, anIon, pos, chType):
        ''' check current mz value against the next two and return max intensity
        '''
        currmz = anIon.npWorking[pos][0]
        toR = 0
        for i in range(1, 3):
            if pos+i < len(anIon.npWorking):
                [mz, insy] = anIon.npWorking[pos+i]
                if isIsotope(currmz, mz, chType):
                    toR = max(toR, insy)
                    currmz = mz
        return toR

        ''' Intensity of the line if it is its isotope.
            @return: intensity or zero
            @rtype: float '''


        ''' Checks if the n'th line (depth) in the file is
            an isotope of mz. Uses searchP (a Peptide object)
            for charge type (chtype).
            @return: The intensity of the isotope if found and
                    zero if no isotope is found.
            @rtype: float '''
