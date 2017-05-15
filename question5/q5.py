# CTA200H 2017 Problem Set 1, Question 5
# Jack Hong and Bill Kong

import numpy as np
import matplotlib.pyplot as plt


def deriv(f, x, delta):
    """Return the approximate derivative of f at x"""
    return (f(x + delta) - f(x)) / delta


def f(x):
    return x * (x - 1)


def dfdx(x):
    return (x - 1) + x


def main():
    x = 1
    deriv_estimates = []
    deltas = np.logspace(-4, -14, 10)
    for delta in deltas:
        deriv_estimates.append(deriv(f, x, delta))

    plt.scatter(deltas, deriv_estimates)
    plt.xlim([1e-14, 1e-4])
    plt.ylim([0.999, 1.00075])
    plt.xscale('log')
    plt.ylabel("Numerical estimate of the derivative")
    plt.xlabel("delta")

    plt.plot([1e-14, 1e-4], [dfdx(1), dfdx(1)], color='r', label='Exact derivative')
    plt.legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()