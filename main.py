import sys
import cv2 as cv

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.uic import *

from AdicionarNovoIndividuo import AdicionarNovoIndividuo
from ReconhecedorLbph import ReconhecedorLbph
from TreinadorClassificador import TreinadorClassificador


class Main(QMainWindow):
    def __init__(self):
        self.CAM_PORT = 0
        super(Main, self).__init__()
        self.main = loadUi('mainwindows.ui', self)

        self.adicionarNovoIndividuoAction.triggered.connect(lambda: self.loadNovoIndividuo())
        # self.adicionarDialogButton.clicked.connect(lambda: self.loadNovoIndividuo())
        # self.adicionarNovoIndividuoAction.clicked.connect(lambda: self.loadNovoIndividuo())
        self.validarIndividuoButton.clicked.connect(lambda: self.validarIdentidade())

        self.adicionarNovoIndividuoAction.triggered.connect(self.loadNovoIndividuo)
        self.treinarIndividuosAction.triggered.connect(self.treinarImagens)
        self.initUI()

    # @pyqtSlot()
    def loadNovoIndividuo(self):
        self.novoIndividuo = AdicionarNovoIndividuo(True, self.CAM_PORT)

    def initUI(self):
        self.th = ReconhecedorLbph(self, self.CAM_PORT)
        self.th.changePixmap.connect(self.imgLabel.setPixmap)
        self.th.start()

    def treinarImagens(self):
        classificadorLbph = TreinadorClassificador()

        if classificadorLbph.treinar():
            print('Treino Realizado com Sucesso!')
        else:
            print('Não foi possível concluir o treinamento')

        self.th.stop()
        self.initUI()

    def validarIdentidade(self):
        imgPath = self.th.validarIdentidade()
        #
        img = cv.imread(imgPath, 1)

        rgbImage = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        self.identidadeLabel.setPixmap(p)

app = QApplication(sys.argv)
w = Main()
w.show()
sys.exit(app.exec())
