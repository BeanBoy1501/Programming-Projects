import cryptocompare
import time
import os
import keyboard
import sys


f = open("C:\\Users\\jbock\\Desktop\\portfolio\\db.txt", "r+")


def updateCoinInfo(coinInput, coinAmountAdded):
    coinMatch = False
    f.seek(0)
    coin = ""
    while True: 
        char = f.read(1)
        if (char == ';'):
            if (coin == coinInput):
                coinMatch = True
                break
            else:
                char = ""
                f.readline(1)
        else:
            coin += char

    if (coinMatch):
        counter = 0
        total = ""
        currentPos = f.tell()
        while True:
            char = f.read(1)
            if (char == '\n' or char == ''):
                break
            else:
                total += char
                counter += 1
        
        result = int(total) + int(coinAmountAdded)
        f.seek(currentPos)
        f.write(str(result))

           
def allCoinInfo():
    coin = ""
    amount = ""
    coinDone = False
    coinsDict = {}
    f.seek(0)
    while True:
        char = f.read(1)
        if (char == ''):
            coinsDict[coin] = amount
            break
        elif (char == '\n'):
            coinsDict[coin] = amount
            coinDone = False
            coin = ""
            amount = "" 
        elif (coinDone != True):
            if (char != ';'):
                coin += char
            else:
                coinDone = True
                continue
        
        if (coinDone == True):
            amount += char
    
    return coinsDict


def printCoinInfo():
    allCoins = allCoinInfo()
    for coin in allCoins:
        print("%s: %s" % (coin, allCoins[coin]))


def mandatoryPrint():
    print("---------------------------------")
    print("Press q to quit")
    print("Press a for adding more money")
    print("Pres i for getting all coin info")
    print("---------------------------------")
    print("")


flag = False
while True:
    counter = 0
    if (not flag):
        os.system("cls")
        flag = True
    elif (keyboard.is_pressed('q')):
        print("")
        print("Quitting...")
        break

    elif (keyboard.is_pressed('i')):
        os.system("cls")
        mandatoryPrint()
        printCoinInfo()

    elif (keyboard.is_pressed('a')):
        os.system("cls")
        print("For which coin do you want to update info")
        print("Press the corresponding number")
        for coin in allCoinInfo():
            counter += 1
            print("%s -> %s " % (counter, coin))

f.close()