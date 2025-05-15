from math import factorial


def countMatches(seq):
    return factorial(seq.count("A")) * factorial(seq.count("C"))


if __name__ == "__main__":
    seq = "UUGUAAGAUAACUCUCGGUUAACCCUCAUAUCCUGUAAGUCCCCUCAAUGAGAACUGGAGUGGGAGGGUCCA"
    print(countMatches(seq))
