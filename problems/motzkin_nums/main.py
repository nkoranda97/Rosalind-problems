def count_non_crossing_matches(seq: str) -> int:
    
    memo = {}
    
    valid_pairs = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    
    def recurse(start: int, end: int) -> int:
        if (start, end) in memo:
            return memo[(start, end)]
        
        if start >= end:
            return 1
        
        count = recurse(start + 1, end)
        for i in range(start + 1, end + 1):
            if seq[start] == valid_pairs.get(seq[i], ''):
                count += recurse(start + 1, i - 1) * recurse(i + 1, end)
                count %= 1000000
        
        memo[(start, end)] = count
        return count
    
    return recurse(0, len(seq) - 1)

def main() -> None:
    seq: str = '''UCUUAGCGUGCGCGCUUGUGACGUACUUCGCUCUCGGACCACAUUGAUCAUGCCACGCCG
CCCCUCAGUCCGUCAGGACGUGAUCAGCUAUGGUGGCCUGUCUUAACAGGUCAUGGAGUU
ACUGCGUAGGACCACCCCGCCGCGUAUUUAUACUUCGGCACCGAUCGACGCGGAGAGGAA
GACCCUACUUGGACAGAACGUCGGAACCUGUAUACCCAGUGUGGUGUAUCAGUAUUACUG
AGGUGGUUCUUGUGGCUUACGCGGAAGACGUGUAUUGUCCAAAAAGAAAUUGAGAC'''
    answer: int = count_non_crossing_matches(seq)
    print(answer)
    
if __name__ == "__main__":
    main()