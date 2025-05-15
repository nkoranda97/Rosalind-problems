import numpy as np
from Bio.Align import substitution_matrices
import sys


class GlobalAlignment:
    def __init__(self, seq1: str, seq2: str):
        self.BLOSUM62 = substitution_matrices.load("BLOSUM62")
        self.CONSTANT_GAP_PENALTY = 5
        self.seq1 = seq1
        self.seq2 = seq2

    def score_matrix(self) -> int:
        diag_matrix = np.full(
            (len(self.seq1) + 1, len(self.seq2) + 1), -np.inf, dtype=np.float32
        )
        vert_matrix = np.full_like(diag_matrix, -np.inf)
        hor_matrix = np.full_like(diag_matrix, -np.inf)

        diag_matrix[0, 0] = 0

        for i in range(1, len(self.seq1) + 1):
            vert_matrix[i, 0] = -self.CONSTANT_GAP_PENALTY
        for j in range(1, len(self.seq2) + 1):
            hor_matrix[0, j] = -self.CONSTANT_GAP_PENALTY

        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                diag_matrix[i, j] = (
                    max(
                        diag_matrix[i - 1, j - 1],
                        vert_matrix[i - 1, j - 1],
                        hor_matrix[i - 1, j - 1],
                    )
                    + self.BLOSUM62[self.seq1[i - 1], self.seq2[j - 1]]
                )
                vert_matrix[i, j] = max(
                    diag_matrix[i - 1, j] - self.CONSTANT_GAP_PENALTY,
                    vert_matrix[i - 1, j],
                )
                hor_matrix[i, j] = max(
                    diag_matrix[i, j - 1] - self.CONSTANT_GAP_PENALTY,
                    hor_matrix[i, j - 1],
                )

        return int(max(diag_matrix[-1, -1], vert_matrix[-1, -1], hor_matrix[-1, -1]))


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

    aligner = GlobalAlignment(seq1, seq2)
    print(aligner.score_matrix())


if __name__ == "__main__":
    main()
