from tools import *



if __name__ == "__main__":
    tableau = lire_tableau_contraintes()
    if tableau:
        print("Tableau des contraintes lu avec succès :")
    matrice = construire_graphe_avec_fictifs(tableau)
    afficher_matrice(matrice)