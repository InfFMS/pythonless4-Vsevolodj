# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def drob(a,b):
    ma=1
    for value in range(1, max(a, b)+1):
        if a%value==0 and b%value==0:
           max=value
    return(a//ma, b//ma)
print(drob(55,10))
