# Projet 1 : Exploration/Exploitation et Puissance 4
# Introduction 

L'***exploration*** et ***exploitation*** est un problème fondamental que l'on retrouve dans plusieurs domaines de l'intelligence artificielle, en particulier en Machine Learning. 
>Parmi un certain nombre de choix possibles, vaut-il mieux ***exploiter*** la connaissance acquise et choisir l'action estimée la plus rentable **ou** vaut-il mieux continuer à ***explorer*** d'autres actions afin d'acquérir plus d'informations ? 

- L'exploration consiste à faire la meilleure décision à partir de toute l'information collectée
- L'exploitation consiste à obtenir plus d'information

Souvent au début d'un processus, il est préférable de faire des sacrifices et de ne pas choisir l'option à priori la plus rentable afin d'améliorer le gain à long terme. 

La question reste de savoir quand arrêter d'explorer, *ie. quand estime-t-on avoir recueilli assez d'informations et que l'exploration n'apportera pas de connaissances supplémentaires*.

**Objectif** : *Étudier différents algorithmes* du dilemme d'*exploration* vs *exploitation* pour des IAs de jeu.

Le jeu étudié sera dans un premier temps le **puissance de 4** qui a l'***avantage d'avoir une combinatoire simple*** *(et donc à porter d'une implémentation naive sans grande puissance computationelle)*.
- [Pt 1](desc/proj1.md) : Implémentation et Analyse combinatoire du jeu, théorique et pratique
	- *combinatoire : tổ hợp (vnm)*
- Pt 2 : Implémentation d'un algorithme de Monte-Carlo pour la résolution du jeu
- Pt 3 : Étude des algorithmes classiques d'exploration vs exploitation dans un cadre simple
- Pt 4 : Étude des algorithmes avancés pour les jeux combinatoires