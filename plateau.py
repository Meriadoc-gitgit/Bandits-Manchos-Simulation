import numpy as np 
from player import *
from src import *
import random

class Plateau : 

  # Initiate class variables
  def __init__(self, pl_width, pl_length, player1, player2) : 
    self.player1 = player1
    self.player2 = player2
    self.board = np.zeros((pl_width,pl_length))
    self.width = pl_width
    self.length = pl_length


  #===============================
  # Affichage du Plateau
  def show(self) : 
    print("=============================")
    print("Current state of the game")
    print("=============================")
    print(self.board)


  # Function for class manipulation 
  def reset(self) : 
    self.board = np.zeros((self.width, self.length))
    return


  def has_won(self) : 
    # Predict possible moves on the board
    predict = predict_winning_quadruplets(self.board)

    # Check each predicted possible move value on the board
    for i in predict : 
      move = self.board[(i[0][0],i[1][0],i[2][0],i[3][0]),
                  (i[0][1],i[1][1],i[2][1],i[3][1])]
      if (sum(move)==4) : return 1
      elif (sum(move)==-4) : return -1

    return 0





  def play(self,x,player) :
    i = self.width-1
    while i>=0 : 
      if self.board[i][x]==0 : 
        self.board[i][x] = player.etiquette
        break
      i-=1

    if player.etiquette == 1 : return -1
    else : return 1

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

    print("Puissance 4 winner is : ", self.has_won())
    self.show()
      
