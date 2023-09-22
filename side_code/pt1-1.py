# Side code to generate graph and database to analyse the distribution of the nombre of turns before finding a winner

# Import necessary libraries
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Distribution du nombre de coups avant une victoire lorsque les deux joueurs jouent aléatoirement 
# en différenciant selon que ce soit le premier ou le deuxième joueur qui gagne
P = Plateau(15,15,Joueur1, Joueur2)
list_move = []

for i in range(1000) : 
    total_move = 0
    P.run(Joueur1, Joueur2)
    for j in range(P.length) :
        for k in range(P.width) : 
            if P.board[j][k]==P.has_won() : 
                total_move+=1
    list_move.append(total_move)
    P.reset()

list_move_unique = np.unique(list_move)
list_move_unique.sort()
freq_move = dict()

# Construire le dictionnaire de base
for i in range(np.max(list_move_unique)+1) : 
    if i not in freq_move : 
        freq_move[i] = 0
        
# Incrementer la frequence des nombres de coups apparus
for i in list_move : 
    freq_move[i] +=1

# Initialiser 2 listes de frequence et la valeur associe a chaque frequence
freq = [i for (i,_) in freq_move.items()]
value = [i for (_,i) in freq_move.items()]

# Generer une base de donnees afin d'eviter le stackoverflow lors d'execution
pd.DataFrame({"freq_move" : freq, "value" : value}).to_csv("freq_moves_database.csv",index=False)


# Graphe de distribution des nombres de déplacements
plt_1 = plt.figure(figsize=(6, 3))
plt.bar(df["freq_move"],df["value"],color="blue")
plt.grid()
#plt.scatter(range(150),list_move,s=.5,c="red")

plt.xlabel('Nombre de coups')
plt.ylabel("Frequence d'apparition associée")
plt.title("Distribution du nombre de coups avant une victoire")

# Sauvegarder le graph sous forme PNG
plt.savefig("poisson_dist_nb_coups.jpg")
