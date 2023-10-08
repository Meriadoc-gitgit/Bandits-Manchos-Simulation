from plateau import *

class MonteCarlo(Plateau) : 
  """Algorithme de Monte Carlo"""
  
  def __init__(self, P) : 
    super(MonteCarlo, self).__init__(P.width, P.length, P.player1, P.player2, P.turn)
    assert self.turn!=0, "Error : Movement decision parameter must be different than 0"


  def MonteCarloStrategy(self,etat,player) : 
    """
    Hypothese : Supposons que les joueurs n'estiment les deplacements que during leur tour.
    Objectif : Calculer le tour de l'autre joueur.
    """

    if etat==0 : 
      tmp = [self.MovesCounter(i, -1) for i in range(self.length)] 
      move = np.argmax(tmp)
      self.play(move,self.turn)
      
    L = [self.MovesCounter(i, player) for i in range(self.length)]
    #print(L)
    return np.argmax(L)
