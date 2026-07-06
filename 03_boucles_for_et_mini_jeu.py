# ==========================================================
# PARTIE 3 : LES BOUCLES FOR, LES LISTES ET PREMIER GAMEPLAY
# ==========================================================

# ===== EXERCICE 1 : Le Sergent d'Orëa fait l'appel =====
print("--- Appel des Gardiens ---")
prenoms = ["Anna", "Ravlon", "Loutre", "Eden"]

for prenom in prenoms:
    if prenom == "Anna":
        print(prenom, "est la gardienne principale")
    elif prenom == "Ravlon":
        print(prenom, "veille sur le portail")
    else:
        print(prenom, "est présent au conseil")




# -----------------------------------------------



# ===== EXERCICE 2 : Le Filtre Magique (Lettre 'A') =====
print("\n--- Analyse des noms (recherche de la lettre 'A') ---")
for gardien in prenoms:
    if "a" in gardien.lower():
        print(f"-> {gardien} contient un 'a'")



# -----------------------------------------------




# ===== EXERCICE 3 : L'Analyseur de Données du Nexus =====
print("\n--- Tri et Statistiques des Nombres ---")
nombres = [3, 8, 12, 5, 20, 1]
total_pair = 0
total_impair = 0

for nombre in nombres:
    if nombre % 2 == 0:
        print(nombre, "est pair")
        total_pair += 1
    else:
        print(nombre, "est impair")
        total_impair += 1
        
print("Il y a", total_pair, "nombres pairs")
print("Il y a", total_impair, "nombres impairs")




# -----------------------------------------------



# ===== EXERCICE 4 : GAMEPLAY I - Le Portail d'Orëa =====
print("\n==================================================")
print("=== BIENVENUE À ORËA : LE PORTAIL (MINI-JEU) ===")
print("==================================================")

choix = input("Tu vois un portail. Tu entres ? (oui / non / fuir) : ")

if choix.lower() == "oui":
    print("\nLe portail s'ouvre devant toi...")
    print("Tu arrives dans une salle gigantesque ornée de moulures dorées.")
    print("De grands cristaux lumineux flottent comme des chandeliers.")
    print("Tu avances prudemment. Il fait froid, un doux parfum chatouille tes narines...")
    print("Un coffre attire ton attention. Alors que tu t'en approches, l'image d'un homme apparaît.")
    print("Tu réalises que c'est un hologramme. Il ne te voit pas, mais déclame un discours, tel un dramaturge :")
    print("'QUI SAURA OUVRIR LE COFFRE, À CELUI-CI UNE CLEF SERA DONNÉE !'")
    
    mot_de_passe = input("\nQuel est le mot de passe ? : ")
    if mot_de_passe.lower() == "ouvre toi":
        print("\nLe coffre s'ouvre !")
        print("Tu trouves une pierre semblable au topaze.")
        print("Le vent se lève, une porte en forme de serrure apparaît entre toi et le coffre.")
    elif mot_de_passe.lower() == "frapper le coffre":
        print("\nLe coffre ne bouge pas d'un poil... Et tu as mal à la main. (._. )")
    elif mot_de_passe.lower() == "partir":
        print("\nTu t'éloignes du coffre, mais la sortie a mystérieusement disparu !")
    else:
        print("\nTu ne fais rien, le temps s'écoule lentement...")
        
elif choix.lower() == "non":
    print("\nTu restes devant le portail, hésitante, à scruter les reflets de la pierre.")
elif choix.lower() == "fuir":
    print("\nLe portail t'aspire soudainement dans un vortex ! Tu disparais en poussant un long cri...")
else:
    print("\nLe portail ne comprend pas ta réponse divine...")