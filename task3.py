# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
def Rimskie(n):
    if n==0:
        return ''
    elif n>=1000:
        n-=1000
        return 'M'+Rimskie(n)
    elif n>=900:
        n-=900
        return 'CM'+Rimskie(n)
    elif n>=500:
        n-=500
        return 'D'+Rimskie(n)
    elif n>=400:
        n-=400
        return 'CD'+Rimskie(n)
    elif n>=100:
        n-=100
        return 'C'+Rimskie(n)
    elif n>=90:
        n-=90
        return 'XC'+Rimskie(n)
    elif n>=50:
        n-=50
        return 'L'+Rimskie(n)
    elif n>=40:
        n-=40
        return 'XL'+Rimskie(n)
    elif n>=10:
        n-=10
        return 'X'+Rimskie(n)
    elif n>=9:
        n-=9
        return 'IX'+Rimskie(n)
    elif n >= 5:
        n -= 5
        return 'V' + Rimskie(n)
    elif n==4:
        n-=4
        return 'IV'+Rimskie(n)
    else:
        n -= 1
        return 'I'+Rimskie(n)
value=int(input())
print(Rimskie(value))
