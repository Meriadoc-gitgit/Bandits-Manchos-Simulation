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

class Graphic :

  def __init__(self) : 
    """Initialiser la classe Graphic, rien a faire ici"""
    pass




  # ================================================
  # DATA SIMULATION
  # ================================================
  @staticmethod
  def simulation(P, player, alg, horizon, etat=0, kstar=0, eps=0.4, alpha=2) : 
    # ================================================
    # PRELIMINARY
    """
    P : Plateau de jeu
    player : etiquette du joueur qui gere le tour actuel/qui va gerer le prochain tour
    alg : algorithme choisi pour l'exploitation
    horizon : nombre d'essai necessaire pour l'exploitation
    kstar : levier choisi/colonne choisi par le joueur
    eps : nombre epsilon en parametre pour l'algo de greedy et e-greedy
    alpha : nombre alpha necessaire pour l'algo d'UCB
    """

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
        A_t = gr.epsilon_greedy(estimations, [horizon*estimations[i] for i in range(len(estimations))], eps=eps)
        #print(A_t)
        r_k_t = gr.binary_gain(estimations, A_t)
        rec[A_t]+=r_k_t
        choix[t] = A_t
        recompenses[t] = r_k_t

    # If UCB is the chosen algorithmn
    elif alg=="UCB" : 
      for t in range(horizon) : 
        A_t = gr.UCB(estimations, [horizon*estimations[i] for i in range(len(estimations))], alpha=alpha)
        r_k_t = gr.binary_gain(estimations, A_t)
        rec[A_t]+=r_k_t
        choix[t] = A_t
        recompenses[t] = r_k_t
    
    if alg=="UCB" : 
      pd.DataFrame(
        {
          "recompenses" : recompenses, 
          "choix" : choix
        }
      ).to_csv("recom-choice-{}-{}.csv".format(alg,alpha), index=False)
    else : 
      pd.DataFrame(
        {
          "recompenses" : recompenses, 
          "choix" : choix
        }
      ).to_csv("recom-choice-{}.csv".format(alg), index=False)


  # ================================================
  # SELECTION RATE
  # ================================================
  @staticmethod
  def affiche_selection(choix, alg, horizon, color="red", kstar=0, eps=0.4, alpha=2) : 
    selection_kstar = 1.0 * (choix==kstar)
    selection_mean = np.cumsum(selection_kstar) / np.cumsum(np.ones_like(choix))
    plt.plot(selection_mean, label=alg,color=color)
    plt.xlabel("Temps discret $t = 1...T={}".format(horizon))
    plt.ylabel("Taux de sélection")
    plt.title("Sélection du bras #{} pour l'algorithme {}".format(kstar, alg))
    plt.legend()

  # ================================================
  # RECOMPENSES RATE
  # ================================================
  def affiche_recompenses(recompense, alg, horizon, color="red", kstar=0, eps=0.4, alpha=2) : 
    recompense_accumulee = np.cumsum(recompense)
    plt.plot(recompense_accumulee, label=alg, color=color)
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompense)))
    plt.ylabel("Récompenses accumulées")
    plt.title("Récompenses accumulées pour différents algorithmes")
    
  # ================================================
  # MEAN RECOMPENSES RATE
  # ================================================
  def affiche_recompenses_moyennes(recompense, alg, horizon, color="red", kstar=0, eps=0.4, alpha=2) : 
    recompense_moyenne = np.cumsum(recompense) / np.cumsum(np.ones_like(recompense))
    plt.plot(recompense_moyenne, label=alg, color=color)
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompense)))
    plt.ylabel(r"Récompenses moyennes $\in [0, 1]$")
    plt.title("Récompenses moyennes pour différents algorithmes")

  # ================================================
  # REGRET RATE
  # ================================================
  def affiche_regret(P, player, recompense, alg, horizon, color="red", kstar=0, eps=0.4, alpha=2) : 
    #Value for color required
    mc = MonteCarlo(P)
    mustar = [mc.MovesCounter(i, player) for i in range(P.length)]
    recompense_accumulee = np.cumsum(recompense)
    regret = np.max(mustar) * np.cumsum(np.ones_like(recompense)) - recompense_accumulee

    plt.plot(regret, label=alg, color=color)
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompense)))
    plt.ylabel("Regret")
    plt.title("Regret accumulé pour différents algorithmes")
