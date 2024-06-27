# RAPPORT DU PROJET

## TACHE 2 : Tracé de Graphiques et Analyse de Données

Faire une analyse de données avancée en Python ou R implique plusieurs étapes, allant de la compréhension des données brutes à la communication ou interprétation des résultats issue des différents graphes affichés. Voici les principales étapes détaillées :

### 1. COMPREHENSION ET PREPARATION DES DONNEES (Prétraitement)

- **Collecte des données**
  Elle consiste généralement à récupérer les données brutes, par exemple en utilisant un fichier 'Housing.csv' téléchargé depuis Kaggle, pour une analyse ultérieure en Python ou en R.

- **Exploration initiale des données dans 'Housing.csv'**
  Cette étape vise à comprendre la structure des données (métadonnées) :
  - La taille du dataset est 543 lignes et 13 colonnes.
  - Information sur les colonnes : 'price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking', ‘mainroad’, ‘guestroom’, ‘basement’, ‘Hotwaterheating’, ‘airconditioning’, ‘prefarea’, ‘Furnishingstatus’.
  - Un résumé statistique sur le dataset ‘Housing.csv’.

- **Nettoyage des données**
  - Il n’y a pas de valeurs manquantes dans le dataset après vérification et visualisation.
  - Seule la colonne ‘price’ contient 15 valeurs aberrantes, ce qui représente 2.75% du total.

### 2. ANALYSE EXPLORATOIRE DES DONNEES (EDA)

Pour les visualisations dans une analyse de données, on utilise généralement la bibliothèque matplotlib.pyplot en Python et ggplot en R.

- **Visualisation de la colonne ‘bedrooms’**
  - **CONCLUSION** : d’après la distribution de la colonne ‘bedrooms’, elle semble symétrique.

- **Graphiques de dispersion de la colonne ‘area’ et ‘price’**
  - **CONCLUSION** : ce graphe permet une compréhension approfondie de la relation entre la surface et le prix des propriétés dans le jeu de données, ainsi que la détection des valeurs aberrantes.

- **Matrix de corrélation du dataset avec ‘ggplot’**
  - **CONCLUSION** : la matrice de corrélation est importante pour la sélection des features, elle permet de visualiser les relations entre les colonnes du dataset. On peut conclure ici qu'il n’y a pas de forte corrélation entre les colonnes de notre jeu de données.
