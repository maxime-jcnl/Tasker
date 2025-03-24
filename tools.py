import tkinter as tk
from tkinter import filedialog
import os
from collections import deque

def lire_tableau_contraintes():
    # retourne donc un dictionnaire avec comme clé le n° de la tache et en valeur un tuple (durée, liste de prédesseur)
    root = tk.Tk()
    root.withdraw()
    fichier = filedialog.askopenfilename(
        title="Sélectionner un fichier de tableau de contraintes",
        filetypes=[("Fichiers texte", "*.txt")]
    )

    if not fichier or not os.path.isfile(fichier):
        print("Aucun fichier valide sélectionné.")
        return None

    contraintes = {}

    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                elements = list(map(int, ligne.strip().split()))
                if len(elements) < 2:
                    continue  # pr éviter les erreurs de formatage

                tache = elements[0]
                duree = elements[1]
                predecesseurs = elements[2:] if len(elements) > 2 else []

                contraintes[tache] = (duree, predecesseurs)

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

    return contraintes
def construire_graphe_avec_fictifs(contraintes: dict) -> list:
    if not contraintes:
        return None
    tasks = sorted(contraintes.keys()) # récup les taches de manière triées
    N = max(tasks) # N contiendra le nombre de taches
    taille = N + 2  # ( N + sommet fictif 0 + sommet fictif n+1)
    matrice = [['*' for _ in range(taille)] for _ in range(taille)] # crée une matrice carrée de "*" (réprésente vide)

    for t in tasks: # pour chaque task
        _, preds = contraintes[t] # récuper la liste des prédesseurs de la task
        if not preds:  # si aucun préd, on crée un arc de 0 à la tasl
            matrice[0][t] = 0

    for t in tasks: # ajoute les arc dans la matrice
        _, preds = contraintes[t]
        for pred in preds:
            if pred in contraintes:
                duree_pred = contraintes[pred][0]
                matrice[pred][t] = duree_pred

    taches_avec_successeur = set() # on utilise un set pr eviter les doublons
    for t in tasks:
        for (_, preds) in contraintes.values(): # On vérifie si la tâche "t" est présente dans la liste des prédécesseurs d'une autre tâche.
            if t in preds:
                taches_avec_successeur.add(t) # on l'ajoute et on stop (pas besoin de vérifier plein de fois)
                break

    fin = N + 1
    for t in tasks: # On lie les tache sans successeur au sommet fictif n+1
        if t not in taches_avec_successeur:
            duree, _ = contraintes[t]
            matrice[t][fin] = duree
    return matrice
def afficher_matrice(matrice: list):
    if not matrice:
        print("Aucune matrice à afficher.")
        return

    taille = len(matrice)
    header = "     " + "  ".join(f"{i:>3}" for i in range(taille))
    print(header)
    for i, ligne in enumerate(matrice):
        ligne_str = "  ".join(f"{elem:>3}" for elem in ligne)
        print(f"{i:>3}  {ligne_str}")
def detecter_cycle(matrice):
    n = len(matrice) # n = nb de tache de la matrice (fictifs compris)
    indegree = [0] * n # degrée entrant
    for i in range(n): # pour chaque sommet
        for j in range(n):
            if matrice[i][j] != '*' and isinstance(matrice[i][j], int): # verifie qu'il y a un entier
                indegree[j] += 1 # Si "i -> j" existe on ajoute +1 au degré entrant de j

    queue = deque()
    for i in range(n): #
        if indegree[i] == 0:
            queue.append(i) #ajoute a la file tous les sommets sans prédecesseur
    count = 0

    while queue: # algorithme de Kahn
        u = queue.popleft()
        count += 1
        for v in range(n):
            if matrice[u][v] != '*' and isinstance(matrice[u][v], int):
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

    return count != n
def verifier_arcs_negatifs(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            valeur = matrice[i][j]
            if isinstance(valeur, int) and valeur < 0:
                print(f"️Arc négatif détecté : {i} → {j} = {valeur}")
                return False
    return True
