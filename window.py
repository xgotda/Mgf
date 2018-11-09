#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:05:35 2018

@author: xgotda
"""

import sys
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QMainWindow, QAction, QLineEdit, QMessageBox,
                             QLabel, QInputDialog, QFileDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect
from fileio import ProcessMgf, aTolerance
#setTol,


class App(QMainWindow):

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
        self.init_processingBtn()
        self.init_saveBtn()
        self.create_textbox()
        self.show()

    def init_processingBtn(self):
        processingBtn = QPushButton('Process', self)
        processingBtn.setToolTip('Click to process mgf file')
        r = QRect(450, 30, 70, 40)
        processingBtn.setGeometry(r)
        processingBtn.clicked.connect(self.on_click)

    def init_saveBtn(self):
        saveBtn = QPushButton('Save', self)
        saveBtn.setToolTip('Save file')
        r = QRect(450, 75, 70, 40)
        saveBtn.setGeometry(r)
        saveBtn.clicked.connect(self.on_save)

    def create_textbox(self):
        tolerance_label = QLabel('Enter tolerance:', self)
        tolerance_label.setGeometry(30, 20, 150, 20)
        self.tolerance_txtbox = QLineEdit(self)
        r = QRect(155, 15, 60, 30)
        self.tolerance_txtbox.setGeometry(r)
        self.tolerance_txtbox.setText(str(aTolerance))

    startTime = 0
    endTime = 0

    @pyqtSlot()
    def on_click(self):
#        setTol(self, float(self.tolerance_txtbox.text()))
        print('Processing mgf.')
        print('Tolerance: ' + str(aTolerance))
        startTime = time.time()
        ProcessMgf()
        endTime = time.time()
        self.statusBar().showMessage('Elapsed time: '
                                     + str(round((endTime - startTime), 4))
                                     + ' seconds')
        print('Done!')

    def on_save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
                self,
                "QFileDialog.getSaveFileName()", "",
                "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
