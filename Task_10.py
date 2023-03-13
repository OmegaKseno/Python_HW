#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.
from random import randint
temp = 1
while temp:
    numberOfCoins = input('введите количество монет ->')
    if numberOfCoins.isdigit():
        numberOfCoins =  int(numberOfCoins)
        tails = 0
        eagle = 0
        for i in  range(numberOfCoins): 
            coin =   randint(0,1)
            print(coin,end = " ") 
            if coin == 1:
                tails = tails+1
            else:
                eagle = eagle+1    
        if eagle<tails:
            print(f"минимальное количество монет которые нужно перевернуть -> {eagle} ")
        else:
            print(f"минимальное количество монет которые нужно перевернуть -> {tails}")
        temp=0
    else:
        print('Введите целое число')            



