from math import pi, sin, exp

def compute_integral(f, x0, xn, divs):
    if divs <= 0 or x0 >= xn:
        return None

    h = (xn - x0) / divs
    total = f(x0) + f(xn)

    for i in range(1, divs):
        xi = x0 + i * h
        total += 2 * f(xi)

    return (h / 2) * total

def f(x):
    return sin(x) / exp(x)

x0 = 0
xn = pi
divs = 20

result = compute_integral(f, x0, xn, divs)
print("Approximated integral:", round(result, 8))
