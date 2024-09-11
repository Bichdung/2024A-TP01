#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Quel est le nom du pays?")
code_medals = input("Quel est le code pour les médailles?")
G_medal = 0
S_medal = 0
B_medal = 0
for letter in code_medals:
    if letter == "G":
        G_medal = G_medal+1
    elif letter == "S":
        S_medal = S_medal+1
    elif letter == "B":
        B_medal = B_medal+1
    else:
        print("Il y a un ou des caractères invalides")
print(country)
print("Résultat du pays: ", code_medals)
print("Médailles: -Or:", G_medal, "-Argent:", S_medal, "-Bronze:", B_medal)
