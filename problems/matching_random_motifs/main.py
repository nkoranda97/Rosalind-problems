from collections import Counter
from functools import reduce
from operator import mul


def probablity_identical(num_strings:int, gc_content:float, sequence:str) -> float:
    """calculates the probability of at least 1 in num_strings have a sequence identical to sequence given the gc_concent

    Args:
        num_strings (int): number of strings
        gc_content (float): gc_conent of strings
        sequence (str): sequence we need to match to

    Returns:
        float: probability of 1 in num_strings being identical to sequencwe
    """
    
    probabilities = {
        'A': (1-gc_content)/2,
        'T': (1-gc_content)/2,
        'C': gc_content/2,
        'G': gc_content/2
    }
    
    # 1-P(A^C)^N
    liklihood = 1 - (1 -reduce(mul, [probabilities.get(base) ** count for base, count in Counter(sequence).items()])) ** num_strings
    return round(liklihood, 3)
            


if __name__ == "__main__":
    a = probablity_identical(93611, 0.596664, 'CTCCAAAC')
    print(a)