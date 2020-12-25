from tkinter import *

#6 x 7 board
#red vs yellow

root = Tk()
root.title("Connect 4")
root.minsize(900,500)

def Click(arg):
    print(arg)


def Restart():
    print("restart")

yellow_circle = PhotoImage(file = r"C:\\Users\\jbock\\OneDrive\\Desktop\\Programming Projects\\Python\\Unfinished\\Connect 4\\red_circle.png")

#creating the buttons
btns = []
counter = 0
for i in range(0, 6):
    for j in range(0, 7):
        btns.append(Button(root, height = 7, width = 14, image = yellow_circle, command = lambda x = counter: Click(x)))
        btns[counter].grid(row = i, column = j)
        counter += 1
Button(root, image = yellow_circle, height = 7, width = 14, command = Restart).grid(row = 3, column = 7)
    




root.mainloop()