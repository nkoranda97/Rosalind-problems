from functools import reduce
import operator

amino_acid_to_num_codons = {
    "F": 2,
    "L": 6,
    "I": 3,
    "M": 1,
    "V": 4,
    "S": 6,
    "P": 4,
    "T": 4,
    "A": 4,
    "Y": 2,
    "H": 2,
    "Q": 2,
    "N": 2,
    "K": 2,
    "D": 2,
    "E": 2,
    "C": 2,
    "W": 1,
    "R": 6,
    "G": 4,
    "*": 3,
}


def numPotentialSeq(ProSeq):
    return (
        reduce(operator.mul, (amino_acid_to_num_codons[aa] for aa in ProSeq + "*"), 1)
        % 1000000
    )


if __name__ == "__main__":
    print(numPotentialSeq())
