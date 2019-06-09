# ─── IMPORT DES LIBRAIRIES ──────────────────────────────────────────────────────
import tkinter as tk 
import cv2 as cv
from PIL import Image, ImageTk

# ─── CREATION DES CLASSES ───────────────────────────────────────────────────────
class App:
    def __init__(self, window, windowTitle, videoSource = 0):
        self.window = window
        self.window.title(windowTitle)
        self.videoSource = videoSource

# ─── AFFICHAGE VIDEO ────────────────────────────────────────────────────────────
        self.originalVideoFrame = tk.LabelFrame(window, text = "Vidéo Originale")
        self.originalVideoFrame.pack(fill = "x")

        self.originalVid = MyVideoCapture(videoSource)

        self.canvas = tk.Canvas(self.originalVideoFrame, width = self.originalVid.width, height = self.originalVid.height)
        self.canvas.pack()

        self.delay = 10
        self.update()
        self.window.mainloop()
    def update(self):
        ret, frame = self.originalVid.getFrame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

        self.window.after(self.delay, self.update)
# ────────────────────────────────────────────────────────────────────────────────
# ─── TRAITEMENT DE LA VIDEO ─────────────────────────────────────────────────────
class MyVideoCapture:
    def __init__(self, videoSource = 0):
        self.vid = cv.VideoCapture(videoSource)
        if not self.vid.isOpened():
            raise ValueError("Impossible d'ouvrir le fichier vidéo", videoSource) # Chemin de fichier non renseigné ou invalide
        
        # Dimensions de la vidéo
        self.width = 720
        self.height = 480
    
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def getFrame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()

            frame = cv.resize(frame, (self.width,self.height))

            if ret:
                return(ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return(ret, None)
        else:
            return(ret, None)
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    App(tk.Tk(),"adr - Algorithme de détection de route", "videos/Colmar.mp4")