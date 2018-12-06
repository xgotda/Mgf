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
        self.pepmass = Peptide()
        self.Mass = 0  # Calculated using pepmass and charge.
        self.fragments = {}  # dictionary
        self.fragmentCount = 0
  # TODO: Get rid of fragmentCount. Use len(list(dict.items()))

    def calculateMass(self):
        ''' calculate the mass of the peptide
            @return: Mass of original peptide
            @rtype: float '''
        self.Mass = self.charge * (self.pepmass.mz - sV._Hplus)

    def addFragment(self, key, vals):
        ''' adds the intensity value for the given key
            to the fragments dictionary.
            @return: amends fragments dictionary with new value added
            @rtype: dictionary '''
        intensity = vals[1]  # keep only intensity
        if self.fragments.get(key, False):
            self.fragments[key].append(intensity)
        else:
            ''' Only these two lines are relevant
            after isotope check!! '''
            self.fragments[key] = [intensity]
        self.fragmentCount += 1
        self.valid = True
