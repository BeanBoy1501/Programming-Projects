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

#click function, creating x's and o's
def Click(arg):
    global player
    if player == 1:
        root.title("Player {}'s turn".format(player + 1))
        if btns[arg].cget('text') == '-':
            btns[arg].configure(text = 'X')
            values[arg] = 1
            player = 2
    elif player == 2:
        root.title("Player {}'s turn".format(player - 1))
        if btns[arg].cget('text') == '-':
            btns[arg].configure(text = 'O')
            values[arg] = 2
            player = 1

#creating buttons
for i in range(0,3):
    for j in range(0,3):
        btns.append(Button(text = '-', height = 8, width = 16, command = lambda x = counter: Click(x)))
        btns[counter].grid(row = i, column = j)
        counter += 1


print("seb gey")


    


        







root.mainloop()