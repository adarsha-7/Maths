import math

x = [0.2, 0.22, 0.24, 0.26, 0.28, 0.3]
y = [1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139]

a = 0.21
b = 0.29

def factorial(n):
    return math.factorial(n)

values = []
for i in range(len(y) - 1):
    row = []
    for j in range(len(y) - i - 1):
        if i == 0:
            diff = round(y[j + 1] - y[j], 4)
        else:
            diff = round(values[i - 1][j + 1] - values[i - 1][j], 4)
        row.append(diff)
    values.append(row)

print("Difference Table:")
for i in range(len(y)):
    row = str(format(x[i], ".4f")).rjust(12) + str(format(y[i], ".4f")).rjust(12)
    for j in range(len(x) - 1 - i):
        row += str(format(values[j][i], ".4f")).rjust(12)
    print(row)

fa = y[0]
pa = (a - x[0]) / (x[1] - x[0])

for i in range(len(values)):
    current = values[i][0] / factorial(i + 1)
    for j in range(i + 1):
        current *= (pa - j)
    fa += current

print(f"Newton's forward interpolation: f({a}) is", fa)

n = len(x) - 1
fb = y[n]
pb = (b - x[n]) / (x[1] - x[0])

for i in range(len(values)):
    current = values[i][n - 1 - i] / factorial(i + 1)
    for j in range(i + 1):
        current *= (pb + j)
    fb += current

print(f"Newton's backward interpolation: f({b}) is", fb)
