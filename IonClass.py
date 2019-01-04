#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:25:12 2018

@author: xgotda
"""

# import sys
from PeptideClass import Peptide
import staticVariables as sV


class Ions:

    def __init__(self):

        self.valid = False  # flag denoting if we have had at least one match
        self.title = ""
        self.charge = 0
        self.RT = 0
        self.scanNo = 0
        self.MaxInts = 0
        self.pepmass = Peptide()
        self.Mass = 0  # Calculated using pepmass and charge.
        self.fragments = {}
        self.fragmentCount = 0

    def calculateMass(self):
        ''' Calculate the mass of the peptide
            @return: Mass of original peptide
            @rtype: float '''
        self.Mass = self.charge * (self.pepmass.mz - sV._Hplus)

    #def addFragment(self, key, intensity, chtype):
    def addFragment(self, key, intensity, slItem):
        ''' Adds the intensity value for the given key
            to the fragments dictionary.
            @return: amends fragments dictionary with new value added
            @rtype: dictionary '''
        if self.fragments.get(key, False):
            self.fragments[key][slItem.chtype] = intensity
        else:
            self.fragments[key] = { 0 : slItem.ptype,
                                    slItem.chtype : intensity}
        self.fragmentCount += 1
        self.valid = True
