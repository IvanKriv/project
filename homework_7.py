from math import factorial
def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)

num = 5
for el in fact(num):
    print(el)