#Задача 32: Определить индексы элементов массива (списка),
#значения которых принадлежат заданному диапазону (т.е. не
#меньше заданного минимума и не больше заданного
#максимума)
#Ввод: [-5, 9, 0, 3, -1, -2, 1,
#4, -2, 10, 2, 0, -9, 8, 10, -9,
#0, -5, -5, 7]
#Вывод: [1, 9, 13, 14, 19]
import random
resultArray =[]
array = [random.randint(1,20) for _ in range(11)]
min = int(input(" минимальный "))
max = int(input(" максимальный "))
print (array)
for i in range(len(array)):
    if array[i] > min-1 and array[i] <max+1:
        resultArray.append(i)
print (resultArray)        