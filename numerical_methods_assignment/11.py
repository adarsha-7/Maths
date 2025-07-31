import os
import numpy as np
import matplotlib.pyplot as plt

def least_squares_fit(x_data, y_data):
    n = len(x_data)
    sum_x = np.sum(x_data)
    sum_y = np.sum(y_data)
    sum_x2 = np.sum(x_data ** 2)
    sum_xy = np.sum(x_data * y_data)

    print("Normal equations:")
    print(n, "* a0 +", sum_x, "* a1 =", round(sum_y, 1))
    print(sum_x, "* a0 +", sum_x2, "* a1 =", round(sum_xy, 1))

    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    B = np.array([sum_y, sum_xy])

    solution = np.linalg.solve(A, B)
    a0 = solution[0]
    a1 = solution[1]
    return a0, a1

def plot_fit(x_data, y_data, a0, a1):
    plt.scatter(x_data, y_data, color='red', label='Data Points')

    x_line = np.linspace(min(x_data), max(x_data), 100)
    y_line = a0 + a1 * x_line
    plt.plot(x_line, y_line, color='blue', label='Fitted Line')

    x_pred = 2.5
    y_pred = a0 + a1 * x_pred
    plt.scatter([x_pred], [y_pred], color='green', marker='*', s=100,
                label='Prediction at x = 2.5')

    plt.title("Least Squares Regression")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/least_squares_plot.png")
    print("\nPlot saved as 'figures/least_squares_plot.png'")
    plt.show()

x_data = np.array([1, 2, 3, 4, 5, 6])
y_data = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])

a0, a1 = least_squares_fit(x_data, y_data)

print("Fitted line: y =", round(a0, 6), "+", round(a1, 6), "* x")

x_estimate = 2.5
y_estimate = a0 + a1 * x_estimate
print("Estimated y(", x_estimate, ") =", round(y_estimate, 6))

plot_fit(x_data, y_data, a0, a1)
