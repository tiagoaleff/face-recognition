import cv2 as cv
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage


class VideoSream(QThread):
    HARCASCADE_FRONTALFACE_FILE = 'harcascade\\haarcascade_frontalface_default.xml'
    changePixmap = pyqtSignal(QPixmap)
    rectangle = False

    def setRectangle(self):
        self.rectangle = True

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.detectorFace = cv.CascadeClassifier(self.HARCASCADE_FRONTALFACE_FILE)

    def run(self):
        camera = cv.VideoCapture(0)

        while True:
            conectado, frame = camera.read()

            frameCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            facesDetectadas = self.detectorFace.detectMultiScale(frameCinza, scaleFactor=1.1, minNeighbors=10,minSize=(30, 30))

            for (x, y, a, l) in facesDetectadas:
                #cv.imwrite('')
                cv.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)

            rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
