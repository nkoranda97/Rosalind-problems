import numpy as np
from tkinter.filedialog import askopenfilename
from Bio import SeqIO

def patternToNumber(pattern):
    nucKey = {'A':0,'C':1,'G':2,'T':3}
    return sum(nucKey.get(pattern[len(pattern)-base-1]) * 4**base for base in range(len(pattern[::-1])))

def findKmerComp(sequence):
    kmerComp = np.zeros(256, dtype=int)
    for i in range(len(sequence) - 3):
        kmer = sequence[i:i+4]
        kmerComp[patternToNumber(kmer)] += 1
    return np.array2string(kmerComp, separator=' ').replace('[','').replace(']','')

def openFasta():
    file = askopenfilename()
    with open(file,'r') as f:
        return SeqIO.read(f,'fasta').seq
        

if __name__ == '__main__':
    sequence = openFasta()
    print(findKmerComp(sequence))