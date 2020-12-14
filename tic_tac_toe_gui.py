from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()
root.minsize(370,395)
root.maxsize(370,395)

btns = []
values = [0,0,0,0,0,0,0,0,0]
counter = 0
player = 1
draw_if_9 = 1

#click function, creating x's and o's
def Click(arg):
    global player
    global draw_if_9
    if player == 1:
        root.title("Player {}'s turn".format(player + 1))
        if btns[arg].cget('text') == '-':
            btns[arg].configure(text = 'X')
            values[arg] = 1
            GameEndChecker()
            player = 2
            draw_if_9 += 1

    elif player == 2:
        root.title("Player {}'s turn".format(player - 1))
        if btns[arg].cget('text') == '-':
            btns[arg].configure(text = 'O')
            values[arg] = 2
            GameEndChecker()
            player = 1
            draw_if_9 += 1

#creating buttons
for i in range(0,3):
    for j in range(0,3):
        btns.append(Button(text = '-', height = 8, width = 16, command = lambda x = counter: Click(x)))
        btns[counter].grid(row = i, column = j)
        counter += 1



def GameEndChecker():
    global draw_if_9
    #checking draw
    if draw_if_9 == 9:
        messagebox.showwarning("Game over", "DRAW!!")

    #checking the win, player 1
    if values[0] == 1 & values[1] == 1 & values[2] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[3] == 1 & values[4] == 1 & values[5] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[6] == 1 & values[7] == 1 & values[8] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[0] == 1 & values[3] == 1 & values[6] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[1] == 1 & values[4] == 1 & values[7] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[2] == 1 & values[5] == 1 & values[8] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[6] == 1 & values[4] == 1 & values[2] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")
    elif values[0] == 1 & values[4] == 1 & values[8] == 1:
        messagebox.showwarning("Game Over", "Player 1 has WON!")

    #checking the win, player 2
    if values[0] == 2 & values[1] == 2 & values[2] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[3] == 2 & values[4] == 2 & values[5] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[6] == 2 & values[7] == 2 & values[8] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[0] == 2 & values[3] == 2 & values[6] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[1] == 2 & values[4] == 2 & values[7] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[2] == 2 & values[5] == 2 & values[8] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[6] == 2 & values[4] == 2 & values[2] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")
    elif values[0] == 2 & values[4] == 2 & values[8] == 2:
        messagebox.showwarning("Game Over", "Player 2 has WON!")


root.mainloop()