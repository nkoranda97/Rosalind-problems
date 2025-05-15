from Bio import SeqIO
from tkinter.filedialog import askopenfilename

codons = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "AGT": "S",
    "AGC": "S",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TAT": "Y",
    "TAC": "Y",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TGT": "C",
    "TGC": "C",
    "TGG": "W",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGA": "R",
    "AGG": "R",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "TAA": "*",
    "TAG": "*",
    "TGA": "*",
}


def splice_rna(s, ssList):
    for ss in ssList:
        s = s.replace(ss, "")
    pro = ""
    for codon in range(0, 3 * len(s) // 3, 3):
        if codons.get(s[codon : codon + 3]) == "*":
            break
        pro += codons.get(s[codon : codon + 3])
    return pro


def readFasta():
    with open(askopenfilename(), "r") as f:
        # uses Bio SeqIO to easily read in fasta file sequences
        records = [str(record.seq) for record in SeqIO.parse(f, "fasta")]
        return records[0], records[1:]


if __name__ == "__main__":
    s, ss = readFasta()
    print(splice_rna(s, ss))
