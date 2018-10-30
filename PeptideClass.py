#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:06:27 2018

@author: xgotda
"""


class Peptide:

    def __init__(self):
        self.m_z = 0.0
        self.intensity = 0.0

    def frLine(self, theLine):
        theLine = theLine.split(' ')
        self.m_z = float(theLine[0])
        self.intensity = float(theLine[1])

    def pepStr(self):
        aStr = str(self.m_z) + ' ' + str(self.intensity)
        return aStr
