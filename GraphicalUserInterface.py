from tkinter import *
import cv2 as cv


class GraphicalUserInterface:

    def __init__(self, title="Reconhecimento Facial"):
        self.window = Tk()
        self.window.config(background="#7b1fa2")
        self.set_title(title)
        self.set_menu()

        imageFrame = Frame(self.window, width=600, height=500)
        imageFrame.grid(row=0, column=0, padx=10, pady=2)

        self.camera = cv.VideoCapture(0)
        self.run()

    def set_webcam(self):
        return ""

    def set_title(self, title):
        self.window.title(title)

    def run(self):
        self.window.mainloop()

    def run_video_strean(self):
        # Graphics window
        imageFrame = Frame(self.window, width=600, height=500)
        imageFrame.grid(row=0, column=0, padx=10, pady=2)

        # Capture video frames
        main = Label(imageFrame)
        main.grid(row=0, column=0)

        conectacao, frame = self.camera.read()
        #framCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # usado na detecção



