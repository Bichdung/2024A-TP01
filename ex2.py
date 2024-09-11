# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = int(input("Quel est la quatité d'eau à assinir (en L)"))
assainir5L = water_quantity/5
filtre = assainir5L
lampesUV = 3*assainir5L
chlore = assainir5L/2
print("Il faudra" , filtre , "filtres," , lampesUV , "lampes UV et" , chlore , "kg de chlore.")