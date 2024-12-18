from tkinter.filedialog import askopenfilename
from Bio import SeqIO
from itertools import combinations

def overlapGraph(seqList):
    graph= []
    for seq1,seq2 in combinations(seqList,2):
        if seq2[1].startswith(seq1[1][-3:]):
            graph.append(f'{seq1[0]} {seq2[0]}')
        if seq1[1].startswith(seq2[1][-3:]):
            graph.append(f'{seq2[0]} {seq1[0]}')
    return graph

if __name__ == "__main__":
    filename = askopenfilename()
    with open(filename,'r') as f:
        #uses Bio SeqIO to easily read in fasta file sequences
        seqList = [(record.id,str(record.seq))for record in SeqIO.parse(f,'fasta')]
        graph = overlapGraph(seqList)
        with open('OverlapGraphs/result.text','w') as n:
            for line in graph:
                n.write(line + '\n')