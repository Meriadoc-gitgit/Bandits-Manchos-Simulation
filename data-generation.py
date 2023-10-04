# Side code to generate graph and database to analyse the distribution of the number of turns before finding a winner

# Import necessary libraries
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from player import *
from src import *
from plateau import *

# Distribution du nombre de coups avant une victoire lorsque les deux joueurs jouent aléatoirement en différenciant selon que ce soit le premier ou le deuxième joueur qui gagne

Joueur1 = Player(1)
Joueur2 = Player(-1)

P = Plateau(20,20,Joueur1, Joueur2)
list_move = []

for i in range(1000) : 
  print(i)
  P.run(Joueur1, Joueur2)
  if P.has_won()==1 : 
    list_move.append((P.player1.total_move,1))
  else : 
    list_move.append((P.player2.total_move,-1))
  
  P.reset()




# Initialiser les listes et dictionnaires nécessaires pour l'étude de la distribution des nombres de coups avant la victoire

# LISTs
list_move_unique = np.unique([i for (i,_) in list_move])
list_move_unique.sort()

# DICTIONNAIREs
freq_move = dict()
freq_move_1 = dict()
freq_move_2 = dict()

# Construire le dictionnaire de base
for i in range(np.max(list_move_unique)+1) : 
    if i not in freq_move : 
        freq_move[i] = 0
        freq_move_1[i] = 0
        freq_move_2[i] = 0

# Incrementer la frequence des nombres de coups apparus
for (i,v) in list_move : 
    freq_move[i] +=1
    # Incrémenter la fréquence des 2 dictionnaires de fréquences de 2 joueurs
    if v==1 : 
        freq_move_1[i] += 1
    else : freq_move_2[i] +=1


# Initialiser 2 listes de frequence et la valeur associe a chaque frequence
value = [i for (i,_) in freq_move.items()]
freq = [i for (_,i) in freq_move.items()]
# pour les 2 joueurs 
freq_1 = [i for (_,i) in freq_move_1.items()]
freq_2 = [i for (_,i) in freq_move_2.items()]


# Generer une base de donnees afin d'eviter le stackoverflow lors d'execution
pd.DataFrame(
    {"value" : value, 
     "freq_move" : freq, 
     "freq_1" : freq_1, "freq_2" : freq_2}
).to_csv("freq_moves_database.csv",
         index=False)

