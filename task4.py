# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    nod = a + b
    print(nod)
a = int(input())
b = int(input())
print(NOD(a,b))

