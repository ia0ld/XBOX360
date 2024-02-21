#\media\0000

import os

# Répertoire contenant les fichiers
repertoire = r'path'

for nom_fichier in os.listdir(repertoire):
    chemin_fichier = os.path.join(repertoire, nom_fichier)

    if os.path.isfile(chemin_fichier):
        with open(chemin_fichier, 'rb') as fichier:
            contenu = fichier.read()
            contenu_sans_112_premiers = contenu[3336:]
            nouveau_nom = os.path.splitext(nom_fichier)[0] + ".flv"
            nouveau_chemin = os.path.join(repertoire, nouveau_nom)
            with open(nouveau_chemin, 'wb') as nouveau_fichier:
                nouveau_fichier.write(contenu_sans_112_premiers)
            print(f"Le fichier {nom_fichier} a été traité pour enlever les 112 premiers bits et renommé en {nouveau_nom}.")
    if not nom_fichier.endswith('.flv'):
        os.remove(chemin_fichier)
        print(f"Le fichier original {nom_fichier} sans extension .flv a été supprimé.")
