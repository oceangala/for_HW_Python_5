# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# # раз решение        
# def poem_rhythm(poem):
#     count = 0
#     for i in stih[0]:
#         if i in 'аеёиоуэыюя':
#             count += 1
#     for i in range(1, len(stih)):
#         count_i = 0
#         for j in stih[i]:
#             if j in 'аеёиоуэыюя':
#                 count_i += 1
#         if count_i != count:
#             return False
#     else:
#         return True


# stih = input().lower().split()
# if poem_rhythm(stih):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# два решение

def poem_rhythm(poem):
    return (len(set(map(lambda x: sum(1 for i in x if i in 'аеёиоуэыюя'), poem))) == 1)



stih = input().lower().split()
if poem_rhythm(stih):
    print('Парам пам-пам')
else:
    print('Пам парам')