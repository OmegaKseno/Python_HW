#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P.
#Помогите Кате отгадать задуманные Петей числа.
from random import randint

numberX = randint(1,1000)
numberY = randint(1,1000)
numberS = numberX + numberY
numberP = numberX * numberY
print(f"Петя загадал {numberX} и {numberY}, назвал сумму {numberS} ,произведение {numberP}")


answerX = 0
answerY = 1

for i in  range(numberS):
   
    answerX=answerX + 1
    answerY = 1 
    for j in range(numberS):
       
        result =   answerX + answerY
        result2 = answerX * answerY
        if result == numberS and result2==numberP:
            if answerY == numberY:
                print(f"Ответ {answerX},{answerY}")
            
        answerY=answerY + 1   
                
               
              
   
      
    