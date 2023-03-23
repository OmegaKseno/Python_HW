#Задача 26: Напишите программу, которая на вход принимает
#два числа A и B, и возводит число А в целую степень B с
#помощью рекурсии.
#Пример:
#A = 3; B = 5 -> 243 
#A = 2; B = 3 -> 8

numberA=int(input("Введите число A"))
numberB=int(input("Введите число B"))
 

def Exponentiation (numA,numB):

    if numB==1:
       return numA
    return  numA*Exponentiation (numA,numB-1)
  
result = Exponentiation (numberA,numberB)
print(result)
