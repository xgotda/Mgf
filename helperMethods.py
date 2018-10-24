#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:51:30 2018

@author: xgotda
"""


def writeToFile(FileName, IonObject):
    if FileName and IonObject:
        FileName.writelines('title  - '+IonObject.title)
        FileName.writelines(str(IonObject.pepmass.m_z))
        FileName.writelines(' '+str(IonObject.pepmass.intensity))
#        FileName.writelines(str(IonObject.scans))
        FileName.writelines('fragments:   ')
        FileName.writelines(str(len(IonObject.fragments)) + '\n')
#        FileName.writelines(IonObject.fragments[0].m_z)
#        FileName.writelines(' ' + IonObject.fragments[0].intensity)
    else:
        print('inivalid objects')

