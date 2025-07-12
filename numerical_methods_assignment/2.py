import sympy as sp

x = sp.symbols('x')

x0 = 1
f_sym = sp.exp(x) - 4 * x

f_prime_sym = sp.diff(f_sym, x)

func = sp.lambdify(x, f_sym, 'math')
funcf = sp.lambdify(x, f_prime_sym, 'math')

def truncate(num, n):
    factor = 10 ** n
    return int(num * factor) / factor

def newt(a, n=0, max_iter=100):
    x_new = truncate(a - func(a) / funcf(a), 4)
    print(str(truncate(a, 4)).rjust(12), str(x_new).rjust(12))

    if x_new == a or n >= max_iter:
        print("\nThe root is", x_new)
        return
    newt(x_new, n + 1, max_iter)

print("xn".rjust(12), "xn+1".rjust(12))
newt(x0)