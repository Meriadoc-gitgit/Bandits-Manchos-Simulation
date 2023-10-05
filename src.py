import random 

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




# BANDITS-MANCHOTS  
def binary_gain(leviers, actions) : # rend le gain binaire corespondant au coup joue
  # random.random() rend un reel entre 0 et 1
  return 1 if random.random()<=leviers[actions] else 0




