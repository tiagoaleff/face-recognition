from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QAction, QFileDialog
from PyQt5.uic import loadUi

import cv2 as cv


class NovoIndividuo(QDialog):
    def __init__(self, show=False):
        super(NovoIndividuo, self).__init__()
        self.novoIndividuoUi = loadUi('adicionarnovoindividuo.ui', self)

        openFile = QAction("&Open File", self)
        openFile.setShortcut("Ctrl+o")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.openWindowsOpenFile)
        #self.localizarFotoBotton.clicked(openFile)
        #self.novoIndividuoUi.activ(openFile)

        self.localizarFotoBotton.addAction(openFile)

        if (show):
            self.show()

    @pyqtSlot()
    def openWindowsOpenFile(self):
        #openFile = QAction("&Open File", self)
        #openFile.setShortcut("Ctrl+o")
        #openFile.setStatusTip('Open File')
        #openFile.triggered.connect(self.fileOpen)
        #openFile.activate(self.fileOpen)
        #self.main.activ(openFile)
#
        #openFile = QAction("&Open File", self)
        #openFile.setShortcut("Ctrl+o")
        #openFile.setStatusTip('Open File')
        #openFile.triggered.connect(self.fileOpen)
        #self.main.activ(openFile)

        name = QFileDialog.getOpenFileName(self, 'Open File')
        imagemCarregada = cv.imread(name[0])
        imagemCarregadaCinza = cv.cvtColor(imagemCarregada, cv.COLOR_BGR2GRAY)
        pass