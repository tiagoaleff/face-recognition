import sys

import cv2 as cv
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class GuiMain(QDialog):

    def __init__(self):
        super(GuiMain, self).__init__()
        loadUi('guimainui.ui', self)
        self.image = None

        self.loadButtom.clicked.connect(self.loadClicked)
        # self.videoStrean()

    @pyqtSlot()
    def loadClicked(self):
        self.camera = cv.VideoCapture(0)
        self.streanVideo()

    def streanVideo(self):
        while True:
            conectado, frame = self.camera.read()
            print(frame)
            self.image = frame
            self.displayImagem()

            if (cv.waitKey(1) == ord('q')):
                break

    def loadImage(self, path):
        self.image = cv.imread(path)
        # cv.imshow("capture", self.image)
        self.displayImagem()

    def displayImagem(self):
        qFormat = QImage.Format_Indexed8

        if len(self.image.shape) == 3:  # rows[0], cols[1], channels[2]
            if self.image.shape[2] == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888

        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qFormat)
        # BGR > RBG
        img = img.rgbSwapped()

        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        #self.imgLabel.setAligment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) tamanho imagem ainda nao funciona

        print(self.imgLabel)


app = QApplication(sys.argv)
window = GuiMain()
window.setWindowTitle('Reconhecimento Facial')
window.show()
sys.exit(app.exec())
