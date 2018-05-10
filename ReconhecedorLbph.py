import os

import cv2 as cv
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap


class ReconhecedorLbph(QThread):
    changePixmap = pyqtSignal(QPixmap)

    listFrames = []

    def stop(self):
        self.keepThead = False

    def __del__(self):
        self.quit()
        self.wait()

    def __init__(self, parent=None, CAM_PORT=0):
        QThread.__init__(self, parent=parent)
        self.keepThead = True
        self.CAM_PORT = CAM_PORT
        self.detectorFace = cv.CascadeClassifier("harcascade\haarcascade_frontalface_default.xml")

        self.reconhecedor = None

        if os.path.isfile("resultadotreinamento/classificadorLBPH.yml"):
            self.reconhecedor = cv.face.LBPHFaceRecognizer_create()
            self.reconhecedor.read("resultadotreinamento/classificadorLBPH.yml")

        self.largura, self.altura = 220, 220
        self.font = cv.FONT_HERSHEY_COMPLEX_SMALL

    def run(self):
        camera = cv.VideoCapture(self.CAM_PORT)

        try:
            while self.keepThead:
                conectado, frame = camera.read()

                if frame is None:
                    continue

                if self.reconhecedor is None:
                    self.atualizarFrameLabel(frame)
                    continue

                frameCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                facesDetectadas = self.detectorFace.detectMultiScale(frameCinza, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

                for (x, y, a, l) in facesDetectadas:
                    cv.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)
                    frameFaceCinza = cv.resize(frameCinza[y: y + a, x: x + l], (self.largura, self.altura))

                    self.id, confianca = self.reconhecedor.predict(frameFaceCinza)

                    nome = "Nao Encontrado"

                    if (confianca > 61):
                        nome = "Nao Encontrado"
                        self.id = None
                    else:
                        if (self.id == 1):
                            nome = "Tiago Aleff"
                        elif (self.id == 2):
                            nome = "Rosani"
                        elif (self.id == 3):
                            nome = "Sergio Coral"
                        elif (self.id == 4):
                            nome = "Antonio"
                        elif (self.id == 5):
                            nome = "Anne"
                        elif (self.id == 6):
                            nome = "Gislane"
                        elif (self.id == 7):
                            nome = "Morgana"
                        elif (self.id == 8):
                            nome = "Diuly"
                        elif self.id == 45 or self.id == 345:
                            nome = 'Tiago Aleff'

                    # self.gerarIdentidade(id, nome)
                    # self.validarIdentidade(frame)
                    # nome += ' (' + str(confianca) + ')'
                    cv.putText(frame, nome, (x, y + (a + 30)), self.font, 2, (0, 0, 255))
                    cv.putText(frame, str("%.2f" % confianca), (x, y + (a + 70)), self.font, 2, (0, 0, 255))

                self.atualizarFrameLabel(frame)

        except ValueError:
            print('erro')

    def atualizarFrameLabel(self, frame):
        rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)

    # def gerarIdentidade(self, id, nome):
    #     self.valifarIdentidade()
    #     totalEncontro = [x[2] for x in self.listFrames if x[0] == id]
    #
    #     if totalEncontro is None:
    #         totalEncontro = 0
    #
    #     totalEncontro += 1
    #     self.listFrames = [id, nome, totalEncontro]

    def validarIdentidade(self):
        id = -1

        if self.id is None:
            id = self.id

        imgPath = 'fotos\\pessoas.' + str(id) + '.00.jpg'

        return imgPath
