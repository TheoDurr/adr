# ─── IMPORT DES LIBRAIRIES ──────────────────────────────────────────────────────
import app as app
from tkinter import filedialog
import tkinter as tk

# ─── CALLBACKS ─────────────────────────────────────────────────────
def openFile():
    filePath = filedialog.askopenfilename(
        initialdir = "/",
        title = "Selectionner le fichier",
        filetypes = (("Fichier mpeg","*.mp4"),("Tous les fichiers","*.*")))
    fileEntry.set(filePath)
def launchApp():
    print(fileEntry.get())
    mainWindow.quit()
    app.App(tk.Tk(),"adr - Algorithme de détection de route", fileEntry.get())
        
# ─── PROGRAMME PRINCIPAL ────────────────────────────────────────────────────────
mainWindow = tk.Tk()
mainWindow.title("Adr - Sélection du fichier source")

windowFrame = tk.LabelFrame(mainWindow, text = "Sélection du chemin du fichier", padx = 10)
windowFrame.pack(fill = "both")

fileFrame = tk.Frame(windowFrame)
fileFrame.pack()

fileLabel = tk.Label(fileFrame, text = "Fichier : ")
fileLabel.pack(side = "left")

fileEntry = tk.StringVar()
entryField = tk.Entry(fileFrame, textvariable = fileEntry, width = 50).pack(side = "left")

explorerMenu = tk.Button(fileFrame, text = "...", command = openFile)
explorerMenu.pack()

buttonFrame = tk.Frame(windowFrame, pady = 2)
buttonFrame.pack(fill = "y")

validateButton = tk.Button(buttonFrame, text = "Sélectionner", command = launchApp)
validateButton.pack(side = "left")
cancelButton = tk.Button(buttonFrame, text = "Annuler", command = mainWindow.quit).pack(side = "left")

mainWindow.mainloop()