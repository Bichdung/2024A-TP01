# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
g = 9.8
speed = float(input("Quel est la vitesse initiale de la boule (en m/s)?"))
angle = math.radians(float(input("Quel est l'angle de lancement? (en degrés)")))
max_distance = ((speed**2 *math.sin(2 * angle)))/g
print("La distance maximale en x est de", round(max_distance, 2), "m.")
