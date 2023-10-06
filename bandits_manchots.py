from plateau import *
from monte_carlo import *
import random

class BDMC(Plateau) : 
  """Algorithme de UCB"""

  def __init__(self, P, player) : 
    super(BDMC, self).__init__(P.width, P.length, P.player1, P.player2, P.turn)
    self.player = player
    assert self.turn!=0, "Error : Movement decision parameter must be different than 0"



  #=======================================
  # BANDITS-MANCHOTS
  """
  2 arguments generaux :
  - la liste des recompenses moyennes estimees pour chaque levier (liste des mu^i)
  - le nombre de fois ou chaque levier a ete joue (la liste des N(i))
  """
  #=======================================

  def binary_gain(self, leviers, actions) : # rend le gain binaire corespondant au coup joue
    # random.random() rend un reel entre 0 et 1
    return 1 if random.random()<=leviers[actions] else 0
  
  
  
  def baseline(self, estimations, nbChosenLevier) : 
    """Choisir a_t uniformement parmi toutes les actions possibles"""
    return random.randint(0, len(estimations)-1)




  def greedy(self, estimations, nbChosenLevier) :
    """
    Implémente un algorithme Greedy pour maximiser les récompenses totales en utilisant des estimations moyennes.

    :return: Le levier dont le rendement estimé est maximum après tous les tirages.
    :rtype: int
    """
    nombre_de_tirages = 10000
    nombre_de_fois_joues = [0] * len(estimations)
    recompenses_accumulees = [0] * len(estimations)

    #=======================================
    # EXPLOITATION
    #=======================================
    for _ in range(nombre_de_tirages):
      # Choisir un levier au hasard
      levier_selectionne = self.baseline(estimations,nbChosenLevier)
      #print(levier_selectionne)

      #print(levier_selectionne)
          
      # Mettre à jour le nombre de fois joué pour ce levier
      nombre_de_fois_joues[levier_selectionne] += 1
          
      # Simuler le tirage du levier et mettre à jour les récompenses accumulées
      recompense = self.binary_gain(estimations, levier_selectionne)
      recompenses_accumulees[levier_selectionne] += recompense

    # Trouver le levier avec le rendement estimé maximum
    levier_max = np.argmax([recompenses_accumulees[i]/nombre_de_fois_joues[i] for i in range(len(recompenses_accumulees))])

    #print(nombre_de_fois_joues)
    #print(recompenses_accumulees)
    #print([recompenses_accumulees[i]/nombre_de_fois_joues[i] for i in range(len(recompenses_accumulees))])
    
    return levier_max


  def epsilon_greedy(self, estimations, nbChosenLevier, eps=0.4) : 

    # Initialiser les variables necessaires pour l'implementation
    N = 500
    L = dict()

    #=======================================
    # EXPLORATION
    #=======================================
    for i in range(N) : 
      r = np.random.rand()
      if r>=eps : 
        greedy = self.greedy(estimations, nbChosenLevier)
        if greedy not in L : L[greedy] = greedy*r
        else : L[greedy]+=greedy*r
      
      else : 
        baseline = self.baseline(estimations, nbChosenLevier)
        if baseline not in L : L[baseline] = baseline*r
        else : L[baseline]+=baseline*r

    # MISE A JOUR DE L
    tmp = [v/N for (_,v) in L.items()]
    print(tmp)
    return np.argmax(tmp)

    
  def UCB(self, estimations, nbChosenLevier, alpha=2) : 
      
    # Initialiser les variables necessaires pour l'implementation
    N = 10000
    L = [0] * N
    chosen = [0] * N
    D = dict()

    #=======================================
    # EXPLORATION
    #=======================================
    for i in range(N) : 
      baseline = self.baseline(estimations, nbChosenLevier)
      if nbChosenLevier[baseline]==0 or i in [0,1] : 
        L[i] = 0
      else : L[i] = estimations[baseline] + np.sqrt((alpha*np.log2(i))/nbChosenLevier[baseline])
      chosen[i] = baseline

      for i in range(N) : 
        if chosen[i] not in D : 
          D[chosen[i]] = L[i]
        else : D[chosen[i]]+=L[i]

    tmp = [v for (_,v) in D.items()]
    #print(tmp)

    return np.argmax(tmp)
