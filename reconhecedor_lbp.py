import cv2 as cv
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap


class ReconhecedorLbp(QThread):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.detectorFace = cv.CascadeClassifier("venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
        self.reconhecedor = cv.face.LBPHFaceRecognizer_create()
        self.reconhecedor.read("classificadorLBPH2.yml")
        self.largura, self.altura = 220, 220
        self.font = cv.FONT_HERSHEY_COMPLEX_SMALL

    def run(self):
        camera = cv.VideoCapture(0)

        while True:
            conectado, frame = camera.read()
            frameCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            facesDetectadas = self.detectorFace.detectMultiScale(frameCinza, scaleFactor=1.1, minNeighbors=10,
                                                                 minSize=(30, 30))
            for (x, y, a, l) in facesDetectadas:
                cv.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)
                frameFaceCinza = cv.resize(frameCinza[y: y + a, x: x + l], (self.largura, self.altura))

                id, confianca = self.reconhecedor.predict(frameFaceCinza)

                nome = "Nao Encontrado"

                if (id == 1):
                    nome = "Tiago Aleff"
                elif (id == 2):
                    nome = "Rosani"
                elif (id == 3):
                    nome = "Sergio Coral"
                elif (id == 4):
                    nome = "Antonio"
                elif (id == 5):
                    nome = "Anne"
                elif (id == 6):
                    nome = "Gislane"
                elif (id == 7):
                    nome = "Morgana"
                elif (id == 8):
                    nome = "Diuly"

                #nome += ' (' + str(confianca) + ')'
                cv.putText(frame, nome, (x, y + (a + 30)), self.font, 2, (0, 0, 255))
                cv.putText(frame, str("%.2f" % confianca), (x, y + (a + 70)), self.font, 2, (0, 0, 255))

            if (cv.waitKey(1) == ord('q')):
                break

            rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
