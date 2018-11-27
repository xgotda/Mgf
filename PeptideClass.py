#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:06:27 2018

@author: xgotda
"""
import staticVariables as sV


# Definitions of types
_G = 'G'
_P = 'P'
_M = 'M'

pType = { _G : 'Glycan',
          _P : 'Peptide',
          _M : 'McPeptide'  # Multi-charged peptide
        }
#   TODO: fix ptype definitions such that the correct thing
#       HAS to be entered when setting ptype
#   _G = 1 and then dict[_G] = 'Glycan'???


class Pep:
    """ Base object for Glycans and Peptides.
        @params: m/z. """

    def __init__(self, m_z = 0.0):
        self.mz = m_z


class Peptide(Pep):
    """ Peptide from the original molecule itself.
        @params: m/z, intensity. """

    def __init__(self, m_z = 0.0, intensity = 0.0):
        super().__init__(m_z)
        self.intensity = intensity

    def frLine(self, theLine):
        theLine = theLine.split(' ')
        self.mz = float(theLine[0])
        self.intensity = float(theLine[1])


class FindPep(Pep):
    """ Peptide to be found. Default to simplest ptype; Glycan.
        Can only of charge-type _single (chType[_single]).
        @params: m/z,
                intensity,
                tolerance,
                peptide type,
                charge type = _single """

    def __init__(self, m_z = 0.0,
                 tolerance = 0.0, type = _G):
        super().__init__(m_z)
        self.tol = tolerance
        self.ptype = type
        self.chType = sV.chType[sV._single]

    @property
    def ptype(self):
        return self.__ptype

    @ptype.setter
    def ptype(self, type):
        ''' Defines type of Peptide. Pass in _G or _P. '''
        if type in [_G, _P]:
            self.__ptype = pType[type]
        else:
            print('Illegal peptide type entered: '+str(type) +
                    '. Check that correct object is used. ' + '\n' +
                    'Peptide remains of type \"' + self.ptype + '\".')

    @property
    def chType(type):
        return self.__mchType

    @chType.setter
    def chType(self, notValid):
        ''' FindPep can only be of charge-type _single and
            is not allowed to be changed. '''
        pass


class FindMcPep(FindPep):
    """ Multi-charged peptide to be found and saved to
        the 'Potentials' list.
        @params: m/z,
                intensity,
                tolerance,
                peptide type = _M,
                charge type,
                parentPeptide. """

    def __init__(self, m_z = 0.0, tolerance = 0.0,
                 charge = sV.chType[sV._double],
                 parent = 0.0):
        super().__init__(m_z, tolerance,)
        self.ptype = pType[_M]
        self.chType = charge
        self.parentPep = parent

    @property
    def ptype(self):
        return super(FindMcPep, self).ptype

    @ptype.setter
    def ptype(self, type):
        ''' FindMcPep can only be of ptype _M.
            Do not change. '''
        pass

    @property
    def chType(self):
        return super(FindMcPep, self).chType

    @chType.setter
    def chType(self, chargeType):
        ''' Set charge type. Doubly or triply charged. '''
        if chargeType in [sV._double, sV._triple]:
            self.chType = sV.chType[chargeType]
        else:
            print()

    def setParentPep(self, parent):
        self.parentPep = parent
