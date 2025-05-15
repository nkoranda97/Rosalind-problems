from typing import Set


class Solution:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.n: int
        self.set1: Set[int]
        self.set2: Set[int]
        self._read_file()

        self.union = self.set1 | self.set2
        self.intersect = self.set1 & self.set2
        self.set1_sub_set2 = self.set1 - self.set2
        self.set2_sub_set1 = self.set2 - self.set1
        self.set1_comp = self._calc_set_complement(self.set1)
        self.set2_comp = self._calc_set_complement(self.set2)

    def _read_file(self) -> None:
        with open(self.file_path) as f:
            self.n = int(f.readline().strip())
            self.set1 = set(map(int, f.readline().strip()[1:-1].split(", ")))
            self.set2 = set(map(int, f.readline().strip()[1:-1].split(", ")))

    def _calc_set_complement(self, set_: Set[int]) -> Set[int]:
        return {i for i in range(1, self.n + 1)} - set_

    def write_set_operations(self, output_file_path: str) -> None:
        with open(output_file_path, "w") as f:
            f.write(f"{self.union}\n")
            f.write(f"{self.intersect}\n")
            f.write(f"{self.set1_sub_set2}\n")
            f.write(f"{self.set2_sub_set1}\n")
            f.write(f"{self.set1_comp}\n")
            f.write(f"{self.set2_comp}\n")


def print_solutions() -> None:
    file_path = "problems/intro_set_operations/rosalind_seto.txt"
    output_file_path = "problems/intro_set_operations/output.txt"
    solution = Solution(file_path)
    solution.write_set_operations(output_file_path)


def main() -> None:
    print_solutions()


if __name__ == "__main__":
    main()
