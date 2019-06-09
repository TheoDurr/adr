# ADR - Logiciel de détection de l'environnement routier en python
Projet d'ISN - Lycée Louis Armand : Mulhouse, par Théo DURR, Louis HECTOR et Célian HUMBERT

# DOSSIER TECHNIQUE - Théo DURR
## Introduction
Notre projet consiste en la réalisation et, plus particulièrement, en la mise en place d’un programme permettant de détecter sur une vidéo, à la foi la route et ses usagers tels que les voitures, les bus et certains éléments de la signalisation et d’en effectuer un suivi par encadrement. Il consiste également en la réalisation d’une interface permettant de sélectionner le fichier à traiter et d’afficher les vidéos traitées et analysées par nos modèles.
Pour ma part, il s'agit de créer l'interface permettant de sélectionner le chemin de la vidéo, ainsi que celle qui permettra d'afficher la vidéo originale et les deux vidéos traitées

![Mockup](Mockup.png)

### Analyse des besoins et faisabilité
Le logiciel doit être capable de détecter des éléments liés à l'environnement que pourrait rencontrer une voiture lors de son utilisation.

### Répartition des tâches 
![ADR](Mindmap.png)

### Spécifications / Fonctionnalités
Le logiciel doit être capable de détecter les choses suivantes : 
  - [x] Marquages au sol
  - [x] Véhicules

### Prérequis pour le développement
Pour travailler sur ce projet, nous utiliserons python ainsi que diverses librairies :
  * Python 3.7.2
    * Pip 19.0.3 (gestionnaire de librairies) `python -m pip install pip --upgrade`
    * OpenCV (gestion des images et des vidéos / détection route)`python -m pip install opencv-contrib-python --upgrade`
    * Tensorflow (Modèle d'apprentissage automatisé) `python -m pip install tensorflow`
    * Tkinter (Gestion de l'interface graphique)

## Fenêtre de sélection du fichier
### Apercu
![fileSelection](fileSelection.jpg)

### Code
```python
# ─── IMPORT DES LIBRAIRIES ──────────────────────────────────────────────────────
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
```

Dans un premier temps, nous importons toutes les librairies nécessaire au bon fonctionnement du programme, l'utilité de chacune d'elle est expliquée plus haut dans l'introduction.
```python
# ─── IMPORT DES LIBRAIRIES ──────────────────────────────────────────────────────
from tkinter import filedialog
import tkinter as tk
```

Ensuite, nous créons les deux fonctions qui seront appelées lors du clic sur les boutons ```...``` et ```Sélectionner```. Ces fonctions sont appelées des [**callbacks**](https://www.codefellows.org/blog/what-is-a-callback-anyway/).
```python
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
    app.App(tk.Tk(),"adr - Algorithme de détection de route", fileEntry.get()) # Appel de l'application
```

Le reste du code comprend la création de l'interface permettant de choisir le fichier en question :
```python
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
```
Ce dernier morceau de code utilise de très nombreuses librairies Tkinter et énormément de méthodes de cette librairie.



## Travailler sur le projet
  * Dupliquer ce repository `git clone https://github.com/TheoDurr/adr`
