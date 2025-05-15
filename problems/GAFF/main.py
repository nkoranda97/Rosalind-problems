import numpy as np
from Bio.Align import substitution_matrices
import sys


class GlobalAlign:
    def __init__(self, seq1: str, seq2: str):
        self.seq1 = seq1
        self.seq2 = seq2
        self.scoring_matrix = substitution_matrices.load("BLOSUM62")
        self.opening_penalty = 11
        self.extension_penalty = 1

    def create_matrix(self):
        # create 3-dimensional matrix filled with -inf
        matrix = np.full(
            (len(self.seq1) + 1, len(self.seq2) + 1, 3), -np.inf, dtype=np.float32
        )
        # diag dim set to [,,0]
        matrix[0, 0, 0] = 0
        # left dim set to [,,1]
        for i in range(1, len(self.seq1) + 1):
            matrix[i, 0, 1] = -self.opening_penalty - self.extension_penalty * (i - 1)
        # up dim set to [,,2]
        for j in range(1, len(self.seq2) + 1):
            matrix[0, j, 2] = -self.opening_penalty - self.extension_penalty * (j - 1)

        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                # for diag dim, we take max diag of all three dims + blossum score
                matrix[i, j, 0] = (
                    max(
                        matrix[i - 1, j - 1, 0],
                        matrix[i - 1, j - 1, 1],
                        matrix[i - 1, j - 1, 2],
                    )
                    + self.scoring_matrix[self.seq1[i - 1], self.seq2[j - 1]]
                )
                # for left dim, we take max of diag dim - opening penalty vs left dim - extension penalty
                matrix[i, j, 1] = max(
                    matrix[i - 1, j, 0] - self.opening_penalty,
                    matrix[i - 1, j, 1] - self.extension_penalty,
                )
                # for up dim, we take max diag dim - opening penalty vs up dim - extension penalty
                matrix[i, j, 2] = max(
                    matrix[i, j - 1, 0] - self.opening_penalty,
                    matrix[i, j - 1, 2] - self.extension_penalty,
                )

        return matrix

    def align(self) -> tuple[int, str, str]:
        matrix = self.create_matrix()

        i = len(self.seq1)
        j = len(self.seq2)
        # dim that has highest value at [i, j]
        k = np.argmax([matrix[i, j, 0], matrix[i, j, 1], matrix[i, j, 2]])
        # store max that value for solution
        max_score = int(matrix[i, j, k])

        aligned_seq1 = []
        aligned_seq2 = []

        while i > 0 or j > 0:
            # if diag dim, no add from both sequeces and find new k with same method
            if k == 0:
                aligned_seq1.append(self.seq1[i - 1])
                aligned_seq2.append(self.seq2[j - 1])
    
                k = np.argmax(
                    [
                        matrix[i - 1, j - 1, 0],
                        matrix[i - 1, j - 1, 1],
                        matrix[i - 1, j - 1, 2],
                    ]
                )
                i -= 1
                j -= 1
            # if up dim, gap in seq2 and backcalculate matrix scoring to determine k
            elif k == 1:
                aligned_seq1.append(self.seq1[i - 1])
                aligned_seq2.append("-")

                if matrix[i, j, 1] == matrix[i - 1, j, 0] - self.opening_penalty:
                    k = 0
                elif matrix[i, j, 1] == matrix[i - 1, j, 1] - self.extension_penalty:
                    k = 1
                i -= 1

            # if left dim, gap in seq1 and backcalculate matrix scoring to determine k
            else:
                aligned_seq1.append("-")
                aligned_seq2.append(self.seq2[j - 1])

                if matrix[i, j, 2] == matrix[i, j - 1, 0] - self.opening_penalty:
                    k = 0
                elif matrix[i, j, 2] == matrix[i, j - 1, 2] - self.extension_penalty:
                    k = 2
                j -= 1
        # aligned sequences built in reverse so reverse back and join to string
        return max_score, "".join(aligned_seq1[::-1]), "".join(aligned_seq2[::-1])


def read_fasta(fp):
    seqs = []
    header = None
    parts = []
    for line in fp:
        line = line.rstrip()
        if not line:
            continue
        if line.startswith(">"):
            if header is not None:
                seqs.append((header, "".join(parts)))
            header = line[1:]
            parts = []
        else:
            parts.append(line)
    if header is not None:
        seqs.append((header, "".join(parts)))
    return seqs


def main():
    fasta = read_fasta(sys.stdin)
    seq1 = fasta[0][1]
    seq2 = fasta[1][1]

    aliger = GlobalAlign(seq1, seq2)
    max_score, aligned_seq1, aligned_seq2 = aliger.align()
    print(max_score)
    print(aligned_seq1)
    print(aligned_seq2)


if __name__ == "__main__":
    main()
