from typing import List


def infer_protein(array: List[float]) -> str:
    # rounding to nearest one hundreth and ignoring leucine. Any isoleucine could be a leucine
    mass_table = {
        71.04: "A",
        103.01: "C",
        115.03: "D",
        129.04: "E",
        147.07: "F",
        57.02: "G",
        137.06: "H",
        113.08: "I",
        128.09: "K",
        131.04: "M",
        114.04: "N",
        97.05: "P",
        128.06: "Q",
        156.10: "R",
        87.03: "S",
        101.05: "T",
        99.07: "V",
        186.08: "W",
        163.06: "Y",
    }

    array = [round(array[i] - array[i - 1], 2) for i in range(1, len(array))]
    return "".join(mass_table.get(mass, "") for mass in array)


def read_file(file_path: str) -> List[float]:
    array: List[float] = list()
    with open(file_path) as f:
        for line in f.readlines():
            array.append(float(line.strip()))

    return array


def main() -> None:
    array: List[float] = read_file(
        "problems/inferring_protein_from_spectrum/rosalind_spec.txt"
    )
    sequence: str = infer_protein(array)
    print(sequence)


if __name__ == "__main__":
    main()
