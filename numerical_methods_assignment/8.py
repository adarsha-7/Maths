import os
import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, xn, n):
    h = (xn - x0) / n
    x_vals = np.linspace(x0, xn, n + 1)
    y_vals = np.zeros(n + 1)
    y_vals[0] = y0

    for i in range(n):
        y_vals[i + 1] = y_vals[i] + h * f(x_vals[i], y_vals[i])

    return x_vals, y_vals

def display_results(x_vals, y_vals):
    print("------------------------")
    print("Step   x       y")
    print("------------------------")
    for i in range(len(x_vals)):
        print(f"{i:<6} {x_vals[i]:<7.2f} {y_vals[i]:<10.3f}")

def plot_solution(x_vals, y_vals):
    plt.plot(x_vals, y_vals, 'o-', color='blue', label="Euler's Method")
    plt.title("Euler's Method Approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/euler_plot.png')
    plt.show()

    print("\nPlot saved as 'figures/euler_plot.png'")

def f(x, y):
    return x ** 2 + x

x0 = 0
y0 = 1
xn = 2
n = 20

x_vals, y_vals = euler_method(f, x0, y0, xn, n)
display_results(x_vals, y_vals)
plot_solution(x_vals, y_vals)
print("\nFinal approximation: y(", xn, ") =", round(y_vals[-1], 6))
