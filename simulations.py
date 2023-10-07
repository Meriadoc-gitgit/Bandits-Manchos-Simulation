# Import necessary classes
from player import *
from plateau import *
from monte_carlo import *
from bandits_manchots import *

# Import necessary libraries
import numpy as np
import pandas as pd 
import random as rd
import matplotlib.pyplot as plt


horizon = 1000

choix, recompenses = np.zeros(horizon), np.zeros(horizon)

# Plateau
P = Plateau(8,8,1,-1)
gr = BDMC(P,1)


rec =[0] * P.length


if P.turn!=gr.player : 
  tmp = [P.MovesCounter(i, P.turn) for i in range(P.length)]
  move = np.argmax(tmp)
  P.play(move,P.turn)

estimations = [P.MovesCounter(i, gr.player) for i in range(P.length)]

for t in range(1000): 
  A_t = gr.baseline(estimations, [horizon*estimations[i] for i in range(len(estimations))])
  r_k_t = gr.binary_gain(estimations, A_t)
  rec[A_t]+=r_k_t
  choix[t] = A_t
  recompenses[t] = r_k_t

print("recompenses",recompenses)
print("choix",choix)

kstar = 1

selection_kstar = 1.0 * (choix==kstar)
print("selection_kstar", selection_kstar)

selection_mean = np.cumsum(selection_kstar) / np.cumsum(np.ones_like(choix))

print("selection_mean", selection_mean)

plt.plot(selection_mean)

plt.show()