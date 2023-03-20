#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
#Затем пользователь вводит сами элементы множеств.
import random
numberN = int(input(" введите количество цифр в первом наборе : "))
numberM = int(input(" введите количество цифр во втором наборе : "))
result =""
First_Array = [random.randint(1,20) for _ in range(numberN)]
Second_Array = [random.randint(1,20) for _ in range(numberM)]

status = 0
result = []
print(First_Array)
print(Second_Array)

for i in range(len(First_Array)):
    for j in range(len(Second_Array)):
        count =int(0) 
        if First_Array[i]==Second_Array[j]and status!=Second_Array[j]:
          
           result.append(Second_Array[j])
           status = First_Array[i]
           Second_Array[j] = 0
min = 0
for i in range(len(result)):
    for j in range(len(result)):
        if result[i]<result[j]:
            min = result[j]
            result[j] = result[i]
            result[i] = min


print(result)

