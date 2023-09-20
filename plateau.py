import numpy as np 
from player import *
from src import *
import random

class Plateau : 

  # Initiate class variables
  def __init__(self, pl_width, pl_length, player1, player2) : 
    self.player1 = player1
    self.player2 = player2
    self.plateau = np.zeros((pl_width,pl_length))
    self.width = pl_width
    self.length = pl_length

  # Affichage du Plateau
  def show(self) : 
    print(self.plateau)


  # Function for class manipulation 
  def reset(self) : 
    self.plateau = np.zeros((self.width, self.length))
    return False

  def has_won(self) : 

    # Add Coordinates present on the Plateau for both players
    for i in range(self.width) : 
      for j in range(self.length) : 
        if self.plateau[i][j]==1 : 
          self.player1.addCoordinate((i,j)) 
        elif self.plateau[i][j]==-1 : 
          self.player2.addCoordinate((i,j)) 
    
    # Possible move dictionnary for Player 1
    Player1 = dict()
    for i in self.player1.coordinate : 
      if i not in Player1 :
        Player1[i] = find_winning_quadruplets(self.width,self.length,i[0],i[1])

    # Possible move dictionnary for Player 2
    Player2 = dict()
    for i in self.player2.coordinate : 
      if i not in Player2 :
        Player2[i] = find_winning_quadruplets(self.width,self.length,i[0],i[1])

    # Generate empty list from dictionnary 
    for i in self.player1.coordinate : 
      for (k,_) in Player1.items() : 
        for j in Player1[k] : 
            if i in j:
                j.remove(i)
    
    for i in self.player2.coordinate : 
      for (k,_) in Player2.items() : 
        for j in Player2[k] : 
            if i in j : 
                j.remove(i)

    # Determine winner from empty list
    p1_winner = 0
    p2_winner = 0

    for (k,_) in Player1.items() : 
      for m in Player1[k]:
      	if len(m)==0:
		      p1_winner = 1
		      break

    for (k,_) in Player2.items() : 
    	for m in Player2[k]:
		    if len(m)==0 : 
		      p2_winner = -1
		      break

    # If both win 
    if p1_winner!=0 and p2_winner!=0 : 
      return 2
    else :
      if p1_winner!=0 : 
        return p1_winner
      else : return p2_winner
    
    # If no one win
    return 0

  def play(self,x,player) :
    i = self.width-1
    while i>=0 : 
      if self.plateau[i][x]==0 : 
        self.plateau[i][x] = player.etiquette
        break
      i-=1

    if player.etiquette == 1 : return -1
    else : return 1

  def is_finished(self) : 
    return self.has_won()
  
  def run(self, player1, player2) :
    if (self.width<self.length) : 
      x = random.randint(0,self.length)
      turn = self.play(x,player2)
      print(turn)
      while not self.is_finished():
        x = random.randint(0,self.length)
        if turn==1 : 
          turn = self.play(x,player1)
        elif turn==-1 : 
          turn = self.play(x,player2)
    
    elif (self.width==self.length) : 
      x = random.randint(0,self.width-1)
      turn = self.play(x,player2)
      print(turn)
      while not self.is_finished():
        x = random.randint(0,self.width-1)
        if turn==1 : 
          turn = self.play(x,player1)
        elif turn==-1 : 
          turn = self.play(x,player2)
    
    else : 
      x = random.randint(0,self.length-1)
      turn = self.play(x,player2)
      print(turn)
      while not self.is_finished():
        x = random.randint(0,self.length-1)
        if turn==1 : 
          turn = self.play(x,player1)
        elif turn==-1 : 
          turn = self.play(x,player2)

    print("Winner is : ", self.has_won())
      
