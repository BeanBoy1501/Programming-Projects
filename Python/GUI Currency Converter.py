from tkinter import *
master = Tk()
master.minsize(400, 400)
master.maxsize(400, 400)
master.title("Currency Converter")

def Convert():
    if currency1.get() == "USD":
        if currency2.get() == "HRK":
            expression.set(textvar.get() * 6.22)
        elif currency2.get() == "EUR":
            expression.set(textvar.get() * 0.83)
        elif currency2.get() == "USD":
            expression.set(textvar.get())
        elif currency2.get() == "SEK":
            expression.set(textvar.get() * 8.46)
    elif currency1.get() == "EUR":
        if currency2.get() == "HRK":
            expression.set(textvar.get() * 7.54)
        elif currency2.get() == "EUR":
            expression.set(textvar.get())
        elif currency2.get() == "USD":
            expression.set(textvar.get() * 1.21)
        elif currency2.get() == "SEK":
            expression.set(textvar.get() * 10.25)
    elif currency1.get() == "HRK":
        if currency2.get() == "HRK":
            expression.set(textvar.get())
        elif currency2.get() == "EUR":
            expression.set(textvar.get() * 0.13)
        elif currency2.get() == "USD":
            expression.set(textvar.get() * 0.16)
        elif currency2.get() == "SEK":
            expression.set(textvar.get() * 1.36)
    elif currency1.get() == "SEK":
        if currency2.get() == "HRK":
            expression.set(textvar.get() * 0.74)
        elif currency2.get() == "EUR":
            expression.set(textvar.get() * 0.098)
        elif currency2.get() == "USD":
            expression.set(textvar.get() * 0.12)
        elif currency2.get() == "SEK":
            expression.set(textvar.get())
    



def press1(value1):
    currency1.set(value1)

def press2(value2):
    currency2.set(value2)


currency1 = StringVar()
currency1.set("EUR")
currency2 = StringVar()
currency2.set("USD")
result = IntVar()
textvar = DoubleVar()
expression = DoubleVar()

menu = Menu(master)
submenu1 = Menu(menu, tearoff=FALSE)
submenu2 = Menu(menu, tearoff=FALSE)
submenu1.add_command(label="EUR", command=lambda: press1("EUR"))
submenu1.add_command(label="USD", command=lambda: press1("USD"))
submenu1.add_command(label="HRK", command=lambda: press1("HRK"))
submenu1.add_command(label="SEK", command=lambda: press1("SEK"))
submenu2.add_command(label="EUR", command=lambda: press2("EUR"))
submenu2.add_command(label="USD", command=lambda: press2("USD"))
submenu2.add_command(label="HRK", command=lambda: press2("HRK"))
submenu2.add_command(label="SEK", command=lambda: press2("SEK"))
menu.add_cascade(label="1st currency", menu=submenu1)
menu.add_cascade(label="2nd currency", menu=submenu2)
master.config(menu=menu)
label1 = Label(master, textvariable=currency1).grid(row=1, column=0)
label2 = Label(master, textvariable=currency2).grid(row=2, column=0)
entry = Entry(master, textvariable=textvar).grid(row=1, column=1)
label3 = Label(master, textvariable=expression, relief=SUNKEN).grid(row=2, column=1, sticky=W)
button = Button(master, text = "Convert", command = Convert).grid(row = 1, rowspan = 2, column = 2, sticky = W + E + N + S)






master.mainloop()