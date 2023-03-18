#Задача 20:
#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;'
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.

#А русские буквы оцениваются так:
#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков.

#Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

#Ввод: ноутбук
#Вывод: 12

mystr = input(" введите слово: ")
dictionary_Rus = {'А':1,'В':1,'Е':1,'И':1,'Н':1,'О':1,'Р':1,'С':1,'Т':1,'Д':2,'К':2,'Л':2,'М':2,'П':2,'У':2,'Б':3,'Г':3,
                  'Ё':3,'Ь':3,'Я':3,'Й':4,'Ы':4,'Ж':5, 'З':5,'Х':5,'Ц':5,'Ч':5,'Ш':8,'Э':8,'Ю':8,'Ф':10,'Щ':10,'Ъ':10}
dictionary_Eng = {'A':1,'E':1,'I':1,'O':1,'U':1,'L':1,'N':1,'S':1,'T':1,'R':1,'D':2,'G':2,'B':3,
              'C':3,'M':3,'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':10,'Z':10}
checkEng = 'ABIOULNSTRDGBCMPFHVWYKJXQZ'
checkRu = 'АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ'
mystr = mystr.upper() 
countEng = 0
countRu = 0
statusLeng=0
result = 0
for i in range(len(mystr)):
     for j in range(len(checkEng)):
          if mystr[i]==checkEng[j]:
               countEng+=1
if countEng==len(mystr): 
    statusLeng=1  

for i in range(len(mystr)):
     for j in range(len(checkRu)):
          if mystr[i]==checkRu[j]:
               countRu+=1
if countRu==len(mystr):               
    statusLeng=2

if statusLeng == 1:
    for i in range(len(mystr)): 
         result+=int(dictionary_Eng[mystr[i]])
    print(result)     
elif statusLeng == 2:
    for i in range(len(mystr)): 
         result+=int(dictionary_Rus[mystr[i]])
    print(result)
else:
     print('Ваше слово введено  некорректно ')         

