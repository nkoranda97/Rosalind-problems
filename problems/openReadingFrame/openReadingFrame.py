from tkinter.filedialog import askopenfilename
from Bio import SeqIO

codons = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S', 'CCT': 'P', 'CCC': 'P',
    'CCA': 'P', 'CCG': 'P', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A',
    'GCA': 'A', 'GCG': 'A', 'TAT': 'Y', 'TAC': 'Y', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
    'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'TAA': '*', 'TAG': '*', 'TGA': '*'
}

def openReadingFrames(seq):
    proList = []
    for frame in range(3):
        length = 3 * ((len(record) - frame) // 3)
        seq_frame = seq[frame:frame+length]
        for nuc in range(0,len(seq_frame),3):
            current_pro = ''
            codon = codons[seq_frame[nuc:nuc+3]]
            if codon == 'M':
                current_nuc = nuc
                while codon != '*':
                    current_pro += codon
                    current_nuc += 3
                    try:
                        codon = codons[seq_frame[current_nuc:current_nuc+3]]
                    except KeyError:
                        current_pro = ''
                        break
                if len(current_pro) > 0:
                    proList.append(current_pro)
    return proList
                    
if __name__ == "__main__":
    with open(askopenfilename(),'r') as f:
        record = SeqIO.read(f,'fasta')
        orf = set(openReadingFrames(str(record.seq)) + (openReadingFrames(str(record.seq.reverse_complement()))))
        for frame in orf:
            print(frame)
        