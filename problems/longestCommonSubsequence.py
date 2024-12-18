from tkinter.filedialog import askopenfilename
from Bio import SeqIO

def findLongestCommonSubsequence(sequence1, sequence2):
    #create the matrix
    m, n = len(sequence1), len(sequence2)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    #reconstruct the sequence            
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if sequence1[i - 1] == sequence2[j - 1]:
            lcs.append(sequence1[i - 1])
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs)).replace('E', '')

def readFasta():
    with open(askopenfilename(), 'r') as f:
        records = [str(record.seq) for record in SeqIO.parse(f, 'fasta')]
        return records[0], records[1]

if __name__ == '__main__':   
    s1, s2 = readFasta()
    print(findLongestCommonSubsequence(s1, s2))
