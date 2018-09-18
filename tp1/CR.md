**Nom/Prénom :** Guillem Eloïse 

# Rapport TP1

## Séance 1: Environnement de travail et initiation à Python

### Partie 1: Environnement de travail, premiers pas avec git

 1. Choix de l'environnement de travail
 
 Mon environnement de travail est constitué du **terminal** par défaut de l'environnement du Cremi, et de **emacs**.
 
 2. Clonage du dépôt Git
 
 Grâce à la commande **git clone** suivie de https://github.com/upici/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif.git dans le terminal , un répertoire a été créé dans mon répertoire courant. Le nom de ce répertoire est : **Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif**.
 
 3. Familiarisation avec le contenu du répertoire

- Les fichiers md, contiennent du code dans le langage **Markdwon**. _README.md_ contient l'énoncé et les questions du TP. _CR.md_ est le fichier contenant le compte-rendu de ma séance de TP.

- Les fichiers py, sont des fichiers de *programmes* en **Python**.

- L'image _ecran01.png_ est l'image référencée dans le README.md.


 
### Partie 2: Programmes de calcul en Python, utilisation de Numpy et Matplotlib

1. Voici les erreurs commises par la méthode d'Euler explicite pour l'équation y'(t) = 1-y avec y(0) = 5 pour t dans [0,1], en prenant des pas de temps h = 0.2 0.1 0.05 0.025 0.0125 0.00625:

0.2 | 0.07551365552911607

0.1 | 0.03677446949454351

0.05 | 0.01816318138330468

0.025 | 0.008418740234395273

0.0125 | 0.0026797528619485543

0.00625 | 0.0007305381751976648

On constate que plus le pas est petit, plus l'erreur l'est aussi.
Ci-joint dans le mail, notre code pour afficher ces résultats.


## Séance 2: Utilisation de GIT et fin du TP1 Partie 2

### Partie 2: Programmes de calcul en Python, utilisation de Numpy et Matplotlib

1. J'ai rajouté au code l'affichage du graph de convergence, et en pièce jointe l'image de ce graph.