from functools import reduce
from tkinter.filedialog import askopenfilename

def sharedMotif(seqList):
    seqList.sort(key=len)
    seqList = [i[0] for i in seqList]
    s1 = seqList[0]
    left = 0
    longestSub = ''
    for right in range(1,len(s1)):
        if all(s1[left:right] in seqs for seqs in seqList):
            if len(s1[left:right])>len(longestSub):
                longestSub = s1[left:right]

        else:
            while left < right-1:
                left += 1
                if all(s1[left:right] in seqs for seqs in seqList):
                    if len(s1[left:right])>len(longestSub):
                        longestSub = s1[left:right]
                    break 

    return longestSub
        
def longest_common_substring(strs):
    if not strs:
        return ""
    # The function to find the longest common substring
    def lcs(s1, s2):
        m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
        longest, x_longest = 0, 0
        for x in range(1, 1 + len(s1)):
            for y in range(1, 1 + len(s2)):
                if s1[x - 1] == s2[y - 1]:
                    m[x][y] = m[x - 1][y - 1] + 1
                    if m[x][y] > longest:
                        longest = m[x][y]
                        x_longest = x
                else:
                    m[x][y] = 0
        return s1[x_longest - longest: x_longest]

    # Apply the function to all strings
    return reduce(lcs, strs)
#binary search technique  
def sharedMotif2(seqList):
    # Sort the sequences by length and extract the sequences from the tuples
    seqList.sort(key=len)
    seqList = [i[0] for i in seqList]

    # Define a function to check if a substring of a certain length is common to all sequences
    def check_substring_length(length):
        # Create a set to store the substrings of the first sequence
        substrings = set(seqList[0][i:i+length] for i in range(len(seqList[0]) - length + 1))

        # Check if each substring is in all the other sequences
        for seq in seqList[1:]:
            new_substrings = set(seq[i:i+length] for i in range(len(seq) - length + 1))
            substrings &= new_substrings

            # If there are no common substrings, return False
            if not substrings:
                return False

        # If there are common substrings, return one of them
        return substrings.pop()

    # Use binary search to find the longest common substring
    low, high = 0, len(seqList[0])
    while low <= high:
        mid = (low + high) // 2
        if check_substring_length(mid):
            low = mid + 1
        else:
            high = mid - 1

    # Return the longest common substring
    return check_substring_length(high)




