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

def affiche_regret(recompenses, noms, mustar=1): 
  plt.figure()
  for i, r in enumerate(recompenses):
    recompense_accumulee = np.cumsum(r)
    regret = mustar * np.cumsum(np.ones_like(r)) - recompense_accumulee 
    plt.plot(regret, label=noms[i])
  
  plt.legend()
  plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompenses[0]))) 
  plt.ylabel("Regret")
  plt.title("Regret accumulé pour différents algorithmes")
  plt.show()
