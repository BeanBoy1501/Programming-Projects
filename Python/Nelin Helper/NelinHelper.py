from tkinter import *
import random

root = Tk()

root.title("IDI UCIT VISE")
root.geometry("250x100")

root.grid_columnconfigure(1, minsize=100)

result = StringVar()

def getRandomNumber():
    try:
        num1 = int(e1.get())
        num2 = int(e2.get())

        if (num1 > num2):
            result.set(random.randint(num2, num1))
        elif (num1 < num2):
            result.set(random.randint(num1, num2))
        else:
            result.set(num1)
    except ValueError:
        result.set("Invalid number")

l1 = Label(root, text = "First number")
l2 = Label(root, text = "Second number")

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(root, width = 10)
e2 = Entry(root, width = 10)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e1.insert(0, "1")
e2.insert(0, "2")

b1 = Button(root, text="Generate", command=getRandomNumber)
b1.grid(row = 2, column = 0)




l3 = Label(root, textvariable = result)

l3.grid(row = 2, column = 1)
result.set("-")



root.mainloop()