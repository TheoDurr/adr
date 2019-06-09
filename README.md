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

## Travailler sur le projet
  * Dupliquer ce repository `git clone https://github.com/TheoDurr/adr`
