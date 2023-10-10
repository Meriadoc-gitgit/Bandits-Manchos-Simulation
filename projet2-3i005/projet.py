#####
# INFORMATION DE BINOMES
#####
# Hoang Thuy Duong VU | 21110221
# Halimatou DIALLO | 
#####




# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats

class projet : 

  def __init__(self) : 
    # Initialiser la classe projet
    pass

  # Question 1.1 : calcul de probabilite a priori
  @staticmethod
  def getPrior(df) : 
    return {
      "estimation" : len([i for i in df["target"] if i==1])/len(df),
      "min5pourcent" : stats.t.interval(0.95, df=len(df)-1, loc=np.mean(df["target"]), scale=np.std(df["target"], ddof=1) / np.sqrt(len(df)-1))[0],
      "max5pourcent" : stats.t.interval(0.95, df=len(df)-1, loc=np.mean(df["target"]), scale=np.std(df["target"], ddof=1) / np.sqrt(len(df)-1))[1]
    }

