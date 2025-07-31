import numpy as np
import matplotlib.pyplot as plt

h, N, n = 0.1, 11, 9
a, b, c, d = 4.2, -2, -2.2, -0.1

A = np.zeros((n, n))
for i in range(n):
    A[i][i] = b
    if i > 0: A[i][i - 1] = a
    if i < n - 1: A[i][i + 1] = c

B = np.full(n, d)
y_internal = np.linalg.solve(A, B)

y = np.zeros(N)
y[1:N-1] = y_internal

x = np.linspace(0, 1, N)

print("x      y")
for i in range(N):
    print(round(x[i], 2), " ", round(y[i], 6))

plt.plot(x, y, 'bo-', label='Numerical Solution')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Finite Difference Method")
plt.grid(True)
plt.legend()
plt.show()
