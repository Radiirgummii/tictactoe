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



def choosing(player):
  global a1,a2,a3,b1,b2,b3,c1,c2,c3
  print(player + " wich field do you want to claim?")
  field = input()
  if field == "a1" and a1 == " ":
    a1 = player
  elif field == "a2" and a2 == " ":
    a2 = player
  elif field == "a3" and a3 == " ":
    a3 = player
  elif field == "b1" and b1 == " ":
    b1 = player
  elif field == "b2" and b2 == " ":
    b2 = player
  elif field == "b3" and b3 == " ":
    b3 = player
  elif field == "c1" and c1 == " ":
    c1 = player
  elif field == "c2" and c2 == " ":
    c2 = player
  elif field == "c3" and c3 == " ":
    c3 = player
  else:
    print(a1 ,"invalid Answer your Field is either taken or you haven't inputted a valid field")
    choosing(player)

def print_fields():
  global a1,a2,a3,b1,b2,b3,c1,c2,c3
  print("  1 2 3 ")
  print(" -------")
  print("a|" + a1 + "|" + a2 + "|" + a3 + "|")
  print(" -------")
  print("b|" + b1 + "|" + b2 + "|" + b3 + "|")
  print(" -------")
  print("c|" + c1 + "|" + c2 + "|" + c3 + "|")
  print(" -------\n\n")

while i < 9:
  print_fields()
  choosing(p)
  if p == "x":
    p = "O"
  else:
    p = "x"
  if a1 == "x" and a2 == "x" and a3 == "x" or b1 == "x" and b2 == "x" and b3 == "x" or c1 == "x" and c2 == "x" and c3 == "x" or a1 == "x" and b1 == "x" and c1 == "x" or a2 == "x" and b2 == "x" and c2 == "x" or a3 == "x" and b3 == "x" and c3 == "x" or a1 == "x" and b2 == "x" and c3 == "x" or a3 == "x" and b2 == "x" and c1 == "x":
    print("x has won")
    print_fields()
    exit()
  if a1 == "O" and a2 == "O" and a3 == "O" or b1 == "O" and b2 == "O" and b3 == "O" or c1 == "O" and c2 == "O" and c3 == "O" or a1 == "O" and b1 == "O" and c1 == "O" or a2 == "O" and b2 == "O" and c2 == "O" or a3 == "O" and b3 == "O" and c3 == "O" or a1 == "O" and b2 == "O" and c3 == "O" or a3 == "O" and b2 == "O" and c1 == "O":
    print("O has won")
    exit()
  i = i + 1
if i == 9:
  print("es ist unentschieden")
