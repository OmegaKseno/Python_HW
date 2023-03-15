#Задача 14: Требуется вывести все целые степени двойки 
#(т.е. числа вида 2k), не превосходящие числа N.

number = int(input('введите количество монет ->'))
temp =2
while number>temp:
    if temp*2<number:
        print(temp,end=" ")
        temp*=2
       
    else:
        print(temp,end=" ")
        temp*=2