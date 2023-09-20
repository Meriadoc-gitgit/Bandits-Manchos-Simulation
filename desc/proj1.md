# Combinatoire du [Puissance 4](https://fr.wikipedia.org/wiki/Puissance_4)
>**Objectif** : Implémentation du jeu + Étude combinatoire du jeu
# Description
- C'est un jeu à 2 joueurs qui se joue sur un plateau de $7\times6$
- Chaque joueur dispose de 21 jetons d'une couleur donnée *(généralement rouge pour l'un, bleu pour l'autre)*
- **Objectif** : Aligner 4 jetons de sa couleur sur le plateau *(verticalement, horizontalement, diagonal)*
- Tour à tour, chaque joueur place un pion sur une des $7$ colonnes et le pion tombe jusqu'à la première position non occupée de la colonne
- Le jeu s'**arrête** :
	- dès que 4 jetons de la même couleur sont alignées 
	- ou si toutes les cases sont occupées


# Conseils pour l'implémentation 
- codez les fonctions de manière générique de manière à ce qu'elles puissent traiter n'importe quelle taille de plateau
	- possible de définir des variables globales au début de votre code pour spécifier la taille de plateau étudié
- utilisez `numpy` pour coder des tableaux et les opérations mathématiques
- utilisez `matplotlib.pyplot` pour des affichages graphiques
- codez des classes : 
	- pour le Plateau
	- pour les Joueurs
- utilisez un tableau pour représenter le tableau, possible de coder
	- $0$ une case vide
	- $1$ le premier joueur
	- $-1$ le deuxième

1. Implémenter une fonction qui calcule la liste de toutes les quadruplets de cases qui doivent être de la même couleur pour gagner : $\{((0,0),(0,1),(0,2),(0,3)),((0,1),(0,2),(0.3),(0.4))...\}$
	- **Attention** : N'oubliez pas les diagonales !
	- **Fonction** : `find_winning_quadruplets(width, length, coord1, coord2)`
2. Implémenter le moteur du jeu *(sous forme de classe de préférence)*. Des indications vous sont données à la fin de l'énoncé pour l'implémentation. Il doit comporter les éléments suivants : 
- un tableau qui représente le plateau du jeu
- Les fonctions : 
	- `reset()` : réinitialiser le jeu
	- `has_won()` : tester la victoire d'un des deux joueurs
		- en parcourant la liste des quadruplets
		- et en testant s'ils sont de la même couleur
	- `play(x,joueur)` : placer un jeton dans la colonne `x` pour le joueur spécifié
	- `is_finished()` : tester si c'est la fin du jeu *(plateau plein/victoire d'un joueur)*
	- `run(joueur1.joueur2)` : jouer une partie entre le joueur 1 et le joueur 2
		- jouent à tour de rôle tant que la partie n'est pas finie
		- renvoie 1 ou -2 selon la victoire du joueur 1 ou 2, et 0 en cas de nul
		- Supposons que chaque joueur est muni d'une fonction `play(plateau,joueur)` qui renvoie le coup à joueur pour ce joueur en lui précisant s'il est joueur 1 ou 2
>**Note** : Utilisez ce codage des joueurs dans tous le projet : 1 pour le joueur 1 et -1 pour le joueur 2