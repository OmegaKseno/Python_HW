#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no
numberN = int(input('введите первое число n  ->'))
numberM = int(input('введите второе число m ->'))
number = int(input('введите  количество длоек которые хотите отломить  ->'))

if number<numberN*numberM :
    if number%numberN==0 or number%numberM==0:
        print('n =',numberN,'m =',numberM,'нужно отломить->',number,'результат->','yes')
    else:
        print('n =',numberN,'m =',numberM,'нужно отломить->',number,'результат->','no')
else:
    print('n =',numberN,'m =',numberM,'нужно отломить->',number,'результат->','no')