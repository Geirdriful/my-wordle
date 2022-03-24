# My-Wordle

Développement d'un wordle similaire à https://wordle.louan.me/ sur une vm Debian 8 server. 

Le principe reste le même : selection d'un mot de 5 lettres. 6 essais pour trouver le mot.

Si dans le mot proposé, une lettre est à la bonne place elle s'affiche en verte

Si dans le mot proposé, une lettre est présente dans le mot a deviné mais pas à la bonne place elle s'affiche en orange

## Build status

23/03/2022 : jeu fonctionnel en ligne de commande

roadmap :
- ajouter une interface graphique (à voir car la VM de dev est une version sans interface)
- se baser sur l'api de DICOLINK pour choisir un mot
- blocage à un mot par jour
- augmenter la difficulté en augmentant la longueur du mot du jour

## Sommaire

* [Captures d’écrans du projet](#Captures-décrans-du-projet)
* [Getting Started](#Getting-Started)
* [Tests](#Tests)
* [Build](#Build)
* [Déploiement](#Déploiement)
* [Documentations externes](#Documentations-externes)
* [Contribuer](#Contribuer)
* [Versioning](#Versioning)

## Captures d’écrans du projet

![image](https://user-images.githubusercontent.com/66006065/159879682-93925fb2-3c95-4f82-b62a-0f410c0a601c.png)

## Getting Started

Les instructions à suivre pour récupérer une version du projet et le faire tourner localement à des fins de développement et de test. Se référer à la section déploiement pour déployer sur un environnement. 

### Pré-requis
- Avoir python3 d'installer
 Installer python3
 ```
 (sudo) apt-get install python3
 ```
 
 Assurez vous que votre environnement de dev a accès à internet
 
### Installation

Je developpe sur une VM distante en passant par VisualStudioCode depuis Windows 10. Cette installation portera sur un environnement de developpement similaire.

Etape 1:
Si vous n'avez pas déjà Python3, installez le en suivant la section Pré-requis.

Etape 2:
Si cela n'est pas déjà fait, vous pouvez installer VisualStudioCode sur votre machine Windows 10 (ou tout autre IDE).

Etape 3:
Connectez vous avec VSC (ou avec un autre IDE) sur la VM configurée précédement puis entrez la commande suivante afin de lancer le téléchargement du projet :
```
git pull git@github.com:Geirdriful/my-wordle.git
```

Etape 4:
Une fois le téléchargement du projet terminé, déplacez vous dans le répertoire du projet puis lancez la commande suivante pour exécuter le jeu :
```
./wordle.py
```

Etape 5:
Si tout est OK, vous devriez avoir quelque chose qui ressemble à cela :

![image](https://user-images.githubusercontent.com/66006065/159884868-94b5250e-22b5-431b-9b25-63a195a1169d.png)


"""
### Tests coding style

Expliquer les standards de code pour les tests

## Build

Comment builder le projet et lancer la chaîne CI

## Déploiement

Comment déployer sur un environnement
"""

## Documentations externes

Ajouter doc DICOLINK pour utilisation API (https://www.dicolink.com/)

## Contribuer
Fonctionne sur le principe de workflow centralisé

- Chaque contributeur clone le projet en local (pour avoir la dernière version du projet) - git clone
- Dev d'une nouvelle fonctionnalité en local - git add / git commit
- Pull de la dernière version du projet (au cas ou il y ai eu des nouvelles fonctionnalités) - git pull
- Résolution des conflits si besoin
- Push de la nouvelle fonctionnalité - git push

