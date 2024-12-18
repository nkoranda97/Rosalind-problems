from Bio import SeqIO
from tkinter.filedialog import askopenfilename
from collections import Counter

def hammingDistance(seq1, seq2):
    return sum(1 for nuc1, nuc2 in zip(seq1, seq2) if nuc1 != nuc2) == 1


def reverseTranscription(seqList):
    return [seq.translate(str.maketrans('ATCG', 'TAGC'))[::-1] for seq in seqList]


def errorCorrection(seqList):
    fullList = seqList + reverseTranscription(seqList)
    sequenceCount = Counter(fullList)
    correctSequences = {seq for seq, count in sequenceCount.items() if count > 1}
    incorrectSequences = [seq for seq in seqList if seq not in correctSequences]
    mutations = []

    for seq1 in incorrectSequences:
        for seq2 in correctSequences:
            if hammingDistance(seq1, seq2):
                mutations.append(f'{seq1}->{seq2}')
                break
                
    return mutations


def readFasta():
    with open(askopenfilename(), 'r') as f:
        return [str(record.seq) for record in SeqIO.parse(f, 'fasta')]


if __name__ == '__main__':
    for mutation in errorCorrection(readFasta()):
        print(mutation)
