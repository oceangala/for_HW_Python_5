# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 

def summ_ab(a, b):
    if b <= 0:
        return a
    else:
        a+= 1
        b-= 1
        return summ_ab(a, b)
        
a, b = int(input('Введите первое число ')), int(input('Введите второе число '))
print(summ_ab(a, b))