import cryptocompare
import time
import keyboard
import os
import sys

db = open("C:\\Users\\jbock\\OneDrive\\Desktop\\GitHub\\Programming-Projects\\Python\\db.txt", "w+")

revolutCoins = ["BTC", "ETH"]
binanceCoins = ["DOGE", "BNB"]
rMoneyInvested = [53.69, 168.36] #EUR
bMoneyInvested = [98.76, 84.97]  #EUR


def mandatoryPrint():
    print("Press R for Revolut balance, B for Binance balance")
    print("Press N for a new transaction")
    print("Press Q for quit")
    print("---------------------------")
    print("")

os.system("cls")
mandatoryPrint()

def getCoinInfo(app):

    if (app == 'revolut'):
        os.system('cls')
        mandatoryPrint()

        for coin in revolutCoins:
            print("%s --> %s" % (coin, cryptocompare.get_price(coin)[coin]['EUR']))

    elif (app == 'binance'):
        os.system('cls')
        mandatoryPrint()

        for coin in binanceCoins:
            print("%s --> %s" % (coin, cryptocompare.get_price(coin)[coin]['EUR']))

counter = 0

def transactionInput(app):
    db.seek(0)
    invalidInput = True
    print("Enter the cryptocurrency which you want to buy")
    if (app == 'revolut'):
        print("Coins avaliable: %s" % (revolutCoins))
        while True:
            coinInput = input()
            for coin in revolutCoins:
                if (coinInput == coin):
                    invalidInput = False
                    break
            if (invalidInput):
                print("Invalid input, try again")
            else:
                break
    elif (app == 'binance'):
        print("Coins avaliable: %s" % (binanceCoins))
        while True:
            coinInput = input()
            for coin in binanceCoins:
                if (coinInput == coin):
                    invalidInput = False
                    break
            if (invalidInput):
                print("Invalid input, try again")
            else:
                break
    
    print(coinInput)
    moneyInput = input("Enter the amount of money you want to invest")


    

#def binanceTransaction():


def newTransaction():
    os.system('cls')
    print("Choose which new transaction you want to do")
    print("1. new Revolut transaction")
    print("2. new Binance transaction")
    print("Press E for exit back to main menu")
    print("------------------------------------")
    print("")
    while True:
        if (keyboard.is_pressed('e')):
            break
        elif (keyboard.is_pressed('1')):
            transactionInput("revolut")
        elif (keyboard.is_pressed('2')):
            transactionInput("binance")





while True:
    if (keyboard.is_pressed('r')):
        getCoinInfo('revolut')
    elif (keyboard.is_pressed('b')):
        getCoinInfo('binance')
    elif (keyboard.is_pressed('n')):
        newTransaction()
    elif (keyboard.is_pressed('q')):
        break




    