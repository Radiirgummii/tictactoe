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
w = False


def choosing(player):
  global a1,a2,a3,b1,b2,b3,c1,c2,c3
  print(f"{player} wich field do you want to claim?")
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
    print("invalid Answer your Field is either taken or you haven't inputted a valid field")
    choosing(player)

def print_fields():
  global a1,a2,a3,b1,b2,b3,c1,c2,c3
  print(f"  1 2 3 \n -------\na|{a1}|{a2}|{a3}|\n -------\nb|{b1}|{b2}|{b3}|\n -------\nc|{c1}|{c2}|{c3}|\n -------\n\n")

for i in range(1,10,1):
  print_fields()
  choosing(p)
  if p == "x":
    p = "O"
  else:
    p = "x"
  if a1 == "x" and a2 == "x" and a3 == "x" or b1 == "x" and b2 == "x" and b3 == "x" or c1 == "x" and c2 == "x" and c3 == "x" or a1 == "x" and b1 == "x" and c1 == "x" or a2 == "x" and b2 == "x" and c2 == "x" or a3 == "x" and b3 == "x" and c3 == "x" or a1 == "x" and b2 == "x" and c3 == "x" or a3 == "x" and b2 == "x" and c1 == "x":
    print("\n\n\n\n __   __   _                                          \n \\ \\ / /  | |                                         \n  \\ V /   | |__    __ _  ___   __      __ ___   _ __  \n   > <    | '_ \\  / _` |/ __|  \\ \\ /\ / // _ \\ | '_ \\ \n  / . \\   | | | || (_| |\\__ \\   \\ V  V /| (_) || | | |\n /_/ \\_\\  |_| |_| \\__,_||___/    \\_/\\_/  \\___/ |_| |_|\n\n")
    w= True
    break
  if a1 == "O" and a2 == "O" and a3 == "O" or b1 == "O" and b2 == "O" and b3 == "O" or c1 == "O" and c2 == "O" and c3 == "O" or a1 == "O" and b1 == "O" and c1 == "O" or a2 == "O" and b2 == "O" and c2 == "O" or a3 == "O" and b3 == "O" and c3 == "O" or a1 == "O" and b2 == "O" and c3 == "O" or a3 == "O" and b2 == "O" and c1 == "O":
    print("\n\n\n\n   ____    _                                         \n  / __ \\  | |                                        \n | |  | | | |__    __ _  ___  __      __ ___   _ __  \n | |  | | | '_ \\  / _` |/ __| \\ \\ /\\ / // _ \\ | '_ \\ \n | |__| | | | | || (_| |\\__ \\  \\ V  V /| (_) || | | |\n  \\____/  |_| |_| \\__,_||___/   \\_/\\_/  \\___/ |_| |_|\n\n\n")
    w = True
    break
if w is False:
  print("\n\n\nes ist unentschieden")
print_fields()