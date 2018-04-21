from PyQt5 import QtCore

import cv2 as cv
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QAction, QFileDialog, QPushButton, QMenuBar
from PyQt5.uic import loadUi


class NovoIndividuo(QDialog):
    def __init__(self, show=False):
        super(NovoIndividuo, self).__init__()
        loadUi('adicionarnovoindividuo.ui', self)

        #self.addAction()

        #openFile = QAction("&Open File", self)
        #openFile.setShortcut("Ctrl+o")
        #openFile.setStatusTip('Open File')
        #openFile.triggered.connect(self.openWindowsOpenFile())

        #self.localizarFotoBotton.addAction(openFile)
        #test = QPushButton
        #test.addAction()

        if (show):
            self.show()

    def addAction(self):
        self.openFile = QAction("&Open File", self)
        self.openFile.setShortcut("Ctrl+o")
        self.openFile.setStatusTip('Open File')
        self.openFile.triggered.connect(self.openWindowsOpenFile())

        self.menu = QMenuBar
        self.menu.addMenu('&File')
        self.menu.addAction(self.openFile)
        QtCore.QObject.connect(self.menu, QtCore.SIGNAL("clicked()"), self.self.openFile.trigger)


    @pyqtSlot()
    def openWindowsOpenFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File', filter='(*.jpg)') #TODO: add new extensions imgs
        #name = QFileDialog.setNameFilter(str("Images (*.png *.xpm *.jpg)")).getOpenFileName(self, 'Open File')
        #imagemCarregada = cv.imread(name[0])
        #imagemCarregadaCinza = cv.cvtColor(imagemCarregada, cv.COLOR_BGR2GRAY)
        pass
