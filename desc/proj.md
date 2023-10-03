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

# Bandits-manchots
>Afin de formaliser le probleme de l'exploitation/exploration, on prend souvent l'exemple des bandits manchots *(machine a sous), le jeu de hasard qu'on retrouve dans tout casinon qui se respecte :*
>
>- Pour une mise, on a le droit d'actionner un levier qui fait tourner des rouleaux
>- en fonction de la combinaison obtenue sur les rouleaux, une recompense est attribue au joueur

Supposons une machine a sous a $N$ leviers denotes par l'ensemble $\{1,2,...N\}$. 

Chacun de ses leviers est une action possible parmi lesquelles le joueur doit choisir a chaque pas de temps
- l'action choisir a l'instant $t$ sera appelee $a_t$ *(un entier entre $1$ et $N$)*

Supposerons dans la suite que la recompense assochiee a chaque levier $i$ suit une distribution de Bernouilli de parametre $\mu_i$ 
- avec une proba $\mu_i$ le joueur obtient une recompense de $1$
- avec une proba $1-\mu_i$ le joueur obtient une recompense de $0$ 

Cette recompense obtenue au temps $t$ lorsque le joueur joue sera notee $r_t$. 

En notant $a_t$ l'action jouee au temps $t$, $r_t$ est donc une variable aleatoire qui suit une loi de Bernouilli de parametre $\mu^{a_t}$. 

Supposons de plus que le rendement de chaque levier est stationnaire dans le temps, *ie. les $\mu_i$ sont constants tout au long de la partie*. 

Pour le joueur : 
- Le gain au bout de $T$ parties = somme des recompenses qu'il a obtenu pendant les $T$ premiere parties

$$G_T = \sum^T_{t=0}r_t$$

n.b. la recompense etant aleatoire, le gain $G_T$ est une variable aleatoire, tout comme $r_t$. 

Pour maximiser ce gain : 
- il faut que le joueur identifie : 
	- le levier au rendement le plus eleve : $i^*=argmax_{i\in(1,...N)}\mu^i$
	- le rendement associe : $\mu^*=\mu^{i^*}=max_{i\in(1,...N)}\mu^i$

- Si le joueur joue un autre levier que $i^*$, il aura en moyenne un gain total inferieur au gain maximal qu'il peut esperer. 
	- Ce gain maximal a un temps $T$ s'ecrit $G^*_T=\sum^T_{i=1}r^*_t$ *($r^*_t$ la recompense aleatoire tiree de la distribution de Bernoulli de parametre $\mu^*$)*
- On appelle regret au temps $T$ la difference entre le gain maximal espere et le gain du joueur : $L_T = G^*=\sum^T_{t=1}r_t=\sum^T_{i=1}(r^*_t-r_t)$
- **Objectif : MINIMISER LE REGRET**

Note : 
- $N_T(a)$ le nombre de fois ou l'action *(le levier)* a ete choisi jusqu'au temps $T$

(to be continue)