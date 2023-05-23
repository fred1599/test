# Mon Projet Python

## Architecture du projet de test

Voici la structure du projet :

```
tests
├── data.log
├── Dockerfile
├── __init__.py
├── main.py
├── Makefile
├── README.md
├── requirements.txt
├── run_app.sh
└── test.py
```


## Comment lancer le projet

Nous utilisons Docker pour faciliter la configuration de l'environnement de développement. Voici les commandes disponibles :

- Pour construire l'image Docker de votre application, exécutez : `make build`
- Pour exécuter les tests unitaires, exécutez : `make run-tests`
- Pour exécuter l'application, exécutez : `make run-app`
- Pour exécuter l'application en mode débogage, exécutez : `make run-debug`

## Configuration de l'IDE

Nous utilisons Visual Studio Code (VSCode) comme environnement de développement intégré (IDE). Voici une configuration typique pour le débogage avec VSCode :

Fichier `launch.json`

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Attach",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5679
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "/app"
                }
            ]
        }
    ]
}


Cette configuration vous permet de vous connecter à une application Python en cours d'exécution sur le port 5679 pour le débogage.

Explication du code et Typer

Le projet est basé sur un script Python principal (main.py) qui analyse et traite un fichier texte (data.log). Il utilise le module Typer pour faciliter la création d'une interface de ligne de commande.

Typer est une bibliothèque pour créer des applications en ligne de commande. Elle est basée sur Python 3.6+ type hints.

Avec Typer, vous pouvez définir des commandes en créant des fonctions Python standard avec des annotations de type. Typer prend ensuite ces annotations de type et les convertit en arguments de ligne de commande. Par exemple, dans notre script principal, nous utilisons Typer pour lire le chemin d'un fichier comme argument de ligne de commande.

De plus, ce projet contient également une suite de tests unitaires (test.py) pour tester les fonctionnalités principales du script. Ces tests peuvent être exécutés avec l'outil de test pytest.

Pour plus d'informations sur Typer, veuillez consulter la documentation officielle à l'adresse suivante : https://typer.tiangolo.com/
