from plateau import *

class MonteCarlo(Plateau) : 
  """Algorithme de Monte Carlo"""
  
  def __init__(self, P) : 
    super(MonteCarlo, self).__init__(P.width, P.length, P.player1, P.player2, P.turn)
    assert self.turn!=0, "Error : Movement decision parameter must be different than 0"

  def MovesCounter(self, x, player) : 
    """Calculer le nombre de victoire au cours de N fois joue basant sur l'algorithme de strategie de Monte Carlo"""
    N = 10000
    i = 0
    virtual = 1 if player==1 else -1
    count = 0
    plt = self.duplicata()

    while i<N : 
      plt = self.duplicata()

      if player==1 : plt.run(player,virtual)
      elif player==-1 : plt.run(virtual,player)

      if plt.has_won()==player :
        count+=1
        
      i+=1 
      #print(count)
    #plt.show()
    #print("ok")
    return count/N


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
    return (np.argmax(L),L)
