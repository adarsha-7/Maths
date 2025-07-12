import math

a, b, h = -1, 1, 0.1

def f(x):
    return math.exp(x)

x = [round(a, 4)]
while True:
    current_value = round(x[-1] + h, 4)
    if current_value <= b:
        x.append(current_value)
    else:
        break

y = [round(f(xi), 4) for xi in x]

header = "x".rjust(12) + "y".rjust(12)
for i in range(1, len(x)):
    header += ("del" + str(i)).rjust(12)
print(header)

values = []
for i in range(len(x) - 1):
    row = []
    for j in range(len(x) - i - 1):
        if i == 0:
            diff = round(y[j + 1] - y[j], 4)
        else:
            diff = round(values[i - 1][j + 1] - values[i - 1][j], 4)
        row.append(diff)
    values.append(row)

for i in range(len(x)):
    row = str(format(x[i], ".4f")).rjust(12) + str(format(y[i], ".4f")).rjust(12)
    for j in range(len(x) - 1 - i):
        row += str(format(values[j][i], ".4f")).rjust(12)
    print(row)