from Bio import SeqIO
from tkinter.filedialog import askopenfilename

def findSubsequence(s,t):
    index = []
    tIndex = 0
    for i,char in enumerate(s):
        if char == t[tIndex]:
            index.append(i)
            tIndex+=1    
        if len(index) == len(t):
              return ' '.join([str(i+1) for i in index])

def readFasta():
    with open(askopenfilename(),'r') as f:
        records =  [str(record.seq) for record in SeqIO.parse(f,'fasta')]
        s = records[0]; t = records[1]
        return s,t
    

if __name__ == '__main__':
    s,t = readFasta()
    print(findSubsequence(s,t))
                