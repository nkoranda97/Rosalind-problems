from tkinter.filedialog import askopenfilename
from Bio import SeqIO

def locateRestriction(seq):
    pairs = {'A':'T','T':'A', 'C':'G','G':'C'}
    for nuc, base in enumerate(seq[:-1]):
        if base == pairs.get(seq[nuc+1]):
            left = nuc
            right = nuc+1
            try:
                while seq[left] == pairs.get(seq[right]):
                    left -= 1
                    right += 1
                    if right-left > 3:
                        yield (left+2, right-left-1)
            except IndexError:
                if right-left > 3:
                    yield (left+2, right-left-1)

def readFasta():
    with open(askopenfilename(),'r') as f:
        #uses Bio SeqIO to easily read in fasta file sequences
        record = SeqIO.read(f,'fasta')
        return record.seq
    
if __name__ == "__main__":
    for position, length in sorted(locateRestriction(readFasta()), key=lambda x: x[0]):
        print(position, length)