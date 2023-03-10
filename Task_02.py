#Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

    
number = int(input('введите число ->'))

sum = 0

while number >10:
        sum = sum + (int (number%10))
        number = (int (number/10))
else:
        result = number+sum        

print (result)