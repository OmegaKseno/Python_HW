#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов 
#сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала 
#в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

number = int(input('введите число ->'))
if number%6==0 and number>6:
   sum = int(number/3)
   guis=int(sum/2)
   girl = int(guis*4)
   print(number,'сделали->',guis,girl,guis)
elif number < 6:
   print('вы ввели маленькое число,введите число больше 6')
else:    
    temp = (number//6)*6
    sum = int(temp/3)
    guis=int(sum/2)
    girl = int(guis*4)
    print(temp,'сделали ->',guis,girl,guis,'осталось->',number-temp)