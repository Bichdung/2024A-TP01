# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input(" What's the battery level ?"))
resultat =0

if battery_level > 50 : resultat += (battery_level-50)*2 ; battery_level -= battery_level-50

if battery_level > 25 : resultat += (battery_level-25)*0.5 ; battery_level -= battery_level-25

if battery_level > 10 : resultat += (battery_level-10)*1 ; battery_level -= battery_level-10

if battery_level > 5 : resultat += (battery_level-5)*2.5 ; battery_level -= battery_level-5

if battery_level > 0 : resultat += battery_level*6

print(resultat, " km")