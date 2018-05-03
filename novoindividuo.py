from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QAction, QMenuBar, QPushButton
from PyQt5.uic import loadUi

from videostream import VideoSream


class NovoIndividuo(QDialog):
    CHOOSE_WEB_CAM = 0  # disposivo webcam, 0 = padrão, 1 = segundo dispositivo conectado, ...
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, show=False):
        super(NovoIndividuo, self).__init__()
        loadUi('adicionarnovoindividuo.ui', self)

        self.initStreamVideo()
        self.novoIndividuoTextEdit.textChanged.connect(lambda: self.changeTextNovoIndividuo())

        if (show):
            self.show()

    def changeTextNovoIndividuo(self):
        if (len(self.novoIndividuoTextEdit.text()) > 1):
            self.recordVideoButton.setEnabled(True)
        elif(len(self.novoIndividuoTextEdit.text()) < 1):
            self.recordVideoButton.setEnabled(False)

    def initStreamVideo(self):
        th = VideoSream(self)
        th.changePixmap.connect(self.saveNovoIndividuo)
        th.start()

    def saveNovoIndividuo(self, value):
        value.save('teste01.jpg')
        self.novoIndividuoImagemLabel.setPixmap(value)

    def addAction(self):
        self.openFile = QAction("&Open File", self)
        self.openFile.setShortcut("Ctrl+o")
        self.openFile.setStatusTip('Open File')
        self.openFile.triggered.connect(self.openWindowsOpenFile())

        self.menu = QMenuBar
        self.menu.addMenu('&File')
        self.menu.addAction(self.openFile)
        QtCore.QObject.connect(self.menu, QtCore.SIGNAL("clicked()"), self.self.openFile.trigger)
