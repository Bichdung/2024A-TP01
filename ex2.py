# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math
water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
assainir5L = water_quantity/5
filtre = math.ceil(assainir5L)
lampesUV = math.ceil(3*assainir5L)
chlore = assainir5L*0.5
if water_quantity % 1 == 0:
    water_quantity = int(water_quantity)

print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:")
print("")
print(f"        \t- Filtre(s) : {filtre}")
print("")
print(f"        \t- Lampe(s) UV : {lampesUV}")
print("")
print(f"        \t- Chlore : {chlore}kg")