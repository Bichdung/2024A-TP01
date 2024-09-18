#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
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
print(f"{country}:")
#print("Résultat du pays: ", code_medals)
print(f"- {G_medal} OR")
print(f"- {S_medal} Argent")
print(f"- {B_medal} Bronze")
