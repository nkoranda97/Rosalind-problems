from scipy.stats import binom


def heteroProb(k, n):
    return sum(binom.pmf(x, 2**k, 0.25) for x in range(n, 2**k + 1))


if __name__ == "__main__":
    print(heteroProb(7, 32))
