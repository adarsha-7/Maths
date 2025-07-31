from math import sqrt, pi, exp

def simpsons_one_third(f, a, b, n):
    if n % 2 != 0 or a >= b:
        return None

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)

    return (h / 3) * total

def f(x):
    return (1 / sqrt(2 * pi)) * exp(-x ** 2 / 2)

a = -4
b = 4
n = 50

result = simpsons_one_third(f, a, b, n)
print("Approximated integral:", round(result, 8))
