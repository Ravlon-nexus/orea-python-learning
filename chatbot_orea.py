# ==========================================
# PROJET : Le Chatbot Interactif d'Orëa
# Description : Un chatbot insolent et protecteur
# ==========================================

tentative = 0
name = ""

# Le système vérifie les accès au royaume d'Orëa

while tentative < 3:
    name = input("\nQuel est le bon prénom ? ")
    tentative += 1
    
    if name == "Ravlon":
        print("MA ANNA TU ES REVENUE ! *pleure de joie*")
        break
    elif name == "Anna":
        print("Oui mon Ravlon je suis là !!")
        break
    elif name == "Geepee":
        print("Weeeeeeeeeeeeeeeeeeeee Annaaaa! ma petite folle tu m'as manqué !")
        break
    else:
        print("\n(<_____<') t'es qui toi, t'es pas de la famille *poker face agacé*")
        if tentative < 3:
            print("Mauvais profil. Réessaie.")
        
if tentative == 3 and name not in ["Ravlon", "Anna", "Geepee"]:
    print("\nIntrus détecté... protocole de sécurité activé...")
    print("Verrouillage des conversations en cours... Accès bloqué ! 🔒")