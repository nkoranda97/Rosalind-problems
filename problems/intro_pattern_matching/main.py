from typing import List, Tuple

class Trie:
    def __init__(self, node):
        self.node: Tuple[str, int] = node
        self.children: List[Tuple[str, int]] = []
        
    def print_nodes(self, file: str, parent: int = None):
        if parent:
            file.write(f'{parent} {self.node[1]} {self.node[0]}\n')
        
        for child in self.children:
            child.print_nodes(file, self.node[1])
        
def make_trie(sequences: List[str]) -> Trie:
    trie: Trie = Trie(('root', 1))
    # keep track of node numbers for solution
    i: int = 2
    
    for sequence in sequences:
        current_trie: Trie = trie
        for char in sequence:
            found_in_child: bool = False
            # looks for char in children
            for child in current_trie.children:
                if child.node[0] == char:
                    current_trie = child
                    found_in_child = True
                    break
            # if char not in children, adds it and makes it the current_trie
            if not found_in_child:
                new_trie = Trie((char, i))
                i += 1
                current_trie.children.append(new_trie)
                current_trie = new_trie
    
    return trie

def read_file(file_path: str) -> List[str]:
    sequences: List[str] = []
    with open(file_path, 'r') as f:
        for line in f:
            sequences.append(line.strip())
            
    return sequences

def main() -> None:
    file_path: str = 'problems/intro_pattern_matching/rosalind_trie.txt'
    output_file_path: str = 'problems/intro_pattern_matching/trie_output.txt'

    sequences: List[str] = read_file(file_path)
    
    trie: Trie = make_trie(sequences)
    
    with open(output_file_path, 'w') as file:
        trie.print_nodes(file)
    
if __name__ == "__main__":
    main()
                
    
        