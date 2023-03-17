#Задача №23. Решение в группах
#Дан массив, состоящий из целых чисел. Напишите
#программу, которая подсчитает количество
#элементов массива, больших предыдущего (элемента
#с предыдущим номером)
#Input: [0, -1, 5, 2, 3]
#Output: 2 (-1 < 5, 2 < 3)
#Примечание: Пользователь может вводить значения
#списка или список задан изначально.
import random

number = int(input('введите колличество элементов массива'))
array = [random.randint(-10,10) for _ in range(number)]

print (array)
count = 0
string_result = ""
for i in range(len(array)-1):
    
    if array[i]<array[i+1]:
        count+=1
        string_result+= f" {array[i]}<{array[i+1]}, "
print(f"{count},( {string_result}) ")        
