"""
Created on Tue Nov 27 12:56:27 2018

@author: xgotda
"""

import PeptideClass as pc
from helperMethods import *


class DoSearch:
    """docstring for DoSearch."""

    def __init__(self, oxos=[], oxo_ppm,
                 peptides=[], peptide_ppm):
        self.oxoList = oxos
        self.oxo_ppm = oxo_ppm
        self.ppList = peptides
        self.pp_ppm = peptide_ppm
        self.searchList = []

    def initGlycans(self):
        for o in self.oxoList:
            aGlycan = pc.FindPep(m_z=o,
                                 tolerance=calcTol(o, self.oxo_ppm))
            self.searchList.append(aGlycan)

    def initPeptides(self):
        for p in self.ppList:
            aPep = pc.FindPep(m_z=p,
                              tolerance=calcTol(p, self.pp_ppm),
                              ptype=pc._P)
            self.searchList.append(aPep)

    def initPotentials(self):
        for p in self.ppList:
            for n in range(2, 4):
                c = chargedMassVar(p, n)
                aPotential = pc.FindMcPep(m_z=c,
                                          tolerance=calcTol(c, self.pp_ppm),
                                          chargeType=n, parent=p)
                self.searchList.append(aPotential)

    def search(self, valueToFind):
        for s in self.searchList:
            if s.ptype == pc._G:
                pass
            elif s.ptype == pc._P:
                pass
            else:
                pass
