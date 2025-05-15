from typing import List
from functools import reduce
from operator import mul


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.n: int
        self.s: str
        self.array: List[float]
        self.read_file()

    def read_file(self) -> None:
        with open(self.file_path) as f:
            self.n = int(f.readline())
            self.s = f.readline().strip()
            self.array = [float(num) for num in f.readline().strip().split(" ")]

    def calculate_expected_num_restriction_sites(self) -> List[float]:
        solution: List[int] = list()

        # mult_factor to calculate probability
        mult_factor: int = self.n - len(self.s) + 1

        for gc_percent in self.array:
            # liklihood of a given base given GC percent
            frequencies = {
                "A": (1 - gc_percent) / 2,
                "T": (1 - gc_percent) / 2,
                "C": gc_percent / 2,
                "G": gc_percent / 2,
            }
            # creates a list of liklihood for each base in s
            # then finds product of list, then multiplies by mult factor
            # then rounds and appends to solution list
            solution.append(
                round(
                    reduce(mul, [frequencies[nuc] for nuc in self.s]) * (mult_factor), 3
                )
            )

        return solution


def main() -> None:
    solution = Solution("problems/expected_num_restriction_sites/rosalind_eval.txt")
    expected_num_restriction_sites: List[float] = (
        solution.calculate_expected_num_restriction_sites()
    )
    printable_answer: str = " ".join(
        [str(num) for num in expected_num_restriction_sites]
    )
    print(printable_answer)


if __name__ == "__main__":
    main()
