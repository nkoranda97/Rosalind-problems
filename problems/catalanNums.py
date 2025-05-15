from tkinter.filedialog import askopenfilename
from Bio import SeqIO


def count_noncrossing_matchings(rna):
    # Memoization to store intermediate results
    memo = {}
    # Define valid pairs
    valid_pairs = {"A": "U", "U": "A", "C": "G", "G": "C"}

    def recurse(start, end):
        if (start, end) in memo:
            return memo[(start, end)]
        if start >= end:
            return 1

        count = 0
        for i in range(start + 1, end + 1, 2):
            print(i)
            if rna[start] == valid_pairs.get(rna[i], ""):
                count += recurse(start + 1, i - 1) * recurse(i + 1, end)
                count %= 1000000

        memo[(start, end)] = count
        return count

    return recurse(0, len(rna) - 1)


def readFasta():
    with open(askopenfilename(), "r") as f:
        record = SeqIO.read(f, "fasta")
        return record.seq


if __name__ == "__main__":
    sequence = "AUAU"
    print(count_noncrossing_matchings(sequence))
