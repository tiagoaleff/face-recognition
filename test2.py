import sys

import numpy as np
import cv2 as cv
from PyQt5.QtWidgets import QApplication, QDialog, QAction, QFileDialog, QInputDialog
from PyQt5.uic import loadUi

from reconhecedor_lbp import ReconhecedorLbp


class App(QDialog):
    def __init__(self):
        super(App, self).__init__()
        ui = loadUi('guimainui.ui', self)
        self.title = 'Reconhecimento Facial'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.largura = 220
        self.altura = 220

        self.classificador = cv.CascadeClassifier(
            "venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")  # TODO retirar daqui

        self.classificadorOlho = cv.CascadeClassifier("venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")# TODO retirar daqui
        openFile = QAction("&Open File", self)
        openFile.setShortcut("Ctrl+o")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.fileOpen)
        ui.addAction(openFile)

        self.loadImage.addAction(self.showDialogInputImg())
        self.initUI()

    def fileOpen(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        imagemCarregada = cv.imread(name[0])
        imagemCarregadaCinza = cv.cvtColor(imagemCarregada, cv.COLOR_BGR2GRAY)

        faceDetectada = self.classificador.detectMultiScale(imagemCarregadaCinza, scaleFactor=1.1, minSize=(100, 100), minNeighbors=10)

        for (x, y, a, l) in faceDetectada:
            cv.rectangle(imagemCarregada, (x, y), (x + l, y + a), (0, 1, 255), 2)

            regiaoFace = imagemCarregada[y: y + a, x: x + l]
            regiaoFaceCinza = cv.cvtColor(regiaoFace, cv.COLOR_BGR2GRAY)
            olhosDetectados = self.classificadorOlho.detectMultiScale(regiaoFaceCinza)

            for (oX, oY, oL, oA) in olhosDetectados:
                cv.rectangle(regiaoFace, (oX, oY), (oX + oL, oY + oA), (0, 255, 0), 2)

                #if np.average(imagemCarregadaCinza) > 109:
                imagemFace = cv.resize(imagemCarregadaCinza[y: y + a, x: x + l], (self.largura, self.altura))
                cv.imwrite("fotos2/xxx.jpg", imagemFace)
                #print("[Foto] " + str(amostra) + ": capturada com sucesso!]")

    def showDialogInputImg(self):
        text, result = QInputDialog.getText(self, 'Entrada de Dados', 'Entre com o nome')

        if result == True:
            print(text)

    def initUI(self):
        th = ReconhecedorLbp(self)
        th.changePixmap.connect(self.imgLabel.setPixmap)
        th.start()
        pass

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
