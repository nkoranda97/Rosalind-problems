def binomial_coefficient(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def sum_combinations(n: int, m: int) -> int:
    total = 0
    for k in range(m, n + 1):
        total += binomial_coefficient(n, k)
    return total


def main():
    n = 1946
    m = 835
    result: int = sum_combinations(n, m)
    print(result % 1000000)


if __name__ == "__main__":
    main()
