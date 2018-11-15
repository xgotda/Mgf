#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:25:12 2018

@author: xgotda
"""

# import sys
from PeptideClass import Peptide
import staticVariables as sV


class Ions():
    
    # Static variables for readibility
    _to_find = 0
    _mz_vals = 1
    _insy_vals = 2
    _mz_insy = 3

    def __init__(self):

        self.valid = False
        self.title = ""
        self.charge = 0
        self.RT = 0
        self.scanNo = 0
        self.pepmass = Peptide()
        self.Mass = 0
        self.fragments = []
        self.fragmentCount = 0

    def calculateMass(self):
        ''' calculate the mass of the peptide
        @return: Mass of original peptide
        @rtype: float '''
        self.Mass = float(self.charge * (self.pepmass.m_z - sV._H))
        return self.Mass

    def addFragment(self, vals):
        ''' adds the m/z and intensity values to the
            fragments list.
            @return: fragments list with new values added
            @rtype: [[m/z][intensity][[m/z, intensity]]] '''
        if len(self.fragments) == 0:
            self.fragments = [[float(vals[0])], [float(vals[1])], [vals]]
        else:
            self.fragmentMZs().append(float(vals[0]))
            self.fragmentIntensities().append(float(vals[1]))
            self.fragmentValues().append(vals)
        self.fragmentCount += 1

        # Alternative fragment structure of find value followed by val lists
        # fragments.append([to_findValue]) - TODO OUTSIDE OF HERE --- [] --- !
            # for f in to_find:
                # fragments.append([f, [], [], []])
        # fragments[position of current to_find value(poctv) ] - OUTSIDE 
        # fragments[poctv][_mz_vals].append(float(vals[0])) 
        # fragments[poctv][_insy_vals].append(float(vals[1]))
        # fragments[poctv][_mz_insy].append(float(vals))

    def fragmentMZs(self):
        ''' returns a list of m/z values
        @return: m/z values
        @rtype: list '''
        if len(self.fragments):
            return self.fragments[0]
        else:
            return []

    def fragmentIntensities(self):
        ''' returns a list of intensity values
        @return: intensity values
        @rtype: list '''
        if len(self.fragments):
            return self.fragments[1]
        else:
            return []

    def fragmentValues(self):
        ''' returns each mz, intensity pair
        @return: m/z, intensity pair
        @rtype: list '''
        if len(self.fragments):
            return self.fragments[2]
        else:
            return []
            