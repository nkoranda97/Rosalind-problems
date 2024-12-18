from itertools import permutations, product

def signedPermutations(num):
    numbers = range(1, num+1)
    signed_numbers = list(product(*[[-i, i] for i in numbers]))
    signed_permutations = [' '.join(map(str, p)) for number in signed_numbers for p in permutations(number)]
    with open('output.txt','w') as f:
        f.write(f'{len(signed_permutations)}\n')
        for p in signed_permutations:
            f.write(p + '\n')

if __name__ == '__main__':
    signedPermutations(5)