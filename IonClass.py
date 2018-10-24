#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:25:12 2018

@author: xgotda
"""

#import sys
from PeptideClass import Peptide


class Ion():
#self.valid is a flag denoting if we have had at least one match
    
    def __init__(self):
        self.valid = False
        self.title = ""
        self.charge = ""
        self.RT = 0
        self.scans = 0
        #self.pepmass = []
        self.pepmass = Peptide()
        self.fragments = []
 
#    def clear(self):
#        self.valid = False
#        self.title = ""
#        self.charge = ""
#        self.RT = 0
#        self.scans = 0
#        self.pepmass = []
#        #self.pepmass = Peptide()
#        self.fragments = []
# 
    
    def addPep(self, lineRead):
        tempPep = Peptide()
        tempPep.initFromLine(0, lineRead)
#        tempPep.m_z = mz
#        tempPep.intensity = insty
        self.fragments.append(tempPep)
    
    