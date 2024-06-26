import pandas as pd
import matplotlib.pyplot as plt

# Charger le jeu de données
data = pd.read_csv('./data/Housing.csv')

# Afficher les premières lignes du jeu de données pour vérifier le chargement
print(data.head())

# Histogramme pour la colonne 'bedrooms'
plt.figure(figsize=(10, 6))
plt.hist(data['bedrooms'], bins=range(int(data['bedrooms'].min()), int(data['bedrooms'].max()) + 1), edgecolor='black')
plt.title('Histogramme des Bedrooms')
plt.xlabel('Nombre des Bedrooms')
plt.ylabel('Fréquence')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Graphique nuage de points (scatter plot) pour 'area' et 'price'
plt.figure(figsize=(10, 6))
plt.scatter(data['area'], data['price'], alpha=0.5)
plt.title('Nuage de points de la superficie par rapport au prix')
plt.xlabel('Area')
plt.ylabel('Price')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
