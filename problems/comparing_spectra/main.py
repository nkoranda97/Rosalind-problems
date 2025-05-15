from typing import List, Tuple
from collections import defaultdict


def find_minkowski_diff(
    array1: List[float], array2: List[float]
) -> defaultdict[float:int]:
    diff_freq: defaultdict[float:int] = defaultdict(int)

    for num1 in array1:
        for num2 in array2:
            diff_freq[abs(round(num1 - num2, 5))] += 1

    return diff_freq


def find_largest_multipicity(diff_freq: defaultdict[float:int]) -> Tuple[int, float]:
    max_count: int = float("-inf")
    num_max_count: float = None

    for key, value in diff_freq.items():
        if value > max_count:
            max_count = value
            num_max_count = key

    return max_count, num_max_count


def read_file(file_path: str) -> Tuple[List[float], List[float]]:
    with open(file_path, "r") as f:
        array1: List[float] = list(map(float, f.readline().strip().split(" ")))
        array2: List[float] = list(map(float, f.readline().strip().split(" ")))

    return array1, array2


def main() -> None:
    file_path: str = "problems/comparing_spectra/rosalind_conv.txt"
    array1, array2 = read_file(file_path)

    diff_freq = find_minkowski_diff(array1, array2)

    max_count, num_max_count = find_largest_multipicity(diff_freq)

    print(f"{max_count}\n{num_max_count}")


if __name__ == "__main__":
    main()
