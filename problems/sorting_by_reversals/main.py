from typing import List, Tuple, Dict
from collections import deque

def reversal(gene: List[str], start: int, end: int) -> List[str]:
    while start < end-1:
        gene[start], gene[end-1] = gene[end-1], gene[start]
        start += 1
        end -= 1
    return gene

def find_reversal_distance(gene1: List[str], gene2: List[str]) -> Tuple[int, List[Tuple[int, int]]]:
    if gene1 == gene2:
        return 0, []
    
    queue = deque([(gene1, 0, None, None)]) 
    visited = set()
    visited.add(tuple(gene1))
    #map to track reversals
    parent_map: Dict[Tuple[str], Tuple[Tuple[str], Tuple[int, int]]] = {} 
    
    while queue:
        current_gene, distance, parent_gene, reversal_indices = queue.popleft()
        
        if parent_gene is not None:
            parent_map[tuple(current_gene)] = (tuple(parent_gene), reversal_indices)
        
        for i in range(len(current_gene)):
            for j in range(i + 2, len(current_gene) + 1):
                new_gene = current_gene[:]
                reversal(new_gene, i, j)
                new_gene_tuple = tuple(new_gene)
                
                if new_gene_tuple == tuple(gene2):
                    parent_map[new_gene_tuple] = (tuple(current_gene), (i + 1, j))
                    return distance + 1, reconstruct_path(parent_map, gene1, gene2)
                
                if new_gene_tuple not in visited:
                    visited.add(new_gene_tuple)
                    queue.append((new_gene, distance + 1, current_gene, (i + 1, j)))
                    
    return -1, []

def reconstruct_path(parent_map: Dict[Tuple[str], Tuple[Tuple[str], Tuple[int, int]]], start_gene: List[str], end_gene: List[str]) -> List[Tuple[int, int]]:
    path = []
    current_gene = tuple(end_gene)
    
    while current_gene != tuple(start_gene):
        parent_gene, reversal_indices = parent_map[current_gene]
        path.append(reversal_indices)
        current_gene = parent_gene
    
    path.reverse()
    return path

def read_file(file_path: str) -> Tuple[List[int]]:
    with open (file_path) as f:
        array_1: List[int] = list(map(int, (f.readline().strip().split(' '))))
        array_2: List[int] = list(map(int, (f.readline().strip().split(' '))))
    
    return array_1, array_2

def main() -> None:
    file_path: str = 'problems/sorting_by_reversals/rosalind_sort.txt'
    array_1, array_2 = read_file(file_path)
    
    reversal_distance, reversal_path = find_reversal_distance(array_1, array_2)
    
    print(reversal_distance) 
    for start, end in reversal_path:
        print(start, end)

if __name__ == "__main__":
    main()