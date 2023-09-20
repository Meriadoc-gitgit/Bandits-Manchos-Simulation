"""
def find_winning_quadruplets(width, length, coord1, coord2) : 
    
  # Input error problem
  if coord1 > width : 
      print("Warning : Plateau width exceeded, value in range of [0, ",width,"] required")
  elif coord2 > length : 
    print("Warning : Plateau length exceeded, value in range of [0, ",length,"] required")
        
  L = []
  sub_L = []

  # Start
  if coord1>=3 : 
    for j in range(4) : 
      sub_L.append((coord1-j,coord2))
    L.append(sub_L)
    sub_L=[]
  if width-coord1>=4 : 
    for j in range(4) : 
      sub_L.append((coord1+j,coord2))
    L.append(sub_L)
    sub_L=[]
  if coord2>=3 : 
    for j in range(4) : 
      sub_L.append((coord1,coord2-j))
    L.append(sub_L)
    sub_L=[]
  if length-coord2>=4 : 
    for j in range(4) : 
      sub_L.append((coord1,coord2+j))
    L.append(sub_L)
    sub_L=[]
  if coord1>=3 and coord2>=3 : 
    for j in range(4) : 
      sub_L.append((coord1-j,coord2-j))
    L.append(sub_L)
    sub_L=[]
  if width-coord1>=4 and coord2>=3 : 
    for j in range(4) : 
      sub_L.append((coord1+j,coord2-j))
    L.append(sub_L)
    sub_L=[]
  if coord1>=3 and length-coord2>=4 : 
    for j in range(4) : 
      sub_L.append((coord1-j,coord2+j))
    L.append(sub_L)
    sub_L=[]
  if width-coord1>=4 and length-coord2>=4 : 
    for j in range(4) : 
      sub_L.append((coord1+j,coord2+j))
    L.append(sub_L)
    sub_L=[]
  return L
"""

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