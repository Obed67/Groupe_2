## ------------------ANALYSE DE DONNEES EN R----------------------- 

find_directory <- getwd()
print(find_directory)

# CHARGEMENT DU DATASET.
data <- read.csv("Housing.csv")

##-----------------EXPLORATION INITIALE DES DONNEES----------------

# FAIRE UNE COPIE COMPLETE DU DATASET
df <- data.frame(data)

# COMPRENDRE LA STRUCTURE DES DONNEES (METADONNEES)

# Taille de l'ensemble de données.
head(df)
n <- dim(df)
n

# Afficher les types de données des variables du dataset
sapply(df, typeof)

# Afficher un résumé des variables numériques du dataset 
summary(df)

##---------------------PRETRAITEMENT DES DONNEES--------------------

# Vérification, visualisation et netoyage des valeurs manquantes du dataset
is.na(df)
sum(is.na(df))

library(VIM)
# visualisation des valeurs manquantes du dataset
matrixplot(is.na(df), col = c("blue", "red"), main = "Matrice des valeurs manquantes")

# verifier, visualier et nettoyer si possible les valeurs aberrantes
numeric_var <- df[, sapply(df, is.numeric)]
boxplot(numeric_var, main = "Boxplot de la variable")

# CONCLUSION: on a quelques valeurs aberrante au niveau de la colonne 'price' qu'on pourrait recceuillir et supprimer

# Fonction pour supprimer les valeurs aberrantes basées sur l'IQR
remove_outliers <- function(df, column) {
  Q1 <- quantile(df[[column]], 0.25)
  Q3 <- quantile(df[[column]], 0.75)
  IQR <- Q3 - Q1
  li <- Q1 - 1.5 * IQR
  ls <- Q3 + 1.5 * IQR
  outlier <- ((df[[column]] < (Q1 - 1.5 * IQR)) | (df[[column]] > (Q3 + 1.5 * IQR)))
  return(outlier)
}

# Supprimer les outliers de la colonne 'price'
outliers <- remove_outliers(df, "price")
nbre_outliers <- sum(outliers > 0)
nbre_outliers
pourcentage_outliers <- (nbre_outliers / nrow(df['price'])) * 100
pourcentage_outliers

# CONCLUSION: On constat que dans le jeu de données il n'y a pas des valeurs aberrantes dans 
# les colonnes à valeurs numériques du dataset sauf la colonne 'price' qu'on pourrait receuillir 
# et supprimer de notre jeu de donnée mais on peut aussi les laissé car elles ne sont pas en bon 
# nombre pour affecter avec un pourcentage de 2,75 %.

##-------------------------ANALYSE EXPLORATOIRE DES DONNEES (EDA)----------------------------------

# Charger ggplot2
library(ggplot2)

# Fonction pour créer un histogramme de la colonne 'bedrooms'
histo <- function(df) {
  ggplot(df, aes(x = bedrooms)) +
    geom_histogram(binwidth = 1, fill = "blue", color = "red", bins = 5) +
    ggtitle('Histogramme des Chambres') +
    xlab('Nombre de Chambres') +
    ylab('Fréquence') +
    theme_minimal()
}
histo(df)

# Fonction pour afficher les statistiques descriptives de la colonne 'bedrooms'
describe <- function(df) {
  moyenne <- mean(df$bedrooms, na.rm = TRUE)
  mediane <- median(df$bedrooms, na.rm = TRUE)
  ecartype <- sd(df$bedrooms, na.rm = TRUE)
  cat("La moyenne est:", moyenne, "\n",
      "La médiane est:", mediane, "\n",
      "L'écart-type est:", ecartype, "\n")
}

describe(df)

# Fonction pour créer un graphique de dispersion pour 'area' vs 'price'
nuage_de_point <- function(df) {
  ggplot(df, aes(x = area, y = price)) +
    geom_point(color = "blue", fill = "black", size = 3, shape = 21, stroke = 1.5, alpha = 0.7) +
    ggtitle('Graphique de Dispersion - Surface vs Prix') +
    xlab('Area') +
    ylab('Price') +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5)) +
    geom_point(color = "black", size = 3, shape = 21, alpha = 0.5) # Ajoute les bordures noires aux points
}

nuage_de_point(df)

# Charger les bibliothèques nécessaires
library(corrplot)

# Sélectionner les colonnes 'price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking'
selection_cols <- c('price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking')
numeric_cols <- df[, selection_cols]

# Calculer la matrice de corrélation
corr_matrix <- cor(numeric_cols, use = "complete.obs")
corr_matrix

# Visualiser la matrice de corrélation
corrplot(corr_matrix, method = "circle", type = "upper", 
         tl.col = "black", tl.srt = 45, addCoef.col = "black", 
         col = colorRampPalette(c("blue", "white", "red"))(200), 
         ggtitle("la matrice de corrélation"))
