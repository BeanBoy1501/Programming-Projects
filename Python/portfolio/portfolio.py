import cryptocompare
import time
import os
import keyboard
import sys
import msvcrt

f = open("C:\\Users\\jbock\\Desktop\\portfolio\\db.txt", "r+")

def flush():
    while msvcrt.kbhit():  
        msvcrt.getch()     

def amountBeforeDigit(number):
    numString = str(number)
    counter = 0
    for n in numString:
        if (n == '.'):
            break
        counter += 1
    return counter


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


def mandatoryPrint():
    print("---------------------------------")
    print("Press a for adding more money")
    print("Pres c for getting all coin info")
    print("Press q to quit")
    print("---------------------------------")
    print("")


flag = False
while True:
    counter = 0
    if (not flag):
        os.system("cls")
        mandatoryPrint()
        flag = True
    elif (keyboard.is_pressed('q')):
        print("")
        print("Quitting...")
        flush()
        break

    elif (keyboard.is_pressed('c')):
        os.system("cls")
        mandatoryPrint()
        printCoinInfo()

    elif (keyboard.is_pressed('a')):
        os.system("cls")
        mandatoryPrint()
        print("For which coin do you want to update info")
        print("Press the corresponding number")
        for coin in getCoinInfo():
            counter += 1
            print("%s -> %s " % (counter, coin))

        print("\nPress b if you wish to cancel")
        
        while True:
            if (keyboard.is_pressed('1')):
                wrongInput = False
                while True:
                    if (wrongInput):
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("You entered too big of a number, try again!")
                        moneyInput = input("Enter the amount of money you want to add > ")
                    else:
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("Enter the amount of money you want to add")
                        moneyInput = input("The number can be 10 digits max! > ")
                    if (len(moneyInput) <= 10):
                        break
                    else:
                        wrongInput = True
                updateCoinInfo("ETH", float(moneyInput))
                flag = False
                break

            elif (keyboard.is_pressed('2')):
                wrongInput = False
                while True:
                    if (wrongInput):
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("You entered too big of a number, try again!")
                        moneyInput = input("Enter the amount of money you want to add > ")
                    else:
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("Enter the amount of money you want to add")
                        moneyInput = input("The number can be 10 digits max! > ")
                    if (len(moneyInput) <= 10):
                        break
                    else:
                        wrongInput = True
                updateCoinInfo("BTC", float(moneyInput))
                flag = False
                break

            elif (keyboard.is_pressed('3')):
                wrongInput = False
                while True:
                    if (wrongInput):
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("You entered too big of a number, try again!")
                        moneyInput = input("Enter the amount of money you want to add > ")
                    else:
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("Enter the amount of money you want to add")
                        moneyInput = input("The number can be 10 digits max! > ")
                    if (len(moneyInput) <= 10):
                        break
                    else:
                        wrongInput = True
                updateCoinInfo("DOGE", float(moneyInput))
                flag = False
                break

            elif (keyboard.is_pressed('4')):
                wrongInput = False
                while True:
                    if (wrongInput):
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("You entered too big of a number, try again!")
                        moneyInput = input("Enter the amount of money you want to add > ")
                    else:
                        os.system("cls")
                        mandatoryPrint()
                        flush()
                        print("Enter the amount of money you want to add")
                        moneyInput = input("The number can be 10 digits max! > ")
                    if (len(moneyInput) <= 10):
                        break
                    else:
                        wrongInput = True
                updateCoinInfo("BNB", float(moneyInput))
                flag = False
                break

            elif (keyboard.is_pressed('b')):
                os.system("cls")
                mandatoryPrint()
                break
            
            elif (keyboard.is_pressed('q')):
                print("")
                print("Quitting...")
                flush()
                exit()

f.close()