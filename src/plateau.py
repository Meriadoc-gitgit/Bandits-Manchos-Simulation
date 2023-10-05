import numpy as np 
import random
from player import *
from src import *

class Plateau : 

  # Initiate class variables
  def __init__(self, pl_width, pl_length, player1, player2) : 
    self.player1 = player1
    self.player2 = player2
    self.board = np.zeros((pl_width,pl_length))
    self.width = pl_width
    self.length = pl_length
    self.turn = 1


  #===============================
  # Affichage du Plateau
  def show(self) : 
    print("=============================")
    print("Current state of the game")
    print("=============================")
    print(self.board)

  #===============================
  # Créer un duplicata du Plateau
  def duplicata(self) : 
    plt = Plateau(self.width, self.length, self.player1, self.player2, self.turn)
    for i in range(plt.length-1) : 
      for j in range(self.width-1) : 
        plt.board[i][j] = self.board[i][j]
    return plt



  # Function for class manipulation 
  def reset(self) : 
    self.board = np.zeros((self.width, self.length))
    return


  def has_won(self) : 
    # Predict possible moves on the board
    predict = predict_winning_quadruplets(self.board)

    # Check each predicted possible move value on the board
    for i in predict : 
      # Gather the current value of each possible move
      move = self.board[
        (i[0][0],i[1][0],
        i[2][0],i[3][0]),
        (i[0][1],i[1][1]
        ,i[2][1],i[3][1])
        ]
      # If the sum(move)==4 than the first player wins, for -4 than the second
      if (sum(move)==4) : return 1
      elif (sum(move)==-4) : return -1

    return 0

  def play(self,x,player) :
    if self.turn != player.etiquette : 
      print("Warning : The other player need to take his turn !")
      return self.turn
    i = self.width-1
    while i>=0 : 
      if self.board[i][x]==0 : 
        self.board[i][x] = player.etiquette
        break
      i-=1

    if player.etiquette == 1 : self.turn = -1; return -1
    else : self.turn = -1; return 1

  def is_finished(self) : 
    return self.has_won()!=0
  
  def run(self, player1, player2) :
    # Generate a random variable of x 
    x = random.randint(0,self.length-1)

    # Start the game with player 1 as first move
    turn = self.play(x,player1)
    while not self.is_finished():
      x = random.randint(0,self.length-1)
      if turn==1 : 
        turn = self.play(x,player1)
      elif turn==-1 : 
        turn = self.play(x,player2)






  #===============================
  # Monte-Carlo strategy
  def mc_strategy(self, etat, joueur) : 
    
    N = self.width*self.length
    L = np.zeros(self.length)
    i = 0

    # Comparer l'état avec l'étiquette du joueur actuel en entrée
    if joueur.etiquette!=etat : 
      print("Error : Player mark must be the same as that of state")

    # Possible que le Plateau actuelle est deja fini !

    # Simuler 1 joueur virtuel
    if etat == 1 : joueur_virtuel = Player(-1)
    else : joueur_virtuel = Player(1)
    #print("etiquette joueur vitruel: ",joueur_virtuel.etiquette)

    while i<N : 
      
      # Simuler un autre Plateau virtuel
      plateau = self.duplicata()
      
      recompenses = 0 #moyenne des victoires par action 
      action = random.randint(0,self.length-1)
      #print("action: ",action)
      
      #while not self.is_finished() :
      plateau.play(action, joueur)
      plateau.run(joueur, joueur_virtuel)

      winner = plateau.has_won()
      #print("winner: ",winner)
      
      
      if winner==etat :  
        for j in range(plateau.length-1) : 
          for k in range(plateau.width-1) : 
            if plateau.board[j][k] == etat : 
              recompenses+=1
        
        if L[action] > recompenses : # Garder seulement les meilleurs nombres de tours 
          L[action] = recompenses
        elif L[action] == 0 :
          L[action] = recompenses

      if i == N-1 : 
        plateau.show()
      
      #plateau.reset()
      i+=1
    print("Array of number of turns before winning: ",L)
    print("winner : ", plateau.has_won())
    return (np.argmin(L), etat, 1) if plateau.has_won()==etat else (np.argmin(L), etat, 0)



  @staticmethod
  # Monte-Carlo play applying Monte-Carlo strategy 
  def mc_play(plt, player1, player2) : 
    plateau = plt.duplicata()
    plateau.reset()
    move = plateau.play(plateau.mc_strategy(player1.etiquette,player1)[0],player1)
    count = 0
    while not plateau.is_finished() : 
      if move == -1 : 
        move = plateau.play(plateau.mc_strategy(player2.etiquette,player2)[0],player2)
      else : 
        move = plateau.play(plateau.mc_strategy(player1.etiquette,player1)[0],player1)
        
      count+=1

    print("winner: ",plateau.has_won())
    print("Number of turns: ",count)
    plateau.show()
    return


  """
  2 arguments generaux :
  - la liste des recompenses moyennes estimees pour chaque levier (liste des mu^i)
  - le nombre de fois ou chaque levier a ete joue (la liste des N(i))
  """

  def baseline(self, recompenses, tours) : 
    return random.randint(0,self.length-1)

  def greedy(self, recompenses, tours) : 
    
    return