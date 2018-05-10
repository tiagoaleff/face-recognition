import cv2 as cv
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage


class CapturaNovoIndividuo(QThread):
    changePixmap = pyqtSignal(QPixmap)
    HARCASCADE_FRONTALFACE_FILE = "harcascade\\haarcascade_frontalface_default.xml"
    HARCASCADE_EYE_FILE = "harcascade\\haarcascade_eye.xml"
    rectangle = False
    largura = 220
    altura = 220
    amostra = 0
    keepLoop = True

    def __init__(self, dialogo, parent=None, CAM_PORT=0, capiturarImagemButton=None, identificadorTextEdit=None, okButton=None, quantidadeImagemLabel=None, novoIndividuoTextEdit=None):
        QThread.__init__(self, parent=parent)
        self.CAM_PORT = CAM_PORT

        self.dialogo = dialogo
        self.capiturarImagemButton = capiturarImagemButton
        self.identificadorTextEdit = identificadorTextEdit
        self.okButton = okButton
        self.quantidadeImagemLabel = quantidadeImagemLabel
        self.novoIndividuoTextEdit = novoIndividuoTextEdit

        self.detectorFace = cv.CascadeClassifier(self.HARCASCADE_FRONTALFACE_FILE)
        self.detectorOlho = cv.CascadeClassifier(self.HARCASCADE_EYE_FILE)

        self.okButton.clicked.connect(lambda: self.treinarImagens())
        self.capiturarImagemButton.clicked.connect(lambda: self.saveFrameAsImage())

    def run(self):
        camera = cv.VideoCapture(self.CAM_PORT)

        while True:
            conectado, self.frame = camera.read()

            if self.frame is None:
                continue

            frameCinza = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
            facesDetectadas = self.detectorFace.detectMultiScale(frameCinza, scaleFactor=1.1, minNeighbors=10, minSize=(100, 100))

            for (x, y, a, l) in facesDetectadas:
                cv.rectangle(self.frame, (x, y), (x + l, y + a), (0, 0, 255), 2)
                regiaoFace = self.frame[y: y + a, x: x + l]
                regiaoFaceCinza = cv.cvtColor(regiaoFace, cv.COLOR_BGR2GRAY)
                olhosDetectados = self.detectorOlho.detectMultiScale(regiaoFaceCinza)

                for (oX, oY, oL, oA) in olhosDetectados:
                    cv.rectangle(regiaoFace, (oX, oY), (oX + oL, oY + oA), (0, 255, 0), 2)

                    self.imagemFace = cv.resize(frameCinza[y: y + a, x: x + l], (self.largura, self.altura))
                    self.refreshPixmapFrames(self.frame)

            self.refreshPixmapFrames(self.frame)

    def saveFrameAsImage(self):
        id = self.identificadorTextEdit.text()

        if self.amostra == 1:
            cv.imwrite("fotos/pessoas." + id + ".00.jpg", self.frame)

        self.amostra += 1
        self.quantidadeImagemLabel.setText(str(self.amostra) + ' / 20')
        cv.imwrite("fotos/pessoas." + id + "." + str(self.amostra) + ".jpg", self.imagemFace)
        print("[Foto] " + str(self.amostra) + ": capturada com sucesso!]")

        if self.amostra >= 20:
            self.capiturarImagemButton.setEnabled(False)

    def refreshPixmapFrames(self, frame):
        rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)

    def exitFromLoop(self):
        self.keepLoop = False

    def treinarImagens(self):
        self.exit()
        self.quit()
        self.dialogo.hide() # fecha o dialogo
#
# def treinarImagens(self):
#     classificadorLbph = TreinadorClassificador()
#
#     if classificadorLbph.treinar():
#         print('Treino Realizado com Sucesso!')
#     else:
#         print('Não foi possível concluir o treinamento')
#
#     self.novoIndividuoTextEdit.setEnabled(False)
#     self.identificadorTextEdit.setEnabled(False)
#     self.exit()
#     self.quit()
#
#     self.dialogo.hide()
