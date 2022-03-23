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

CAPTURE ECRAN A AJOUTER

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
Voir commande git a tester pour DL le projet
```

Etape 4:
Une fois le téléchargement du projet terminé, déplacez vous dans le répertoire du projet puis lancez la commande suivante pour exécuter le jeu :
```
./wordle.py
```

Etape 5:
Si tout est OK, vous devriez avoir quelque chose qui ressemble à cela :
CAPTURE ECRAN

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

Si nécessaire, ajouter des informations ou des liens vers les documentations externes. Cela peut être un lien vers la documentation applicative, un lien vers la documentation de webservices utilisés, etc.

## Contribuer
Détailler le workflow centralisé
Un lien vers la documentation permettant de contribuer au projet, comment soumettre une pull request, une anomalie, etc.

### Code style

Donner les informations pour répondre aux standards de code

## Versioning

Indiquer la méthode de versioning, SemVer de préférence. 

## License

Indiquer la licence du projet s’il y en a une et/ou les éléments légaux


