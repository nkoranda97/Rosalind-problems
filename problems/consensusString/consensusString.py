import numpy as np
from tkinter.filedialog import askopenfilename
from Bio import SeqIO
import pandas as pd


def makeMatrix(seqList):
    # turn seqs to list of list of nucleotides
    nucList = []
    for seq in seqList:
        nucList.append([nuc for nuc in seq])
    # turn list of list of nucs into np array, makes for easy transposing
    seqArray = np.array(nucList)
    # make df to store counts at each position
    profileMatrix = pd.DataFrame(columns=["A", "C", "G", "T"])
    # iterate through each position
    for i, position in enumerate(seqArray.T):
        # makes string of nucleotides at a given position
        seqT = "".join(position)
        # counts bases at a given position, adds counts to df
        counts = {}
        for nuc in profileMatrix.columns:
            counts[nuc] = seqT.count(nuc)
        profileMatrix.loc[i] = counts
    # makes consensus string
    consensusString = (
        profileMatrix.T.idxmax().to_string(header=False, index=False).replace("\n", "")
    )
    # formats profile matrix
    profileMatrix.rename(
        columns={"A": "A:", "C": "C:", "G": "G:", "T": "T:"}, inplace=True
    )

    return consensusString, profileMatrix.T.to_string(header=False)


if __name__ == "__main__":
    filename = askopenfilename()
    with open(filename, "r") as f:
        # uses Bio SeqIO to easily read in fasta file sequences
        seqList = [str(record.seq) for record in SeqIO.parse(f, "fasta")]
    s, profileMatrix = makeMatrix(seqList)
    with open("results.txt", "w") as f:
        f.write(s)
        f.write("\n")
        f.write(profileMatrix)
