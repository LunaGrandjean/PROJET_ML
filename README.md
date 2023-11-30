## Projet Machine Learning - Apnée


### Introduction
Le projet vise à explorer les données des compétitions d'apnée, effectuer une analyse exploratoire (EDA), réaliser du clustering pour comprendre les raisons d'obtention de cartons rouges, et enfin, prédire les résultats des plongées.


### Fichiers
data/:
* raw/: Contient le fichier CSV original et éventuellement d'autres données brutes.
* processed/: Données transformées et nettoyées prêtes pour l'analyse.

notebooks/:
* exploration.ipynb: Notebook Jupyter pour l'exploration des données, y compris la visualisation.
* preprocessing.ipynb: Notebook pour le nettoyage et la préparation des données.

src/ :
* data_preprocessing.py: Script pour le nettoyage et la préparation des données.
* data_analysis.py: Script pour l'analyse des données.
* model.py: Script pour la construction et l'entraînement du modèle ML.
* utils.py: Fonctions utilitaires communes.

models/:
Dossiers pour les modèles sauvegardés, par exemple après l'entraînement.
requirements.txt ou environment ymI : Liste des dépendances nécessaires pour exécuter le projet.
gitignore: Fichier pour exclure des fichiers/dossiers spécifiques du dépôt (par exemple, fichiers de données volumineux, fichiers de configuration personnels).

tests/:
Scripts de tests pour valider les fonctions dans 'src/*

docs/: Documentation supplémentaire.


### Data cleaning
On a pris des décisions après analyse de la quantité de données manquantes et leurs source (détails dans le notebook *preprocessing*):
* Transformer comme demandé les données qui étaient sous formes de str en int pour faciliter l'analyse.
* Transformer les données manquantes sous forme de () ou autre en Nan ou null.
* Supprimer toutes les lignes avec des données manquantes car elles représentaient une partie négligeable du dataset.
* Ajouter les colonnes Year et Month pour pouvoir faire des visualisations en fonction de ces données spécifiquement.
