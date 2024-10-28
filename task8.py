# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def prostmnozh(a):
    s = []
    def isPrime(n):
        for i in range(2, n + 1):
            if n % i == 0 and n != i:
                return 0
            if n % i == 0 and n == i:
                return 1
        return 0
    i = 2
    while i <= a + 1:
        if isPrime(i) == 1 and a % i == 0:
            s = s + [i]
            a = a / i
            prostmnozh(a)
        else:
            i += 1
    s = str(s)
    s = s.replace(", ", "*")
    return s[1:-1]
print(prostmnozh(int(input())))