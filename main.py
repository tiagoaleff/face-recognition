import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import *

from novoindividuo import NovoIndividuo
from reconhecedor_lbp import ReconhecedorLbp


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.main = loadUi('mainwindows.ui', self)

        self.adicionarDialogButton.clicked.connect(lambda: self.loadNovoIndividuo())
        self.initUI()

    @pyqtSlot()
    def loadNovoIndividuo(self):
        self.novoIndividuo = NovoIndividuo(True)

    def initUI(self):
        #th = ReconhecedorLbp(self)
        #th.changePixmap.connect(self.imgLabel.setPixmap)
        #th.start()
        pass

app = QApplication(sys.argv)
w = Main()
w.show()

sys.exit(app.exec())
