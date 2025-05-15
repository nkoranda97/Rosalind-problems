from Bio import SeqIO
from tkinter.filedialog import askopenfilename


def findRatio(s1, s2):
    convertKey = {"A": 0, "C": 1, "G": 0, "T": 1}
    transitions = 0
    transversions = 0
    for nuc1, nuc2 in zip(s1, s2):
        if nuc1 != nuc2:
            if convertKey[nuc1] == convertKey[nuc2]:
                transitions += 1
            else:
                transversions += 1
    return transitions / transversions


def readFasta():
    with open(askopenfilename(), "r") as f:
        records = [str(record.seq) for record in SeqIO.parse(f, "fasta")]
        return records[0], records[1]


if __name__ == "__main__":
    s1, s2 = readFasta()
    print(findRatio(s1, s2))
