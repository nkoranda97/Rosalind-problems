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
    
    return ''.join(reversed(lcs)) 
    

def find_shortest_common_supersequence(str1: str, str2: str) -> str:
    subsequence: str = findLongestCommonSubsequence(str1, str2)
    supersequence: str = ''
    i: int = 0
    j: int = 0
    k: int = 0
    while i < len(str1) or j < len(str1):
        if str1[i] == subsequence[k] and str2[j] == subsequence[k]:
            supersequence += subsequence[k]
            i += 1
            j += 1
            k += 1
        elif str1[i] == subsequence[k] and str2[j] != subsequence[k]:
            supersequence += str2[j]
            j += 1
        elif str1[i] != subsequence[k] and str2[j] == subsequence[k]:
            supersequence += str1[i]
            i += 1
        else:
            supersequence += str1[i]
            supersequence += str2[j]
            i += 1
            j += 1
        
        if k == len(subsequence):
            break
            
    while i < len(str1):
        supersequence += str1[i]
        i += 1
        
    while j < len(str2):
        supersequence += str2[j]
        j += 1
        
    return supersequence


        
        
def main() -> None:
    str1: str = 'CTGTCTGGAGCGGTCGATAACCGCATGTGACCCTCTAAGGGCACTTTTGTTACCCGCCTACATAACGTGTGGGACGGACACCATTCT'
    str2: str = 'CGACATCGCCACATTCGCATCTTATCTATTCAGCTTGGCCAGACTAACTTCCTTGGTATACTTTCTGGAGCATGCATATTC'
    supersequence: str = find_shortest_common_supersequence(str1, str2)
    print(supersequence)
    
if __name__ == "__main__":
    main()