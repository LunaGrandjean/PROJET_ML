## Projet Machine Learning - Apnée

### Introduction
Le projet vise à explorer les données des compétitions d'apnée, effectuer une analyse exploratoire (EDA), réaliser du clustering pour comprendre les raisons d'obtention de cartons rouges, et enfin, prédire les résultats des plongées.

### Fichiers
data/:
* raw/: Contient le fichier CSV original et éventuellement d'autres données brutes.
* processed/: Données transformées ou nettoyées prêtes pour l'analyse.

notebooks/:
• exploration.ipynb: Notebook Jupyter pour l'exploration des données, y compris la visualisation.
• preprocessing.ipynb: Notebook pour le nettoyage et la préparation des données.

src/ :
• data_preprocessing.py: Script pour le nettoyage et la préparation des données.
• data_analysis.py: Script pour l'analyse des données.
• model.py: Script pour la construction et l'entraînement du modèle ML. utils.py: Fonctions utilitaires communes.

models/:
Dossiers pour les modèles sauvegardés, par exemple après l'entraînement.
requirements.txt ou environment ymI : Liste des dépendances nécessaires pour exécuter le projet.
gitignore: Fichier pour exclure des fichiers/dossiers spécifiques du dépôt (par exemple, fichiers de données volumineux, fichiers de configuration personnels).

tests/:
Scripts de tests pour valider les fonctions dans 'src/*

docs/: Documentation supplémentaire.
