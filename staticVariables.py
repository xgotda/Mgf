#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:50:54 2018

@author: xgotda
"""

_Hplus = 1.00727647
''' Mass of a proton in atomic mass units (u) '''

#   To be filtered by in the Spectra file
#   but not searched for by weight in mgf file
#    new Glycan("Acetate", 42.0106f, true),
#    new Glycan("H+", 1.00727f, true),
#    new Glycan("H", 1.00783f, true),
#    new Glycan("H2O", 18.01056f, true),
#    new Glycan("K+", 38.963707f, true),
#    new Glycan("Na+", 22.989768f, true),
#    new Glycan("Phosp", 79.9663f, true),
#    new Glycan("Sulph", 79.9568f, true)

_Fuc = 'Fuc'
_Hex = 'Hex'
_HexA = 'HexA'
_HexNAc = 'HexNAc'
_NeuAc = 'NeuAc'
_NeuGc = 'NeuGc'


''' list of common monosaccarides and their
    (underivatised) monoisotopic masses'''
Glycans = {
        _Fuc: 146.0579,
        _Hex: 162.0528,
        _HexA: 176.03209,
        _HexNAc: 203.0794,
        _NeuAc: 291.0954,
        _NeuGc: 307.0903
        }


# Charge types
_single = 1
_double = 2
_triple = 3
_variance = 0.01    #+- 0.01

chType = {
        _single: 1/_single,
        _double: 1/_double,
        _triple: 1/_triple
    }
