import math
from itertools import permutations

# Define a function to generate a list of permutations and its length
def permutationList(n):
    # Return the factorial of n (the number of permutations) and the permutations themselves
    return math.factorial(n), permutations(range(1, n+1))

if __name__ == "__main__":
    # Open the results file in write mode
    with open('permutations/results.txt', 'w') as r:
        # Get the number of permutations and the permutations themselves
        num, permList = permutationList(7)
        # Write the number of permutations to the file
        r.write(f'{num}\n')
        # Write each permutation to the file, one per line
        # The ' '.join(map(str, numList)) part converts each permutation to a space-separated string
        # The for numList in permList part generates these strings for all permutations
        # The writelines method writes all these strings to the file, adding a newline after each one
        r.writelines(' '.join(map(str, numList)) + '\n' for numList in permList)