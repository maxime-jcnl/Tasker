from tools import *


def main():
    print("=== TASKER ===\n")
    continuer = True
    while continuer:
        contraintes = lire_tableau_contraintes()
        if contraintes is None:
            print("Erreur de lecture du fichier. Réessayer.\n")
            continue

        matrice = construire_graphe_avec_fictifs(contraintes)
        print("\n--- Matrice du graphe d'ordonnancement ---")
        afficher_matrice(matrice)

        print("\n--- Vérifications ---")
        has_cycle = detecter_cycle(matrice)
        has_negative = not verifier_arcs_negatifs(matrice)

        if has_cycle:
            print("Le graphe contient un CYCLE. Il n'est pas valide pour l'ordonnancement.\n")
        elif has_negative:
            print("Le graphe contient des ARCS NÉGATIFS. Il n'est pas valide pour l'ordonnancement.\n")
        else:
            print("Le graphe est VALIDE pour l'ordonnancement !\n")
            # suite du prog
        reponse = input("Voulez-vous tester un autre fichier ? (o/n) : ").strip().lower()
        if reponse != 'o':
            continuer = False
            print("\nFin du programme.")

if __name__ == "__main__":
    main()
