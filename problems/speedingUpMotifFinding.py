from tkinter.filedialog import askopenfilename
from Bio import SeqIO


def findFailureArray(sequence):
    n = len(sequence)
    failureArray = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and sequence[i] != sequence[j]:
            j = failureArray[j - 1]
        if sequence[i] == sequence[j]:
            j += 1
        failureArray[i] = j

    return " ".join(map(str, failureArray))


def openFasta():
    file = askopenfilename()
    with open(file, "r") as f:
        return SeqIO.read(f, "fasta").seq


if __name__ == "__main__":
    sequence = openFasta()
    with open("/users/name/Desktop/output.txt", "w") as f:
        f.write(findFailureArray(sequence))
