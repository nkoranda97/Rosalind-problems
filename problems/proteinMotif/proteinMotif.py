from requests import get
from Bio import SeqIO
from io import StringIO
from tkinter.filedialog import askopenfilename
import re


def getFasta(uniprotID):
    """Fetches the FASTA sequence for a given UniProt ID."""
    response = get("http://www.uniprot.org/uniprot/" + uniprotID + ".fasta")
    if response.status_code != 200:
        print(f"Error fetching data for {uniprotID}: {response.status_code}")
        return None
    return SeqIO.read(StringIO(response.text), "fasta")


def findGlycanMotifs(seq):
    """Finds glycan motifs in the given sequence."""
    seq = str(seq.seq)
    pattern = re.compile(r"(?=N[^P][ST][^P])")
    matches = [str(m.start() + 1) for m in pattern.finditer(seq)]
    return matches if matches else False


if __name__ == "__main__":
    # Read UniProt IDs from a file, find glycan motifs in their sequences,
    # and write the results to another file.
    with open(askopenfilename(), "r") as f:
        with open("proteinMotif/results.txt", "w") as r:
            for seqID in f.readlines():
                seqID = seqID.strip()
                seqRecord = getFasta(seqID.split("_", 1)[0])
                if seqRecord is not None:
                    results = findGlycanMotifs(seqRecord)
                    if results:
                        r.write(seqID + "\n")
                        r.write(" ".join(results) + "\n")
