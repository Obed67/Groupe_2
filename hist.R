# Chargement des bibliothèques nécessaires
library(ggplot2)

# Chargements du dataset
data <- read.csv('./data/Housing.csv')

# Afficher les premières lignes du jeu de données pour vérifier le chargement
head(data)

# Histogramme pour la colonne 'bedrooms'
ggplot(data, aes(x = bedrooms)) +
  geom_histogram(binwidth = 1, color = "black", fill = "blue", alpha = 0.7) +
  labs(title = "Histogramme de Bedrooms", x = "Nombre de Bedrooms", y = "Fréquence") +
  theme_minimal()

# Graphique nuage de points (scatter plot) pour 'area' vs 'price'

ggplot(data, aes(x = area, y = price)) +
  geom_point(alpha = 0.5) +
  labs(title = "Nuage de points de la relation entre Area et Price", x = "Area", y = "Price") +
  theme_minimal()