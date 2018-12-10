#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:06:27 2018

@author: xgotda
"""
import staticVariables as sV


# Definitions of types
_G = 'Glycan'
_P = 'Peptide'
_M = 'Multi-charged peptide'

pType = {_G: _G,
         _P: _P,
         _M: _M
         }
#   TODO: fix ptype definitions such that the correct thing
#       HAS to be entered when setting ptype
#   _G = 1 and then dict[_G] = 'Glycan'???


class Pep:
    """ Base object for Glycans and Peptides.
        @params: m/z. """

    def __init__(self, m_z=0.0):
        self.mz = m_z


class Peptide(Pep):
    """ Peptide from the original molecule itself.
        @params: m/z, intensity. """

    def __init__(self, m_z=0.0, intensity=0.0):
        super().__init__(m_z=m_z)
        self.intensity = intensity

    def frLine(self, theLine):
        theLine = theLine.split(' ')
        self.mz = float(theLine[0])
        self.intensity = float(theLine[1])


class FindPep(Pep):
    """ Peptide to be found. Default to simplest ptype; Glycan.
        Can only be of charge-type _single (chType[_single]).
        @params: m_z,
                tolerance,
                peptide type,
                charge type = _single """

    def __init__(self, m_z=0.0,
                 tolerance=0.0, ptype=_G):
        ''' If complains about super() --> 
        super(FindPep, self) b/c python 3 vs python 2. '''
        super().__init__(m_z)
        self.tol = tolerance
        self.ptype = ptype
        self._chtype = sV.chType[sV._single]

    @property
    def ptype(self):
        return self._ptype

    @ptype.setter
    def ptype(self, type):
        ''' Defines type of Peptide. Pass in _G or _P. '''
        if type in [_G, _P]:
            self._ptype = pType[type]
        else:
            print('Illegal peptide type entered: '+str(type) +
                  '. Check that correct object is used. ' + '\n' +
                  'Peptide remains of type \"' + self.ptype + '\".')

    @property
    def chtype(self):
        return self._chtype

    @chtype.setter
    def chtype(self, notValid):
        ''' FindPep can only be of charge-type _single and
            is not allowed to be changed. '''
        pass


class FindMcPep(FindPep):
    """ Multi-charged peptide to be found and saved to
        the 'Potentials' list.
        @params: m/z,
                tolerance,
                peptide type = _M,
                charge type,
                parentPeptide. """

    def __init__(self, theParent, m_z=0.0, tolerance=0.0,
                 chargeType=sV._double
                 ):
        super().__init__(m_z, tolerance, _M)
        self._chtype = sV.chType[chargeType]
        self.parentPep = theParent

    @property
    def ptype(self):
        return super().ptype

    @ptype.setter
    def ptype(self, type):
        ''' FindMcPep can only be of ptype _M.
            Do not change. '''
        self._ptype = pType[_M]

    @property
    def chtype(self):
        return self._chtype

    @chtype.setter
    def chtype(self, chargeType):
        ''' Set charge type. Doubly or triply charged. '''
        if chargeType in [sV._double, sV._triple]:
            self._chtype = sV.chType[chargeType]
        else:
            print('Illegal charge type entered: '+str(chargeType) +
                  '. Check that correct object is used. ' + '\n' +
                  'Peptide charge remains \"' + str(self.chtype) + '\".')

#    def setParentPep(self, parent):
#        self.parentPep = parent
