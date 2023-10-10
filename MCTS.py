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
    self.t = 0; self.n = 0
    self.visited = False

  def addNode(self, new_node) : 
    if not new_node.visited : 
      self.fils.add(new_node)

  def show(self) : 
    L = "id: "+str(self.id)+" | t: "+str(self.t)+" | n: "+str(self.n)
    
    for i in self.fils :
      if i.visited == False :
        i.visited = True
        i.show() 
      if i.fils==set() : break
    print(L)






class MCTS : 

  LIMIT = 30

  def __init__(self, P, player, alpha=2) : 
    self.P = P 
    self.player = player
    self.alpha=alpha
    self.ite = 0


  def liste_leviers(self,P, nb_fils_max=3) : 
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
    #print(nb_levier)

    # Generer un nombre nb_levier de fois l'algo UCB
    liste_levier = np.unique([gr.UCB(estimations=estimations, nbChosenLevier=[horizon*estimations[i] for i in range(len(estimations))]) for i in range(nb_fils_max)])
    #print(liste_levier)

    return liste_levier




  def generate_childNode(self, leviers, current_node) : 
    # Creer et ajouter les nodes de la liste en entree
    current_node.fils = set()
    for i in range(len(leviers)) : 
      current_node.addNode(Node(id=leviers[i], pere=current_node))
  

  def simulation(self, root_node, nb_child=3, height=10) : 
    """
    Simuler un arbre UCT dont le nombre de noeuds fils est au max 3 par defaut, et l'hauteur de l'arbre est donc par defaut 10
    """

    if height==0 : 
      nb_chosen_child = np.random.randint(1,nb_child+1)
      liste_levier = self.liste_leviers(self.P, nb_chosen_child)
      self.generate_childNode(liste_levier, root_node)

    else : 
      nb_chosen_child = np.random.randint(1,nb_child+1)
      liste_levier = self.liste_leviers(self.P, nb_chosen_child)
      self.generate_childNode(liste_levier, root_node)
      L = []
      for i in root_node.fils : 
        if len(L)!=nb_child : 
          L.append(i)
          self.simulation(i, nb_chosen_child, height-1)
      

    return root_node


  def exploitation(self, root_node, player=1) : 
    L = []
    if len(root_node.fils)==0 : 
      if self.P.is_finished() : 
        root_node.t+=1
      root_node.n += 1
    
    else : 
      P = self.P
      for i in root_node.fils : 
        if len(L)!=len(root_node.fils) : 
          L.append(i)
          if P.turn!=player : 
            move = np.random.randint(1,P.length-1)
            P.play(move,P.turn)
          P.play(i.id, player)
          self.P = P
          if P.is_finished() : 
            root_node.t += self.exploitation(i,player).t
          root_node.n+=self.exploitation(i,player).n
    
    return root_node


  def winning_rate_calculation(self, root_node) : 
    L = []
    r = []
    for i in root_node.fils :
      L.append(i)
      if i.n==0 : 
        r.append((i.t/1, i.id))
      else : r.append((i.t/i.n, i.id))
      if len(L)==len(root_node.fils) : break
    

    taux = [k for (k,_) in r]
    ID = [v for (_,v) in r]

    return ID[np.argmax(taux)]
    