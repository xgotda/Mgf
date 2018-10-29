#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:51:30 2018

@author: xgotda
"""


def writeToFile(FileName, IonObject):
    if FileName and IonObject:
        FileName.writelines('TITLE: ' + IonObject.title + '\t'
                       + IonObject.pepmass.pepStr() + '\t'
#        FileName.write(str(IonObject.scans))
                       + 'fragments:   ' + str(len(IonObject.fragments)) + '\t')
#                        IonObject.fragments[0].pepStr() + '\n')
#        FileName.write('TITLE: ' + IonObject.title)
#        FileName.write(IonObject.pepmass.pepStr())
##        FileName.write(str(IonObject.scans))
#        FileName.write('fragments:   ')
#        FileName.write(str(len(IonObject.fragments)) + '\n')
#        if len(IonObject.fragments) > 0:
        FileName.write(IonObject.fragments[0].pepStr())

    else:
        print('inivalid objects')

