import math

A = 0.5
B = 1
xn = []

def func(x):
    return x**2 - math.sin(x)

def truncate(num, n):
    factor = 10 ** n
    return int(num * factor) / factor

def bisc(a, b):
    x = truncate((a + b) / 2, 4)
    fx = truncate(func(x), 4)
    xn.append(x)

    print(
        str(len(xn)).rjust(4), str(a).rjust(12), str(b).rjust(12), str(x).rjust(12),
        ("-ve" if math.copysign(1, fx) == -1 else "+ve").rjust(20)
    )

    if len(xn) >= 2 and xn[-1] == xn[-2]:
        print("\nThe root is ", x)
    elif fx < 0:
        bisc(x, truncate(b, 4))
    elif fx > 0:
        bisc(truncate(a, 4), x)
    else:
        print("\nThe root is ", x)

print(
    "Iter".rjust(4), "a".rjust(12), "b".rjust(12), "x".rjust(12),
    "sign of f(x)".rjust(20)
)

bisc(A, B)
