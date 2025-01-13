from typing import List, Tuple

def read_fasta(file_path: str) -> Tuple[str, str]:
    with open(file_path, 'r') as file:
        sequences: List = []
        sequence: str = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        sequences.append(sequence)
    return sequences[0], sequences[1]

def compute_edit_distance(str1: str, str2: str) -> List[List[int]]:
    #initialize matrix
    matrix: List[List[int]] = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    for i in range(len(str1) + 1):
        matrix[0][i] = i
    for i in range(1, len(str2) + 1):
        matrix[i][0] = i
    
    #score matrix
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i-1] == str1[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1] + 1, matrix[i][j-1] + 1, matrix[i-1][j] + 1)
    
    return matrix[-1][-1]

def main() -> None:
    file_path: str = 'edit_distance/rosalind_edit.txt'
    str1: str
    str2: str
    str1, str2 = read_fasta(file_path)
    
    edit_distance: int = compute_edit_distance(str1, str2)
    
    #final 
    print(edit_distance)

if __name__ == "__main__":
    main()