from tkinter.filedialog import askopenfilename
from Bio import SeqIO


def findMerge(s1,ss):
    middle = len(s1)//2
    start = len(s1)
    while start>middle:
        if ss.endswith(s1[:start]):
            return ss + s1[start:], True
        start -=1
    end = 0
    while end < middle:
        if ss.startswith(s1[end:]):
            return s1[:end] + ss, True
        end += 1
    else:
        return ss, False 


def buildSuperString(seqList):
    ss = seqList.pop(0)
    while len(seqList) > 0:
        for s1 in seqList.copy():
            ss, progress = findMerge(s1,ss)
            if progress:
                seqList.remove(s1)
                break           
    return ss
    
def readFasta():
    with open(askopenfilename(),'r') as f:
        records = [str(record.seq) for record in SeqIO.parse(f,'fasta')]
        return records
    
if __name__ == '__main__':
    seqList = readFasta()
    print(buildSuperString(seqList))
                
            