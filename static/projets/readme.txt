Site portefolio de Killian Besançon.

Ce dossier contient les différentes catégories des projets ainsi que leurs conetenu.


+-------------------+
|                   |
|   projets.zip     |
|                   |
+-------------------+

    
    ```
    /projets.zip
        /catégorie1
            /projet1
            /projet2
        /catégorie2
            /projet1
                /la_barrique.jpg
                /la_barique_finie.jpg
                /...
                /projet.json
            /projet2
            /projet3
    
    ```

Le nom des catégories et des projets sont libre. Cependant si tu veux qu'il y ait un ordre, je te conseille de les nommer ainsi "cat<priorité>" et "pro<priorité>".
Les catégories et les projets sont triés par ordre croissant de leur priorité.


Les images sont optionnelles et leur nom 100% libres. Elles doivent être placées dans le dossier du projet.
Le fichier projet.json contient les informations du projet. Il est obligatoire et doit être placé dans le dossier du projet.

+-------------------+
|                   |
|   projet.json     |
|                   |
+-------------------+

Le JSON : c'est tout le contenu de ta page détaillé de ton projet.
Voici un exemple expllicatif:



{
    "titre": "Rénovation et Transformation d’une barrique",       // Titre du projet (affiché sur la page d'accueil et en haut de la page détaillé)
    "date": "2020-2021",                                          // Date du projet (affiché en haut de la page détaillé)
    "sous_titre": "Étape 1",                                      // Sous-titre du projet (affiché en haut de la page détaillé)
    "feat": "Projet réalisé avec mon père",                       // Texte de présentation du projet (affiché nulle part pour l'instant)
    "img": "1.JPG",                                               // Image de présentation du projet (affiché sur la page d'accueil et en première image de la page détaillé)
    "desc": [                                                     // Description du projet paragraphes par paragraphes
        "Le projet consistait",                                   // Paragraphe 1
        "%6.png%",                                                // Insérer une image (nom de l'image dans le dossier du projet)
        "%2.png%3.png%",                                          // Double images (nom des images dans le dossier du projet)
        "Pour ce faire, nous avons",
        "Nous avons traité le bois et",
        "Nous avons attaché une charnière",
        "Enfin, nous avons ajouté des"
    ]
}

Note supplémentaire : les " (guillmet) sont à remplacer par des \" (antislash + guillmet) pour éviter les conflits avec le format des fichiers JSON.