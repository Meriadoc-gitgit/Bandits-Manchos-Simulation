# Import necessary libraries
import numpy as np
import random

from player import *


#=======================================================

# PREDICTING THE BOARD'S POSSIBLE WINNING QUADRUPLETS
def predict_winning_quadruplets(board):
  rows = len(board)
  cols = len(board[0])
  quadruplets = []

  # Check horizontal quadruplets
  for row in range(rows):
    for col in range(cols - 3):
      quadruplets.append(((row, col), (row, col + 1), (row, col + 2), (row, col + 3)))

  # Check vertical quadruplets
  for row in range(rows - 3):
    for col in range(cols):
      quadruplets.append(((row, col), (row + 1, col), (row + 2, col), (row + 3, col)))

  # Check diagonal (top-left to bottom-right) quadruplets
  for row in range(rows - 3):
    for col in range(cols - 3):
      quadruplets.append(((row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)))

  # Check diagonal (bottom-left to top-right) quadruplets
  for row in range(3, rows):
    for col in range(cols - 3):
      quadruplets.append(((row, col), (row - 1, col + 1), (row - 2, col + 2), (row - 3, col + 3)))

  return quadruplets



#=======================================================

class Plateau : 
  # INITIALISATIONS
  def __init__(self, width, length, player1, player2, turn=1) : 
    self.width = width
    self.length = length
    self.player1 = Player(player1)
    self.player2 = Player(player2)

    self.board = np.zeros((width, length))
    self.turn = turn # default turn = 1


  # BASIC FUNCTIONS
  def show(self) : # Visualiza the current session, including the information about the state of the game and the winner of the game has marked an end
    print("====================================")
    print("VISUALIZATION OF THE CURRENT SESSION OF PUISSANCE 4")
    if not self.is_finished() : 
      print("The game is not finished !")
    else : 
      print("The game has marked an end !")
      print("Winner :", self.has_won())
    

    print("====================================")
    print(self.board)
    print("====================================")

  def duplicata(self) : # Duplicate the current board
    plt = Plateau(self.width, self.length, self.player1.etiquette, self.player2.etiquette)
    for i in range(plt.length-1) : 
      for j in range(self.width-1) : 
        plt.board[i][j] = self.board[i][j]
    return plt
  

  # BOARD MANIPULATION FUNCTION
  def reset(self) : 
    self.board = np.zeros((self.width, self.length))
    #print("The game is successfully reset")
    self.player1.reset()
    self.player2.reset()

  # Verify if there is a winner on the current session 
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

  def is_finished(self) : 
    return self.has_won() != 0

  def play(self,x,player) : 
    # Verify if the player has the right to process his turn
    if self.turn != player : 
      print("Warning : The other player need to take his turn !")
      return
    
    # Place the button on the bottommost of the column
    i = self.width-1
    while i>=0 : 
      if not self.board[i][x] : 
        self.board[i][x] = player
        if player==1 : 
          self.player1.addCoordinates((i,x))
          self.player1.total_move+=1
        else : 
          self.player2.addCoordinates((i,x))
          self.player2.total_move+=1
        break
      i-=1

    # Update the current turn 
    if self.turn == 1 : 
      self.turn = -1
    else : 
      self.turn = 1
 
  def run(self, player1, player2) : 
    count = 0
    # Generate auto-play game
    while not self.is_finished() : 
      x = random.randint(0,self.length-1)
      self.play(x, self.turn)



  #=======================================================

  # COMPTER LE TAUX DE REUSITTE DE CHAQUE CHOIX

  def MovesCounter(self, x, player) : 
    """Calculer le nombre de victoire au cours de N fois joue basant sur l'algorithme de strategie de Monte Carlo"""
    N = 100
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
      #print(i)
    #plt.show()
    #print("ok")
    return count/N