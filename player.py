class Player : 
  def __init__(self, value) : 
    self.etiquette = value
    self.coordinate = set()
  
  def addCoordinate(self, coord) : 
    self.coordinate.add(coord)