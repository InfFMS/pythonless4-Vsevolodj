# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
N = int(input())
s=["*"]
s = s*(N+1)
for j in range(1,N+1):
    print("".join(s[0:j]))