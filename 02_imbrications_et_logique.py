# ==========================================================
# PROJET : Logique Avancée - Les Conditions Imbriquées
# Description : Maîtrise des structures complexes, des vérifications 
#               multiples (if dans un if) et des opérateurs (and/or)
# ==========================================================

print("=== EXERCICE 1 : Le Vigile d'Orëa (V1) ===")
age = int(input("Quel est ton âge ? : "))
    
if age < 0:
    print("Âge invalide")
elif age < 18:
    print("Accès refusé")
else:
    # Condition imbriquée : on est majeur, donc on vérifie le mot de passe !
    mot_de_passe = input("Quel est le mot de passe ? : ")
    if mot_de_passe == "Orëa":
        print("Bienvenue dans Orëa ;)")
    else:
        print("Mot de Passe incorrect")


print("\n=== EXERCICE 2 : Analyseur de Nombres (Pairs et Impairs) ===")
nombre = int(input("Choisis un nombre : "))

if nombre < 0:
    print("Nombre négatif")
elif nombre == 0:
    print("Ce nombre est nul")
else:
    # Condition imbriquée : le nombre est positif, est-il pair ou impair ?
    if nombre % 2 == 0:
        print("Nombre positif et pair")
    elif nombre % 2 == 1:
        print("Ce nombre est positif et impair")


print("\n=== EXERCICE 3 : Double Vérification des Identifiants ===")
name = input("Quel est ton nom ? ")
motdepasse = input("Quel est le mot de passe ? ")

if name == "Anna" and motdepasse == "Ravlon":
    print("Bienvenue à Orëa Anna !")
elif name == "Anna" and motdepasse != "Ravlon":
    print("Mot de passe incorrect")
elif name != "Anna" and motdepasse == "Ravlon":
    print("Nom inconnu.")
else:
    print("Accès refusé.")