# Import necessary classes
from plateau import *
from monte_carlo import *
from bandits_manchots import * 
from graphic import *


# Dependancies
import random


# -*- coding: utf-8 -*-

class Node :
  """
  Classe définissant un State (ou Node) caractérisée par :
    - un identifiant
    - un label utilisé pour les constructions
        ou il faut memoriser d'ou vient l'etat construit

    - un Node pere (par default None)
    - un ensemble de Node fils (par default set())
    - une valeur t indiquant le nombre de victoire obtenu aubout de n simulations pour le levier i (= valeur accumulee des v_i)
    - une valeur n indiquant le nombre de simulations necessaires avant une victoire de tous les leviers 
    - une valeur v_i indiquant le nombre de victoire d'un branche du levier
  """

  def __init__ (self, id, label=None, pere=None, fils=set()) :
    """ int x bool x bool x str -> State
      constructeur d'état
    """
    self.id = id
    if label==None : 
      self.label = "S"+str(self.id)
    else : self.label = label
    self.pere = pere 
    self.fils = fils
    self.t = 0; self.n = 0; self.v = 0
    self.visited = False

  def addNode(self, new_node) : 
    if not new_node.visited : 
      self.fils.add(new_node)

  def show(self) : 
    L = "id: "+str(self.id)+" | t: "+str(self.t)+" | n: "+str(self.n)+" | v: "+str(self.v)
    
    for i in self.fils :
      if i.visited == False :
        i.visited = True
        i.show() 
      if i.fils==set() : break
    print(L)

  def removeChildNode(self, id) : 
    s = set()
    j = 0
    nb_elem = len(self.fils)
    for i in self.fils : 
      if i.id!=id : 
        s.add(i)
        j +=1
        if j==nb_elem-1 : 
          break
    self.fils = s






class MCTS : 

  def __init__(self, P, player, alpha=2) : 
    self.P = P 
    self.player = player
    self.alpha=alpha


  def liste_leviers(self,P) : 
    # Generer une liste de levier a jouer

    # Plateau associe a ce MCTS
    player = self.player
    alpha = self.alpha
    horizon = 10 # Constant declaree au debut du projet

    gr = BDMC(P, player)

    if P.turn!=gr.player : 
      move = np.random.randint(1,P.length-1)
      P.play(move,P.turn)

    estimations = [P.MovesCounter(i, gr.player) for i in range(P.length)]
    # Generer un nombre random de levier a choisir entre [1, P.length]
    nb_levier = np.random.randint(1, P.length)
    #print(nb_levier)

    # Generer un nombre nb_levier de fois l'algo UCB
    liste_levier = np.unique([gr.UCB(estimations=estimations, nbChosenLevier=[horizon*estimations[i] for i in range(len(estimations))]) for i in range(nb_levier)])
    #print(liste_levier)

    return liste_levier




  def generate_childNode(self, leviers, current_node) : 
    # Creer et ajouter les nodes de la liste en entree
    current_node.fils = set()
    for i in range(len(leviers)) : 
      current_node.addNode(Node(id=leviers[i], pere=current_node))
  

  def simulation(self, root_node) : 
    
    # Plateau associe a ce MCTS
    P = self.P
    player = self.player

    # Generer une liste de leviers
    leviers = self.liste_leviers(P)
    #print("ok")

    P.show()

    # Generate root_node child
    self.generate_childNode(leviers, root_node) 



    if root_node.pere is None : 
      
      print("len root_node: ", len(root_node.fils), "id: ", root_node.id)
    else : print("len root_node: ", len(root_node.fils), "id: ", root_node.id, "pere: ", root_node.pere.id)
    print("child id: ",[i.id for i in root_node.fils])
    child = root_node.fils
      
    for i in child :

      if not P.is_finished() : 
        if not i.visited : 
          if P.turn!=player : 
            move = np.random.randint(1,P.length-1)
            P.play(move,P.turn)
          P.play(i.id, player)
          i.visited = True 
          self.P = P
          node = self.simulation(i)
          root_node.t+=node.t
          root_node.n+=node.n
          
      else : 
        if P.has_won()==player :
          print("END") 
          root_node.t = 1
          root_node.n = 1
          root_node.removeChildNode(i.id)
          self.P.reset()
        else : 
          print("END") 
          root_node.t = 0
          root_node.n = 1
          root_node.removeChildNode(i.id)
          self.P.reset()
      
      if len(root_node.fils) == 0 and root_node.pere is None : break

    return root_node

  def winning_rate_calculation(self, root_node) : 
    if root_node.pere is None : 
      child = root_node.fils 
      len_child = len(child)
      list_childT = []
      
      for i in child : 

        if len_child==0 : 
          
          T = [v for (v,_) in list_childT]
          ID = [v for (_,v) in list_childT]
          maximum = np.argmax(T)

          return ID[maximum]

        list_childT.append((i.t,i.id))
        len_child-=1

      
    