# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
g = 9.8
speed = float(input("Vitesse initiale (m/s): "))
angle = math.radians(float(input("Angle de lancer (en degrés): ")))
max_distance = ((speed**2 *math.sin(2 * angle)))/g
print(f"Distance parcourue: {round(max_distance, 2)}m")
