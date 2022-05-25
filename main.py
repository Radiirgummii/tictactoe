def choosing(field, player):
  if field == a1:
    a1 = player
  elif field == a2:
    a2 = player
  elif field == a3:
    a2 = player
  elif field == b1:
    a2 = player
  elif field == b2:
    a2 = player
  elif field == b3:
    a2 = player
  elif field == c1:
    a2 = player
  elif field == c2:
    a2 = player
  elif field == c3:
    a2 = player
  elif field == a2:
    a2 = player
  
  
a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
i = 0
p = "x"
while i < 9:
  print(p + " wich field do you want to claim?")
  f = input()
  choosing(f, p)
  if p == "x":
    p = "O"
  else:
    p = x
  print("  1 2 3 ")
  print(" -------")
  print("a|" + a1 + "|" + a2 + "|" + a3 + "|")
  print(" -------")
  print("b|" + b1 + "|" + b2 + "|" + b3 + "|")
  print(" -------")
  print("c|" + c1 + "|" + c2 + "|" + c3 + "|")
  print(" -------\n\n")
  if a1 == "x" and a2 == "x" and a3 == "x" or b1 == "x" and b2 == "x" and b3 == "x" or c1 == "x" and c2 == "x" and c3 == "x" or a1 == "x" and b1 == "x" and c1 == "x" or a2 == "x" and b2 == "x" and c2 == "x" or a3 == "x" and b3 == "x" and c3 == "x" or a1 == "x" and b2 == "x" and c3 == "x" or a3 == "x" and b2 == "x" and c1 == "x":
    print("x has won")
    exit()
  if a1 == "O" and a2 == "O" and a3 == "O" or b1 == "O" and b2 == "O" and b3 == "O" or c1 == "O" and c2 == "O" and c3 == "O" or a1 == "O" and b1 == "O" and c1 == "O" or a2 == "O" and b2 == "O" and c2 == "O" or a3 == "O" and b3 == "O" and c3 == "O" or a1 == "O" and b2 == "O" and c3 == "O" or a3 == "O" and b2 == "O" and c1 == "O":
    print("O has won")
    exit()
  i = i + 1
if i == 9:
  print("es ist unentschieden")
