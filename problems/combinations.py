from tkinter.filedialog import askopenfilename
from itertools import product


def seqCombinations(seq, r):
    return product(seq, repeat=r)


if __name__ == "__main__":
    for seq in seqCombinations("ABCDEFGHI", 3):
        print("".join(seq))
