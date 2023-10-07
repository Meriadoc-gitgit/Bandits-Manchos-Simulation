# Import necessary classes
from plateau import *
from player import *
from monte_carlo import *
from bandits_manchots import *

# Import necessary libraries
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns
sns.set(context="notebook", style="whitegrid", palette="hls", font="sans-serif", font_scale=1.4) 
from tqdm import tqdm_notebook as tqdm

class Graphic :

  def __init__(self) : 
    pass

  # ================================================
  # SELECTION RATE
  # ================================================
  @staticmethod
  def selections_simulation(P, player, alg, horizon, kstar=0) : 

    # Initiate Bandits-Manchots 
    gr = BDMC(P, player)

    if P.turn!=gr.player : 
      tmp = [P.MovesCounter(i, P.turn) for i in range(P.length)]
      move = np.argmax(tmp)
      P.play(move,P.turn)

    estimations = [P.MovesCounter(i, gr.player) for i in range(P.length)]

    # Initiate necessary list
    rec = [0] * gr.length
    choix, recompenses = np.zeros(horizon), np.zeros(horizon)

    # Loop

    # If BASELINE is the chosen algorithmn
    if alg=="baseline" : 
      for t in range(horizon) : 
          A_t = gr.baseline(estimations, [horizon*estimations[i] for i in range(len(estimations))])
          r_k_t = gr.binary_gain(estimations, A_t)
          rec[A_t]+=r_k_t
          choix[t] = A_t
          recompenses[t] = r_k_t


    # If GREEDY is the chosen algorithmn
    elif alg=="greedy" : 
      for t in range(horizon) : 
          A_t = gr.greedy(estimations, [horizon*estimations[i] for i in range(len(estimations))])
          #print(A_t)
          r_k_t = gr.binary_gain(estimations, A_t)
          rec[A_t]+=r_k_t
          choix[t] = A_t
          recompenses[t] = r_k_t
      

    # If EPS-GREEDY is the chosen algorithmn
    elif alg=="eps-greedy" : 
      for t in range(horizon) : 
          A_t = gr.epsilon_greedy(estimations, [horizon*estimations[i] for i in range(len(estimations))])
          r_k_t = gr.binary_gain(estimations, A_t)
          rec[A_t]+=r_k_t
          choix[t] = A_t
          recompenses[t] = r_k_t

    # If UCB is the chosen algorithmn
    elif alg=="UCB" : 
      for t in range(horizon) : 
          A_t = gr.UCB(estimations, [horizon*estimations[i] for i in range(len(estimations))])
          r_k_t = gr.binary_gain(estimations, A_t)
          rec[A_t]+=r_k_t
          choix[t] = A_t
          recompenses[t] = r_k_t
      
    selection_kstar = 1.0 * (choix==kstar)
    selection_mean = np.cumsum(selection_kstar) / np.cumsum(np.ones_like(choix))
    return selection_mean

  