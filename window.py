#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:05:35 2018

@author: xgotda
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from fileio import ProcessMgf


#class App(QMainWindow):
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'The Ioniser'
        self.left = 450
        self.top = 300
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.statusBar().showMessage('Message in statusbar.')
        button = QPushButton('Process', self)
        button.setToolTip('Click to process mgf file')
        button.move(80,70)
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Processing mgf.')
        ProcessMgf()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
