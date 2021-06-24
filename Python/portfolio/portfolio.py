#!/usr/bin/env
# -*- coding: UTF-8 -*-

import cryptocompare
import time
import os
import keyboard
import sys
import io
import platform

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
        from termios import tcflush, TCIFLUSH
        sys.stdout.flush()
        sys.stdin.flush()
        tcflush(sys.stdin, TCIFLUSH)

    def clearScreen():
        os.system("clear")
        

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


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
    f.seek(0)
    wholeDB = f.read()
    
    f.close()

    f = open("db.txt", "w")
    
    dbList = wholeDB.split(";")
    index = dbList.index(coin)
    del dbList[len(dbList) - 1]

    del dbList[index + 1]

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
    print("Press m for modifying money/coins")
    print("Press r for removing a coin")
    print("Pres c for getting all coin info")
    print("Press q to quit")
    print("---------------------------------")
    print("")

def addNewCoin(f):
    flush()
    clearScreen()
    
    while True:
        print("If you wish to quit, type 'quit'.")
        print("\nEnter abbreviated coin name (3~5 letters)")
        flush()
        coinName = input("> ")

        if (coinName in getCoinInfo()):
            clearScreen()
            print("You already have this coin in your portfolio.\n")
        elif (coinName in list(cryptocompare.get_coin_list(True))):
            break
        elif (coinName == "quit"):
            break
        else:
            clearScreen()
            print("This coin isn't in the cryptocompare coin list, try again.\n")

    if (coinName != "quit"):
        while True:
            clearScreen()
            print("If you wish to quit, type 'quit'.\n")
            print("Enter the coin amount you want to add\n")
            coinAmount = input("The number can be 15 characters max! > ")
            if (len(coinAmount) <= 15 & is_number(coinAmount)):
                break
            elif (coinAmount == "quit"):
                break
            else:
                clearScreen()
                print("Wrong input, try again.\n")
        
        if (coinAmount != "quit"):
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
        flush()
        print("If you wish to cancel, type quit\n")
        print("Enter the coin which you want to remove")

        quitRemove = False
        while True:
            coinInput = input("Enter 3/4 characters > ")
            if (coinInput in getCoinInfo()):
                break
            elif (coinInput == "quit"):
                quitRemove = True
                break
            else:
                print("\nThis coin isn't in your portfolio, try again.")

        if (not quitRemove):
            removeCoin(coinInput, f)
            f = open("db.txt", "r+")

            clearScreen()
            mandatoryPrint()
            print("\nRemoved {}".format(coinInput))
            
        
        else:
            clearScreen()
            mandatoryPrint()

        

    elif (keyboard.is_pressed('m')):
        clearScreen()
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
                
            if (readKey == "a"):
                flush()
                addNewCoin(f)

                f = open("db.txt", "r+")

                clearScreen()
                mandatoryPrint()
                break

            elif (readKey == "b"):
                clearScreen()
                mandatoryPrint()
                break

            elif (readKey == "q"):
                flush()
                break

            elif (int(readKey) >= 0):
                if (int(readKey) <= len(getCoinInfo())):
                    wrongInput = False
                    while True:
                        if (wrongInput):
                            clearScreen()
                
                            mandatoryPrint()
                            flush()
                            print("Wrong input, try again!\n")
                            print("If you wish to cancel, type 'quit'.\n")
                            print("Enter the coin amount you want to add, if you want to subtract put a minus before the amount")
                            moneyInput = input("The number can be 15 characters max! > ")
                        else:
                            clearScreen()
                            mandatoryPrint()
                            flush()
                            print("If you wish to cancel, type quit\n")
                            print("Enter the coin amount you want to add, if you want to subtract put a minus before the amount")
                            moneyInput = input("The number can be 15 characters max! > ")
                        if (len(moneyInput) <= 15 & is_number(moneyInput)):
                            break
                        elif (moneyInput == "quit"):
                            break
                        else:
                            wrongInput = True
                    
                    if (moneyInput == "quit"):
                        clearScreen()
                        mandatoryPrint()
                        flush()
                        break

                    else:
                        updateCoinInfo(list(getCoinInfo())[int(readKey) - 1], float(moneyInput))
                        flag = False
                        break
            



f.close()