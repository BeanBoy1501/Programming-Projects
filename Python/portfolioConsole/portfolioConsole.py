import cryptocompare
import time
import keyboard
import os
import sys


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

def newTransaction():
    print("new transaction")


while True:
    if (keyboard.is_pressed('r')):
            getCoinInfo('revolut')
    elif (keyboard.is_pressed('b')):
        getCoinInfo('binance')
    elif (keyboard.is_pressed('n')):
        newTransaction()
    elif (keyboard.is_pressed('q')):
        break
    elif (keyboard.is_pressed(' ')):
        mandatoryPrint()
        print("Invalid key pressed..")




    