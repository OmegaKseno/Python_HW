#Задача 18:
#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N.
#Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

#Ввод: 10
#Ввод: 7
#1 2 1 8 9 6 5 4 3 4
#Вывод: 6
import random

numberN = int(input(" введите количество элементов в массиве: "))
numberX = int(input("введите число, которое необходимо проверить: "))
array = [random.randint(1,numberN) for _ in range(numberN)]
print(array)
best_max = 0
best_min = 0
temp = numberN
for i in range(len(array)):
    
    if array[i]-numberX<=temp and array[i]>numberX:  # если в условие array[i]>numberX добавить = то он будет показывать элементы равные Х
        temp = int(array[i]-numberX)
        best_max = array[i]
        print(temp)
    elif numberX-array[i]<=temp and array[i]<numberX:    
        temp = int(numberX-array[i])
        best_min = array[i]
        print(temp)
if numberX-best_min <= best_max-numberX:
    print("Вывод ",best_min)
else:
    print("Вывод ",best_max)          
