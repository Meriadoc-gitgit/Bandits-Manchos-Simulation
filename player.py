class Player : 
  # INITIALISATIONS
  def __init__(self, etiquette) : 
    self.etiquette = etiquette
    self.coord = []
    self.total_move = 0

  # Add coordinates of the recent move
  def addCoordinates(self, coord) : 
    self.coord.append(coord)
  
  # Reset the information of the Player when playing
  def reset(self) : 
    self.coord = []
    self.total_move = 0