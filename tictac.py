def grid(a,guide):
    layout = ("-"*7)+"\n"+"|"+a[0][0]+"|"+a[0][1]+"|"+a[0][2]+"|"+"\n"+("-"*7)+"\n"+"|"+a[1][0]+"|"+a[1][1]+"|"+a[1][2]+"|"+"\n"+("-"*7)+"\n"+"|"+a[2][0]+"|"+a[2][1]+"|"+a[2][2]+"|"+"\n"+("-"*7)
    print(layout)
    if guide:
        print("The grid below is for your guidance for choice")
        guidel = ("-"*7)+"\n"+"|1|2|3|"+"\n"+("-"*7)+"\n"+"|4|5|6|"+"\n"+("-"*7)+"\n"+"|7|8|9|"+"\n"+("-"*7)
        print(guidel)

def check(choice,rchoices):
    if choice in rchoices:
        rchoices.remove(choice)
        return True,rchoices
    else:
        return False,rchoices

def listchn(a,choice,pos):
    if pos == 1:
        a[0][0] = choice
    elif pos == 2:
        a[0][1] = choice
    elif pos == 3:
        a[0][2] = choice
    elif pos == 4:
        a[1][0] = choice
    elif pos == 5:
        a[1][1] = choice
    elif pos == 6:
        a[1][2] = choice
    elif pos == 7:
        a[2][0] = choice
    elif pos == 8:
        a[2][1] = choice
    elif pos == 9:
        a[2][2] = choice
    return a

def player1turn(a,guide,rchoices):
    grid(a,guide)
    print("Player 1 turn")
    choice = int(input("Choose location to place X: "))
    checked,rchoices = check(choice,rchoices)
    if checked:
        a = listchn(a,"X",choice)
        return a,guide,rchoices
    else:
        print("Please choose a location that isn't occupied")
        return player1turn(a,guide,rchoices)

def player2turn(a,guide,rchoices):
    grid(a,guide)
    print("Player 2 turn")
    choice = int(input("Choose location to place O: "))
    checked,rchoices = check(choice,rchoices)
    if checked:
        a = listchn(a,"O",choice)
        return a,guide,rchoices
    else:
        print("Please choose a location that isn't occupied")
        return player2turn(a,guide,rchoices)

def wincheck(a,rchoices):
    if a[0][0] == a[0][1] == a[0][2] == "X" or a[1][0] == a[1][1] == a[1][2] == "X" or a[2][0] == a[2][1] == a[2][2] == "X" or a[0][0] == a[1][0] == a[2][0] == "X" or  a[0][1] == a[1][1] == a[2][1] == "X" or a[0][2] == a[1][2] == a[2][2] == "X" or a[0][0] == a[1][1] == a[2][2] == "X" or a[0][2] == a[1][1] == a[2][0] == "X":
        print("Player 1 Wins!")
        return False
    elif a[0][0] == a[0][1] == a[0][2] == "O" or a[1][0] == a[1][1] == a[1][2] == "O" or a[2][0] == a[2][1] == a[2][2] == "O" or a[0][0] == a[1][0] == a[2][0] == "O" or  a[0][1] == a[1][1] == a[2][1] == "O" or a[0][2] == a[1][2] == a[2][2] == "O" or a[0][0] == a[1][1] == a[2][2] == "O" or a[0][2] == a[1][1] == a[2][0] == "O":
        print("Player 2 Wins!")
        return False
    elif rchoices[0] == "Tie!":
        print("It's a tie!!")
        return False
    else:
        return True
print("""The rules of the game is simple:
Player 1 is X
Player 2 is O
Use guidance grid to find block where you wish to place your choice
Try to get 3 in a row to win!!!
""")
guidec = input("Do you want a guidance grid?(Y for Yes, type anything else for No) ")
if guidec.lower() == "y":
    guide = True
else:
    guide = False
rchoices = [1,2,3,4,5,6,7,8,9,"Tie!"]
print("Let the game begin!")
gameon = True
a = [[" "," "," "],[" "," "," "],[" "," "," "]]
while True:
    a,guide,rchoices = player1turn(a,guide,rchoices)
    gameon = wincheck(a,rchoices)
    if gameon == False:
        break
    a,guide,rchoices = player2turn(a,guide,rchoices)
    gameon = wincheck(a,rchoices)
    if gameon == False:
        break
guide = False
grid(a,guide)
print("Thank you for playing")
