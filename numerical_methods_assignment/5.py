x = [0, 1, 3, 4, 5]
y = [0, 1, 81, 256, 625]
a = 2

def l(i):
    v = 1
    for j in range(len(x)):
        if i != j:
            v *= (a - x[j]) / (x[i] - x[j])
    return v

fx = 0
for i in range(len(x)):
    fx += l(i) * y[i]

print(f"Using Lagrange Interpolation, f({a}) = {fx}")
