def count_subsets(n: int) -> int:
    """counts subsets of set of size n

    Args:
        n (int): size of set

    Returns:
        int: number of subsets of set of size n modulo 1000000
    """

    return (2**n) % 1000000


if __name__ == "__main__":
    print(count_subsets(837))
