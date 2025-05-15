from typing import List, Tuple


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


def compute_edit_distance(str1: str, str2: str) -> Tuple[List[List[int]], int]:
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

    return matrix, matrix[-1][-1]


def align_sequences(matrix: List[List[int]], str1: str, str2: str) -> Tuple[str, str]:
    i: int = len(str2)
    j: int = len(str1)
    aligned_1: str = ""
    aligned_2: str = ""

    while i > 0 and j > 0:
        # compute min score and add to strings accordingly
        cost_diag = matrix[i - 1][j - 1]
        if str1[j - 1] == str2[i - 1]:
            cost_diag -= 1
        cost_up = matrix[i - 1][j]
        cost_left = matrix[i][j - 1]
        min_cost = min(cost_diag, cost_up, cost_left)
        # if any costs are equal, cost_diag is the chosen direction
        if min_cost == cost_diag:
            aligned_1 += str1[j - 1]
            aligned_2 += str2[i - 1]
            i -= 1
            j -= 1
        elif min_cost == cost_up:
            aligned_1 += "-"
            aligned_2 += str2[i - 1]
            i -= 1
        else:
            aligned_1 += str1[j - 1]
            aligned_2 += "-"
            j -= 1

    # add gaps to the sequence that has iterator greater than zero
    while i > 0:
        aligned_2 += str2[i - 1]
        aligned_1 += "-"
        i -= 1

    while j > 0:
        aligned_1 += str1[j - 1]
        aligned_2 += "-"
        j -= 1

    # return in reverse order because they were built in reverse
    return aligned_1[::-1], aligned_2[::-1]


def main() -> None:
    file_path: str = "problems/edit_distance_alignment/test.txt"
    str1: str
    str2: str
    str1, str2 = read_fasta(file_path)

    matrix, edit_distance = compute_edit_distance(str1, str2)

    aligned_1, aligned_2 = align_sequences(matrix, str1, str2)

    # final
    print(f"{edit_distance}\n{aligned_1}\n{aligned_2}")

    for line in matrix:
        print(line)


if __name__ == "__main__":
    main()
