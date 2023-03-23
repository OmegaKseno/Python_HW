#Задача 28: Напишите рекурсивную функцию sum(a, b),
#возвращающую сумму двух целых неотрицательных чисел. Из
#всех арифметических операций допускаются только +1 и -1.
#Также нельзя использовать циклы.
numberA=int(input("Введите число A"))
numberB=int(input("Введите число B"))
 

def Sum_numbers (numA,numB):

    if numB==0:
       return numA

    return Sum_numbers (numA+1,numB-1)
  
result = Sum_numbers (numberA,numberB)
print(result)