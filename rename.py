# static\Dessins\Croquis
import os
import json


def dessinrename(path):
    filelist = os.listdir(path)
    for file in filelist:
        tmp = file
        file = file.replace("é", "e")
        file = file.replace("è", "e")
        file = file.replace("à", "a")
        file = file.replace("ç", "c")
        file = file.replace("ù", "u")
        file = file.replace("ô", "o")
        file = file.replace("ê", "e")
        file = file.replace("î", "i")
        file = file.replace("É", "E")
        file = file.replace("È", "E")
        file = file.replace("À", "A")
        file = file.replace("Ç", "C")
        file = file.replace("Ù", "U")
        file = file.replace("Ô", "O")
        file = file.replace("Ê", "E")
        file = file.replace("Î", "I")
        # if file starts with a number, add a 0
        while len(file.split(";;;")[0]) < 4:
            file = "0" + file

        os.rename(path + "\\" + tmp, path + "\\" + file)


# DESSINS
# Enlève les accents des noms de fichiers
filelist = "static\\Dessins\\Croquis"
dessinrename(filelist)
filelist = "static\\Dessins\\Inktober"
dessinrename(filelist)
filelist = "static\\Dessins\\Personnels"
dessinrename(filelist)
filelist = "static\\Dessins\\Observation"
dessinrename(filelist)

# PROJETS
# lire récursivement les fichiers json dans static/projets/xx/projet.json
import os

# Définit le répertoire racine à partir duquel commencer la recherche
racine = "static/projets"

# Liste pour stocker les chemins des fichiers trouvés
fichiers_projet = []

# Parcourt l'arborescence des dossiers
for dossier, sous_dossiers, fichiers in os.walk(racine):
    for fichier in fichiers:
        # Vérifie si le fichier courant est un 'projet.json'
        if fichier == "projet.json":
            # Ajoute le chemin complet du fichier à la liste
            fichiers_projet.append(os.path.join(dossier, fichier))

# Affiche les chemins des fichiers trouvés
for fichier in fichiers_projet:
    # vérifier si le fichier est bien formaté
    try:
        with open(fichier, "r", encoding="utf-8") as outfile:
            data = json.load(outfile)
    except:
        raise ValueError("Erreur dans le fichier " + fichier)
    

# PLASTIQUES
# lire récursivement les fichiers json dans static/plastiques/xx/projet.json
# Définit le répertoire racine à partir duquel commencer la recherche
racine = "static/plastiques"

# Liste pour stocker les chemins des fichiers trouvés
fichiers_plastique = []

# Parcourt l'arborescence des dossiers
for dossier, sous_dossiers, fichiers in os.walk(racine):
    for fichier in fichiers:
        # Vérifie si le fichier courant est un 'projet.json'
        if fichier == "projet.json":
            # Ajoute le chemin complet du fichier à la liste
            fichiers_plastique.append(os.path.join(dossier, fichier))

# Affiche les chemins des fichiers trouvés
for fichier in fichiers_plastique:
    # vérifier si le fichier est bien formaté
    try:
        with open(fichier, "r", encoding="utf-8") as outfile:
            data = json.load(outfile)
    except:
        raise ValueError("Erreur dans le fichier " + fichier)
    
print("Tout est OK !")
