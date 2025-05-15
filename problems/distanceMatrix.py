from Bio import SeqIO
from tkinter.filedialog import askopenfilename
import itertools
import csv


def distanceMatrix(seqList):
    matrix = [[0] * len(seqList) for _ in seqList]
    for i, j in itertools.combinations(range(len(seqList)), 2):
        n = sum(1 for char1, char2 in zip(seqList[i], seqList[j]) if char1 != char2)
        matrix[i][j] = matrix[j][i] = n / len(seqList[i])
    return matrix


def readFasta():
    with open(askopenfilename(), "r") as f:
        return [str(record.seq) for record in SeqIO.parse(f, "fasta")]


if __name__ == "__main__":
    seqList = readFasta()
    matrix = distanceMatrix(seqList)
    output_file_path = "/Users/nick/Desktop/output.txt"
    with open(output_file_path, "w", newline="") as f:
        writer = csv.writer(f, delimiter=" ")
        writer.writerows([[f"{num:.5f}" for num in row] for row in matrix])
