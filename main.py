from PyQt5 import QtCore

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.uic import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from reconhecedor_lbp import ReconhecedorLbp
from novoindividuo import NovoIndividuo


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.main = loadUi('mainwindows.ui', self)

        #openFile = QAction("&Open File", self)
        #openFile.setShortcut("Ctrl+o")
        #openFile.setStatusTip('Open File')
        #openFile.triggered.connect(self.fileOpen)
        #self.main.activ(openFile)
#
        #self.loadImage.addAction(self.showDialogInputImg())
        #self.main.isSignalConnected(self.adicionarDialogButton, self.loadNovoIndividuo())

        self.adicionarDialogButton.clicked.connect(lambda:self.loadNovoIndividuo())
        # self.initUI()

    @pyqtSlot()
    def loadNovoIndividuo(self):
        print('acao 1')
        self.novoIndividuo = NovoIndividuo(True)

    def initUI(self):
        th = ReconhecedorLbp(self)
        th.changePixmap.connect(self.imgLabel.setPixmap)
        th.start()

app = QApplication(sys.argv)
w = Main()
w.show()

sys.exit(app.exec())
