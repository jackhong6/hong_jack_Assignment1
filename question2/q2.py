# CTA200H 2017 Problem Set 1, Question 2
# Jack Hong and Bill Kong

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


# Part A =========================================
def fact(n):
    """Return the factorial of n, where n is assumed to be an integer with n >= 0."""
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def comb(n, k):
    """Return n choose k."""
    if k == 0:
        return 1
    else:
        return int(fact(n) / (fact(k) * fact(n - k)))


# Part B ==========================================
def print_pascal_triangle(num_rows):
    """Print the first num_rows rows of Pascal's triangle."""
    for n in range(num_rows):
        for k in range(n + 1):
            print(comb(n, k)),
        print("\n")


# Part C ==========================================
def prob_k_heads(n, k, p):
    """Return the probability of obtaining k heads out of n coin tosses.
    
    Parameters:
        n: number of coin tosses (int)
        k: number of heads (int)
        p: probability of heads (e.g. prob of heads) (float)
    """
    return comb(n, k) * p**k * (1-p)**(n-k)


def prob_at_least_k_heads(n, k, p):
    """Return the probability of obtaining at least k heads out of n coin tosses.

    Parameters:
        n: number of coin tosses (int)
        k: minimum number of heads desired (int)
        p: probability of heads (e.g. prob of heads) (float)
    """
    ssf = 0
    for x in range(k, n+1):
        ssf = ssf + prob_k_heads(n, x, p)
    return ssf


# Part D =========================================
def coin_toss_sim(n, k, p, N):
    """Simulate n coin tosses with probability p of getting heads for each toss, N times. 
    Return fraction of experiments with at least k heads.
    """
    n_successes = 0
    for x in range(N):
        n_heads = 0
        for toss in range(n):
            if np.random.random() < p:
                n_heads = n_heads + 1
        if n_heads >= k:
            n_successes = n_successes + 1
    return float(n_successes) / N


def plot_coin_toss_sim(n, k, p, Ns):
    """Plot the results of the experiment in part D."""
    frac_success = []

    for N in Ns:
        frac_success.append(coin_toss_sim(n, k, p, N))

    plt.scatter(Ns, frac_success)
    plt.title("Fraction of successful trials vs the number of trials")
    plt.ylabel("Fraction of successful trials")
    plt.xlabel("N (the number of trials)")


def main():
    # Part b. print the first 20 rows of Pascal's triangle.
    print_pascal_triangle(20)

    # Part c.
    str_msg = "For values n=100, k=30, p=0.3 the probability of obtaining at least k heads in n flips is {:f}"
    n = 100
    k = 30
    p = 0.3
    print(str_msg.format(prob_at_least_k_heads(n, k, p)))

    # Part d. coin toss experiment with n=100, k=30, p=0.3 repeated N times
    Ns = [100, 1000, 10000]
    plot_coin_toss_sim(n, k, p, Ns)

    plt.show()


if __name__ == "__main__":
    main()
