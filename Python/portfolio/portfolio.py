#!/usr/bin/env
# -*- coding: UTF-8 -*-

import cryptocompare
import time
import os
import keyboard
import sys
import io
import platform
from termios import tcflush, TCIFLUSH

plt = platform.system()

f = open("db.txt", "r+")

if (plt == "Windows"):
    import msvcrt
    def flush():
        while msvcrt.kbhit():  
            msvcrt.getch() 

    def clearScreen():
        os.system("cls")

elif (plt == "Linux"):
    def flush():
        sys.stdout.flush()
        sys.stdin.flush()
        tcflush(sys.stdin, TCIFLUSH)

    def clearScreen():
        os.system("clear")
        


def amountBeforeDigit(number):
    numString = str(number)
    counter = 0
    for n in numString:
        if (n == '.'):
            break
        counter += 1
    return counter

def addRemainingDigits(number):
    numString = str(number)
    size = len(numString)
    if ("." in numString):
        for x in range(0, 15 - size):
            numString += "0"
    else:
        numString += "."
        for x in range(0, 15 - size - 1):
            numString += "0"
    return numString



def updateCoinInfo(coinInput, coinAmountAdded):
    coinMatch = False
    coin = ""
    counter = 0
    f.seek(0)
    while True:
        char = f.read(1)
        if (char == ';'):
            if (coin == coinInput):
                coinMatch = True
                break
            counter += 1
        
        if (counter == 2):
            counter = 0
            coin = ""

        elif (counter == 0):
            coin += char

    if (coinMatch):
        currentPos = f.tell()
        amount = ""
        while True:
            char = f.read(1)
            if (char == ';'):
                break
            amount += char
        
        resultingAmount = float(amount) + float(coinAmountAdded)
        resultingAmount = round(resultingAmount, 14 - amountBeforeDigit(resultingAmount))
        f.seek(currentPos)
        f.write(str(resultingAmount))
        
def removeCoin(coin, f):
    wholeDB = f.readline()
    
    f.close()

    f = open("db.txt", "w")
    
    dbList = wholeDB.split(";")
    index = dbList.index(coin)
    del dbList[len(dbList) - 1]
    #dbList.remove(index)
    del dbList[index + 1]
    #dbList.remove(index + 1)
    del dbList[index]

    finalString = ""
    for x in dbList:
        finalString += x
        finalString += ";"


    f.writelines(finalString)
    f.close()



def getCoinInfo():
    counter = 0
    coin = ""
    amount = ""
    coins = {}
    skipRead = False
    f.seek(0)
    while True:
        if (not skipRead):
            char = f.read(1)
        if (char == ''):
            break
        elif (counter == 2):
            coins[coin] = amount
            coin = ""
            amount = ""
            counter = 0
            skipRead = False
        elif (char == ';'):
            counter += 1
            if (counter == 2):
                skipRead = True
        elif (counter == 0):
            coin += char
        elif (counter == 1):
            amount += char
        

    return coins


def printCoinInfo():
    allCoins = getCoinInfo()
    sumOfAll = 0
    for coin in allCoins:
        coinUnitPriceEUR = cryptocompare.get_price(coin, "EUR")[coin]["EUR"]
        myCoinAmountPrice = float(coinUnitPriceEUR) * float(allCoins[coin])
        sumOfAll += float(myCoinAmountPrice)
        print("%s: %s ---> %s € ---> %s HRK " % (coin, allCoins[coin], myCoinAmountPrice, myCoinAmountPrice * 7.53))
    
    print("\nSum of all coins: %s € ---> %s HRK" % (sumOfAll, sumOfAll * 7.53))

    print("\nNOTE: The prices are not 100% correct, this is a really close estimate!")

    print("\nTHIS IS NOT COUNTING SHITCOINS -> $SHIB AND $ASS")


def mandatoryPrint():
    print("---------------------------------")
    print("Press a for adding more money/coins")
    print("Press r for removing a coin")
    print("Pres c for getting all coin info")
    print("Press q to quit")
    print("---------------------------------")
    print("")

def addNewCoin(f):
    flush()
    print("\nEnter abbreviated coin name (3/4 letters)")
    coinName = input("> ")
    print("Enter the coin amount you want to add")
    coinAmount = input("The number can be 15 characters max! > ")
    
    f.close()
    f = open("db.txt", "a")
    f.write(coinName)
    f.write(";")
    f.write(addRemainingDigits(coinAmount))
    f.write(";")
    f.close()

flag = False
while True:
    counter = 0
    if (not flag):
        clearScreen()
        mandatoryPrint()
        flag = True
    elif (keyboard.is_pressed('q')):
        print("")
        print("Quitting...")
        flush()
        break

    elif (keyboard.is_pressed('c')):
        clearScreen()
        mandatoryPrint()
        printCoinInfo()

    elif (keyboard.is_pressed('r')):
        clearScreen()
        mandatoryPrint()
        flush()
        print("Enter the coin which you want to remove")
        coinInput = input("Enter 3/4 characters > ")
        removeCoin(coinInput, f)
        f = open("db.txt", "r+")

        print("\n Removed {}".format(coinInput))
        

    elif (keyboard.is_pressed('a')):
        clearScreen()
        mandatoryPrint()
        print("For which coin do you want to update info")
        print("Press the corresponding number")
        for coin in getCoinInfo():
            counter += 1
            print("%s -> %s " % (counter, coin))

        print("\nPress a if you wish to add a new coin")
        print("Press b if you wish to cancel")   

        while True:
            flush()
            x = keyboard.read_key() #needed to absorb the previous keypress of the letter a
            readKey = keyboard.read_key()

            if (isinstance(readKey, int)):
                if (int(readKey) <= len(getCoinInfo())):
                    wrongInput = False
                    while True:
                        if (wrongInput):
                            clearScreen()
                
                            mandatoryPrint()
                            flush()
                            print("You entered too big of a number, try again!")
                            moneyInput = input("Enter the coin amount you want to add > ")
                        else:
                            clearScreen()
                
                            mandatoryPrint()
                            flush()
                            print("Enter the coin amount you want to add")
                            moneyInput = input("The number can be 15 characters max! > ")
                        if (len(moneyInput) <= 15):
                            break
                        else:
                            wrongInput = True
                    
                    updateCoinInfo(list(getCoinInfo())[int(readKey) - 1], float(moneyInput))
                    flag = False
                    break
            elif (isinstance(readKey, str)):
                if (readKey == "a"):
                    addNewCoin(f)

                    f = open("db.txt", "r+")

                    clearScreen()
                    mandatoryPrint()
                    printCoinInfo()

                    break

                elif (readKey == "b"):
                    clearScreen()
                    mandatoryPrint()

                elif (readKey == "q"):
                    flush()
                    break



f.close()