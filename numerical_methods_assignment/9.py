import os
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_2nd(f, x0, y0, xn, n):
    h = (xn - x0) / n
    x_vals = np.linspace(x0, xn, n + 1)
    y_vals = np.zeros(n + 1)
    y_vals[0] = y0

    for i in range(n):
        k1 = h * f(x_vals[i], y_vals[i])
        k2 = h * f(x_vals[i] + h, y_vals[i] + k1)
        y_vals[i + 1] = y_vals[i] + 0.5 * (k1 + k2)

    return x_vals, y_vals

def display_results(x_vals, y_vals):
    print("------------------------")
    print("Step   x       y")
    print("------------------------")
    for i in range(len(x_vals)):
        print(i, "   ", round(x_vals[i], 2), "  ", round(y_vals[i], 3))

def plot_solution(x_vals, y_vals):
    plt.plot(x_vals, y_vals, 'o-', color='green', label="RK2 Method")
    plt.title("Runge-Kutta 2nd Order")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/rk2_plot.png")
    plt.show()
    print("\nPlot saved as 'figures/rk2_plot.png'")

def f(x, y):
    return x ** 2 + x

x0 = 0
y0 = 1
xn = 2
n = 10

x_vals, y_vals = runge_kutta_2nd(f, x0, y0, xn, n)
display_results(x_vals, y_vals)
plot_solution(x_vals, y_vals)

print("\nFinal approximation: y(", xn, ") =", round(y_vals[-1], 6))
