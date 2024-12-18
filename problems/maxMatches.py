from collections import Counter
from math import factorial

def find_max_matches(sequence):
    char_counts = Counter(sequence)
    auMax, auMin = max(char_counts['A'],char_counts['U']), min(char_counts['A'],char_counts['U'])
    gcMax, gcMin = max(char_counts['G'],char_counts['C']), min(char_counts['G'],char_counts['C'])
    
    return factorial(auMax)//factorial(auMax-auMin) * factorial(gcMax)//factorial(gcMax-gcMin)

if __name__ == '__main__':
    sequence = 'UAAGAUCGGACUUGUGAGUUCCUAGAUAGAGGCUCGCUAAGAGAAACUCCCCUCAGCCCCUUAUAAGGCCGUUCAUAAGGCGCUCACCGCU' 
    print(find_max_matches(sequence))