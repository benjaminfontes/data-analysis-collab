print('hello')
import pandas as pd

# 1. Charger le fichier CSV situé dans le dossier data
df = pd.read_csv('data/ventes.csv')

# 2. Calculer le chiffre d'affaires pour chaque ligne (quantité x prix unitaire)
df['chiffre_affaires'] = df['quantite'] * df['prix_unitaire']

# 3. Calculer le chiffre d'affaires total de toutes les ventes
ca_total = df['chiffre_affaires'].sum()

# 4. Afficher le résultat
print(f"Le chiffre d'affaires total est de : {ca_total} €")