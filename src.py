def predict_possible_move(width, length, coord1, coord2) : 
    
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