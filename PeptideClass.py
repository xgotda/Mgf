#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:06:27 2018

@author: xgotda
"""

import re

class Peptide:
    
    
    def __init__(self):
        self.m_z = 0.0
        self.intensity = 0.0
        
        
    def initFromLine(self, startPos, theLine):
        #t is the MatchObject which resulted in the line beginning with 
        # 'PEPMASS' being found. Used for position of first number.
        #line from file is the line currently read from file which 
        # will here be split into mz and intensity values
        # and saved into the object
        theLine= theLine[startPos:]
        t = re.search(r'\b ', theLine)
        self.m_z = theLine[:t.end()-1]
        self.intensity = theLine[t.end():]
    
    
        
    def pepStr(self):
        aStr = str(self.m_z) + ' ' + str(self.intensity)
        return aStr

