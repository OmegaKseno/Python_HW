#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6

array_length = int(input('Введите колличество чисел'))
number_k = int(input('введите сдвиг'))
array =[i for i in range(1,array_length +1)]
print (array)

for i in range(number_k):
    array.insert(0,array.pop())
print(array)    