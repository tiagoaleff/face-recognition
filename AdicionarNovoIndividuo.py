from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from CapturaNovoIndividuo import CapturaNovoIndividuo


class AdicionarNovoIndividuo(QDialog):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, show=False, CAM_PORT=0):
        super(AdicionarNovoIndividuo, self).__init__()
        self.CAM_PORT = CAM_PORT
        loadUi('adicionarnovoindividuo.ui', self)

        self.initStreamVideo()
        self.novoIndividuoTextEdit.textChanged.connect(lambda: self.changeTextNovoIndividuo())

        if (show):
            self.show()

    def changeTextNovoIndividuo(self):
        if (len(self.novoIndividuoTextEdit.text()) > 1):
            self.capiturarImagemButton.setEnabled(True)
        elif (len(self.novoIndividuoTextEdit.text()) < 1):
            self.capiturarImagemButton.setEnabled(False)

    def initStreamVideo(self):
        th = CapturaNovoIndividuo(self, self, self.CAM_PORT, self.capiturarImagemButton, self.identificadorTextEdit, self.okButton, self.quantidadeImagemLabel, self.novoIndividuoTextEdit)
        th.changePixmap.connect(self.uploadLabelWizard)
        th.start()

    def uploadLabelWizard(self, value):
        self.novoIndividuoImagemLabel.setPixmap(value)
