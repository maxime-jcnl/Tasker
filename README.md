Voici un **README clair et concis** pour ton projet Python d’ordonnancement, suivi d’une **TODO list structurée** pour la suite du développement 👇

---

# 📘 README – Projet ORDONNANCEMENT

## 🎯 Objectif

Ce programme vise à **lire un fichier de contraintes** de tâches, construire le **graphe d’ordonnancement correspondant** (avec sommets fictifs), et **vérifier** qu’il est valide pour une analyse d’ordonnancement.

---

## 🧱 Structure actuelle du projet

### 📂 Fichiers principaux
- `main.py` : point d’entrée du programme, boucle sur les fichiers à tester
- `tools.py` ou équivalent : contient toutes les fonctions utilitaires (lecture, construction, vérif, affichage…)

---

## ⚙️ Fonctionnement actuel

### 1. Lecture du fichier
- Via une fenêtre Tkinter (`filedialog`)
- Retourne un **dictionnaire** de la forme :
```python
{tache: (durée, [liste_des_prédécesseurs])}
```

### 2. Construction du graphe
- Création d’une **matrice d’adjacence** de taille `(N+2)x(N+2)`
- Intègre :
  - Le **sommet fictif 0** : début du projet
  - Le **sommet fictif N+1** : fin du projet
- Chaque arc est représenté par la **durée du prédécesseur**

### 3. Vérifications
- **Détection de cycle** via l’algorithme de Kahn (tri topologique)
- **Détection d’arcs négatifs**

### 4. Affichage
- Affiche la **matrice** du graphe
- Affiche les **résultats des vérifications**

---

## 📊 Représentation des données

La **matrice** est une `list` de `list`, où :

- `matrice[i][j] = '*'` : pas d’arc de i vers j
- `matrice[i][j] = x` : il y a un arc de i vers j, avec une valeur x (durée du prédécesseur i)

---

## ✅ Ce qui est déjà fait

- Lecture du fichier `.txt`
- Création du graphe avec sommets fictifs
- Détection de cycle
- Vérification des arcs négatifs
- Affichage de la matrice
- Interface utilisateur pour tester plusieurs fichiers

---

# 📝 TODO LIST – Suite du développement

### 🔄 Étape 4 : Calcul des **rangs**
- [ ] Implémenter la fonction `calculer_rangs(matrice)`
- [ ] Afficher les rangs pour chaque sommet
- [ ] S’assurer que le calcul fonctionne bien avec les sommets fictifs

### ⏱️ Étape 5 : **Calendriers au plus tôt / au plus tard**
- [ ] Calculer la date au plus tôt de chaque sommet (en se basant sur les rangs)
- [ ] Calculer la date au plus tard (avec durée totale connue)
- [ ] Convention : la date au plus tard de fin = date au plus tôt de fin

### ➖ Étape 6 : **Calcul des marges**
- [ ] Calcul des marges totales pour chaque tâche
- [ ] Identifier les tâches avec marge nulle

### 🔴 Étape 7 : **Chemins critiques**
- [ ] Déterminer les **chemins critiques**
- [ ] Afficher tous les chemins avec marge nulle menant du sommet 0 à N+1

### 🧪 Étape 8 : Traces d’exécution
- [ ] Générer un **fichier `.txt`** par test, contenant toutes les étapes (affichages, calculs…)
- [ ] Conserver ces fichiers dans un dossier `traces/`

### 💄 Étape BONUS : Amélioration interface
- [ ] Ajouter un menu d’accueil plus clair (interface graphique, tracé de graphes etc)
- [ ] Faire des animation visuel pendant l'execution des algo pour mieux comprendre leurs fonctionnements
- [ ] Faire un créateur de graphe qui converti un graphe visuel en graphe txt
