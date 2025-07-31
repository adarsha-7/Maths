import os
import numpy as np
import matplotlib.pyplot as plt

def exponential_least_squares(x_data, y_data):
    ln_y = np.log(y_data)

    n = len(x_data)
    sum_x = np.sum(x_data)
    sum_ln_y = np.sum(ln_y)
    sum_x2 = np.sum(x_data ** 2)
    sum_x_ln_y = np.sum(x_data * ln_y)

    print("Normal equations for ln(y) = ln(a) + b * x:")
    print(n, "* ln(a) +", sum_x, "* b =", round(sum_ln_y, 3))
    print(sum_x, "* ln(a) +", sum_x2, "* b =", round(sum_x_ln_y, 3))

    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    B = np.array([sum_ln_y, sum_x_ln_y])

    solution = np.linalg.solve(A, B)
    ln_a = solution[0]
    b = solution[1]
    a = np.exp(ln_a)

    return a, b

def plot_fit(x_data, y_data, a, b):
    plt.scatter(x_data, y_data, color='red', label='Data Points')

    x_line = np.linspace(min(x_data), max(x_data), 100)
    y_line = a * np.exp(b * x_line)
    plt.plot(x_line, y_line, color='blue', label='Fitted Curve')

    x_pred = 9
    y_pred = a * np.exp(b * x_pred)
    plt.scatter([x_pred], [y_pred], color='green', marker='*', s=100,
                label='Prediction at x = 9')

    plt.title("Exponential Fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/exp_fit.png")
    print("\nPlot saved as 'figures/exp_fit.png'")
    plt.show()

x_data = np.array([2, 4, 6, 8, 10])
y_data = np.array([4.077, 11.084, 30.128, 81.897, 222.62])

a, b = exponential_least_squares(x_data, y_data)

print("Fitted curve: y =", round(a, 6), "* e^(", round(b, 6), "* x )")

x_estimate = 9
y_estimate = a * np.exp(b * x_estimate)
print("Estimated y(", x_estimate, ") =", round(y_estimate, 6))

plot_fit(x_data, y_data, a, b)
