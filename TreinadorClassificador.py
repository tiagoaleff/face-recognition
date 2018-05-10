import os

import cv2 as cv
import numpy as np


class TreinadorClassificador:
    lbph = cv.face.LBPHFaceRecognizer_create()

    def __init__(self):
        pass

    def getImagensIds(self):
        caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

        identificadores = []
        faces = []

        for caminhoImagem in caminhos:
            imagemFace = cv.cvtColor(cv.imread(caminhoImagem), cv.COLOR_BGR2GRAY)
            id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
            identificadores.append(id)
            faces.append(imagemFace)

        return np.array(identificadores), faces

    def treinar(self):
        print("Treinando...")
        identificadores, faces = self.getImagensIds()
        self.lbph.train(faces, identificadores)
        self.lbph.write('resultadotreinamento/classificadorLBPH.yml')
        return True
