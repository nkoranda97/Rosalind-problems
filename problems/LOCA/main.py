import numpy as np
from Bio.Align import substitution_matrices
import sys


class LocalAlignment:
    def __init__(self, seq1: str, seq2: str):
        self.scoring_matrix = substitution_matrices.load("PAM250")
        self.linear_gap_penalty = 5
        self.seq1 = seq1
        self.seq2 = seq2

    def score_matrix(self) -> tuple[np.ndarray[np.int32], tuple[int, int]]:
        max_pos = 0, 0
        len1, len2 = len(self.seq1), len(self.seq2)
        matrix = np.zeros((len1 + 1, len2 + 1), dtype=np.int32)

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                diag = (
                    matrix[i - 1, j - 1]
                    + self.scoring_matrix[self.seq1[i - 1], self.seq2[j - 1]]
                )
                up = matrix[i - 1, j] - self.linear_gap_penalty
                left = matrix[i, j - 1] - self.linear_gap_penalty
                matrix[i, j] = max(diag, up, left, 0)
                if matrix[i, j] > matrix[max_pos]:
                    max_pos = i, j

        return matrix, max_pos

    def make_local_alignment(self) -> list[str, str, int]:
        matrix, current = self.score_matrix()
        i, j = current
        max_score = matrix[i, j]
        align1 = ""
        align2 = ""

        while matrix[i, j] != 0:
            score = matrix[i, j]
            diag = (
                matrix[i - 1, j - 1]
                + self.scoring_matrix[self.seq1[i - 1], self.seq2[j - 1]]
            )
            up = matrix[i - 1, j] - self.linear_gap_penalty
            # this traceback solution biases diag then up then left traceback
            if score == diag:
                align1 += self.seq1[i - 1]
                align2 += self.seq2[j - 1]
                i -= 1
                j -= 1
            elif score == up:
                align1 += self.seq1[i - 1]
                i -= 1
            else:
                align2 += self.seq2[j - 1]
                j -= 1
        # strings are built backwards so we return backwards
        return align1[::-1], align2[::-1], int(max_score)


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

    aligner = LocalAlignment(seq1, seq2)
    align1, align2, score = aligner.make_local_alignment()
    print(f"{score}\n{align1}\n{align2}")


if __name__ == "__main__":
    main()
