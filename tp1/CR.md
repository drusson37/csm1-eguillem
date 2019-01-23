**Nom/Prénom :** Guillem Eloïse 

# Rapport TP1


## Partie 1: Environnement de travail, premiers pas avec git

 1. Choix de l'environnement de travail
 
 Mon environnement de travail est constitué du **terminal** par défaut de l'environnement du Cremi, et de **emacs**.
 
 2. Clonage du dépôt Git
 
 Grâce à la commande **git clone** suivie de https://github.com/upici/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif.git dans le terminal , un répertoire a été créé dans mon répertoire courant. Le nom de ce répertoire est : **Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif**.
 
 3. Familiarisation avec le contenu du répertoire

- Les fichiers md, contiennent du code dans le langage **Markdwon**. _README.md_ contient l'énoncé et les questions du TP. _CR.md_ est le fichier contenant le compte-rendu de ma séance de TP.

- Les fichiers py, sont des fichiers de *programmes* en **Python**.

- L'image _ecran01.png_ est l'image référencée dans le README.md.


 
## Partie 2: Programmes de calcul en Python, utilisation de Numpy et Matplotlib

1. Voici les erreurs commises par la méthode d'Euler explicite pour l'équation **y'(t) = 1-y² **avec **y(0) = 5** pour t dans [0,1]:


| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.07551365552911607      |   |   |   |
| 0.1     | 0.03677446949454351      |   |   |   |
| 0.05    | 0.01816318138330468      |   |   |   |
|  0.025  | 0.008418740234395273     |   |   |   |
| 0.0125  | 0.0026797528619485543    |   |   |   |
| 0.00625 |    0.0007305381751976648 |   |   |   |

On constate que plus le pas est petit, plus l'erreur l'est aussi.

 J'ai rajouté au code l'affichage du **graph de convergence**:
 
 <img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/grapherreurq1.png">
 
 
C'est à dire, on trace à partir de ces résultats: la courbe de l'erreur relative en fonction de h, en échelle logarithmique.

2. a/ Voici les erreurs commises par la méthode d'Euler explicite pour l'équation **y'(t) = 1-y² **avec **y(0) = 0 **pour t dans [0,1]:

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.051542711647093474     |   |   |   |
| 0.1     | 0.025230901150132257     |   |   |   |
| 0.05    | 0.012443814368973037     |   |   |   |
|  0.025  | 0.006178101429809816     |   |   |   |
| 0.0125  | 0.0028708761597393104    |   |   |   |
| 0.00625 |    0.0008973099322736569 |   |   |   |

Ainsi que le **graph de convergence** correspondant :


 <img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/grapherreurq2.png">
 

b/ Voici les erreurs commises par la méthode d'Euler explicite pour l'équation **y'(t) = 1-y² **avec **y(0) = 2 ***pour t dans [0,1]:

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 1.2056454817778384       |   |   |   |
| 0.1     | 1.9761765033790237       |   |   |   |
| 0.05    | 2.4479182119578877       |   |   |   |
|  0.025  | 2.712527275197839        |   |   |   |
| 0.0125  | 2.853204867600841        |   |   |   |
| 0.00625 |        2.925810657011926 |   |   |   |

Ainsi que le **graph de convergence** correspondant :


 <img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/grapherreurq2b.png">
 


*Dans la suite on s'intéressera toujours à l'équation y'(t) = 1-y² que l'on traitera avec des méthodes différentes.*

3. On s'intéresse maintenant à Runge Kutta 2  (RK2) :  y_{n+1} = y_n + h*f(t_n+0.5*h,y_n+0.5*f(y_n))

a/ De la même manière que précédemment, on obtient les erreurs relatives selon les pas de temps.

Pour **y(0) = 0** :

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.0018411439066010615    |   |   |   |
| 0.1     | 0.0004309701745974781    |   |   |   |
| 0.05    | 0.00010399118583059863   |   |   |   |
|  0.025  | 2.5528167184263317e-05   |   |   |   |
| 0.0125  | 6.323422493736963e-06    |   |   |   |
| 0.00625 |   1.5735372290714977e-06 |   |   |   |



On compare les courbes du **graph de convergence** de RK2 et Euler Explicite:


 <img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/3a.png">
 

b/ Pour **y(0) = 2 **:

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.046538941587258575     |   |   |   |
| 0.1     | 0.008960178608243385     |   |   |   |
| 0.05    | 0.00196632618937298      |   |   |   |
|  0.025  | 0.0004574160075347944    |   |   |   |
| 0.0125  | 0.00011034792737540933   |   |   |   |
| 0.00625 |   2.7102475435025752e-05 |   |   |   |

On remarque que RK2 plus efficace qu'Euler Explicite, d'après la comparaison des courbes (de RK2 et Euler Explicite) du **graph de convergence** correspondant :

 <img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/3b.png">

4. On utilise maintenant la méthode du point milieu : y_{n+1} = y_{n-1} + 2*h*f(t_n,y_n), y_1 calculé par la méthode RK2.


a/ Pour **y(0) = 0 **:

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.004369437744775051     |   |   |   |
| 0.1     | 0.0010665334989954367    |   |   |   |
| 0.05    | 0.0002612810011757838    |   |   |   |
|  0.025  | 6.427941171555096e-05    |   |   |   |
| 0.0125  | 1.5945627627023118e-05   |   |   |   |
| 0.00625 |    3.971242142963849e-06 |   |   |   |


Le **graph de convergence** correspondant :

<img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/4.png">

Le graph de **comparaison des courbes de convergence des trois méthodes (RK2,Euler Explicite et Point milieu) **:

<img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/4compa.png">

b/ Pour **y(0) = 2** :

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.13770469255595308      |   |   |   |
| 0.1     | 0.010576976531172955     |   |   |   |
| 0.05    | 0.0020494953659644377    |   |   |   |
|  0.025  | 0.0005387764719391175    |   |   |   |
| 0.0125  | 0.00013403491303987103   |   |   |   |
| 0.00625 |    3.320397284811705e-05 |   |   |   |

Le **graph de convergence** correspondant :

<img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/4b.png">

Le graph de **comparaison des courbes de convergence des trois méthodes (RK2,Euler Explicite et Point milieu) **:

<img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/4compab.png">

En comparant Euler Explicite, RK2 et la méthode du point milieu, on voit que c'est RK2 qui est le plus efficace (c'est avec cette méthode que l'erreur est la plus faible).

5. On s'intéresse maintenant à la méthode du trapèze: y_{n+1} = y_n + 0.5*h*( f(t_n,y_n) + f(t_{n+1},y_{n+1}).
On utilise pour cela la méthode dite de prédiction/correction:
Prédiction: y_* = y_n + h*f(t_n,y_n)
Correction: y_{n+1} = y_n + 0.5*h*( f(t_n,y_n) + f(t_{n+1},y_*) ) 

 a/ Pour **y(0) = 0**:
 
| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.005884470097676564     |   |   |   |
| 0.1     | 0.0013287762811675652    |   |   |   |
| 0.05    | 0.000315732166490279     |   |   |   |
|  0.025  | 7.695770254201317e-05    |   |   |   |
| 0.0125  | 1.8997570096490612e-05   |   |   |   |
| 0.00625 |   4.7194734267286265e-06 |   |   |   |

Le **graph de convergence** correspondant :

<img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/5.png">

b/ Pour **y(0) = 2**:

| Pas h   | Erreur relative associée |   |   |   |
|---------|--------------------------|---|---|---|
| 0.2     | 0.02853894158725856      |   |   |   |
| 0.1     | 0.006356659480775573     |   |   |   |
| 0.05    | 0.0014540286536903757    |   |   |   |
|  0.025  | 0.0003455803659389023    |   |   |   |
| 0.0125  | 8.42587831753061e-05     |   |   |   |
| 0.00625 |   2.0794139891533447e-05 |   |   |   |

Le **graph de convergence** correspondant :

<img src = "/net/cremi/eguillem/Utilisation-de-Plateforme-Industrielle-pour-le-Calcul-Intensif/csm1-eguillem/tp1/5b.png">

