from typing import List, Tuple
import time


def read_fasta(file_path: str) -> Tuple[str, str]:
    with open(file_path, "r") as file:
        sequences: List = []
        sequence: str = ""
        for line in file:
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
            else:
                sequence += line.strip()
        sequences.append(sequence)
    return sequences[0], sequences[1]


def compute_edit_distance(str1: str, str2: str) -> List[List[int]]:
    # initialize matrix
    matrix: List[List[int]] = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    for i in range(len(str1) + 1):
        matrix[0][i] = i
    for i in range(1, len(str2) + 1):
        matrix[i][0] = i

    # score matrix
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j - 1] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j] + 1
                )

    return matrix


def count_optimal_alignments(matrix: List[List[int]], str1: str, str2: str) -> int:
    memo = {}

    def align_sequences(i: int, j: int) -> int:
        # check if path has already been built and stored in memo
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            memo[(i, j)] = 1
            return 1

        cost_diag = matrix[i - 1][j - 1]
        if str1[j - 1] == str2[i - 1]:
            cost_diag -= 1
        cost_up = matrix[i - 1][j]
        cost_left = matrix[i][j - 1]
        min_cost = min(cost_diag, cost_up, cost_left)

        paths = 0
        if min_cost == cost_diag:
            paths += align_sequences(i - 1, j - 1)
        if min_cost == cost_up:
            paths += align_sequences(i - 1, j)
        if min_cost == cost_left:
            paths += align_sequences(i, j - 1)

        # add path to memo
        memo[(i, j)] = paths
        return paths

    return align_sequences(len(str2), len(str1))


def main() -> None:
    file_path: str = "problems/counting_optimal_alignments/test.txt"
    str1: str
    str2: str
    str1, str2 = read_fasta(file_path)

    start_time = time.time()
    matrix = compute_edit_distance(str1, str2)
    num_optimal: int = count_optimal_alignments(matrix, str1, str2)
    end_time = time.time()

    print(f"Number of optimal solutions: {num_optimal}")
    print(f"Execution time: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
