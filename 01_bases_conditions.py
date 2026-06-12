# ==========================================================
# PROJET : Les Fondations du Code - Les Conditions en Python
# Description : Maîtrise des structures fondamentales (if, elif, else)
#               Gestion des entrées utilisateurs et de la logique
# ==========================================================

print("=== EXERCICE 1 : Choix du mode utilisateur ===")
nom = input("Comment t'appelles-tu ? ")
choix = input("Choisis un mode (1 pour chill, 2 pour motivée) : ")

if choix == "1":
    print("Ok", nom, ", on reste tranquille aujourd'hui :)")
elif choix == "2":
    print("Ok", nom, ", aujourd'hui tu avances !")
else:
    print("Choix inconnu, mais t'es quand même cool :p")


print("\n=== EXERCICE 2 : Qualification des tranches d'âge ===")
age = int(input("Quel âge as-tu ? : "))

if age < 0:
    print("Âge invalide")
elif age > 120:
    print("Euh... tu viens du futur ou quoi ?")
elif age < 18:
    print("Tu es mineur")
else:
    print("Tu es majeur")


print("\n=== EXERCICE 3 : Système de contrôle d'accès ===")
score_francais = int(input("Note de français (sur 20) : "))
score_maths = int(input("Note de maths (sur 20) : "))

if score_francais >= 10 and score_maths >= 10:
    print("Félicitations, tu as validé tes deux matières !")
elif score_francais >= 10 or score_maths >= 10:
    print("Tu as validé une seule matière, accroche-toi !")
else:
    print("Rattrapages nécessaires, tu feras mieux la prochaine fois !")