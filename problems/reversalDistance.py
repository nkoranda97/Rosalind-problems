from typing import List
from collections import deque


def reversal(gene: List[str], start: int, end: int) -> List[str]:
    """Does a reversal of a gene (permutation)


    Args:
        gene (List[str]): permutation
        start (int): index to start reversal
        end (int): inted to end reversal

    Returns:
        List[str]: reversed gene (permutation)
    """

    while start < end - 1:
        gene[start], gene[end - 1] = gene[end - 1], gene[start]
        start += 1
        end -= 1
    return gene


def find_reversal_distance(gene1: List[str], gene2: List[str]) -> int:
    """finds the reversal distance between two genes (permutations)

    Args:
        gene1 (List[str]): gene (permutation)
        gene2 (List[str]): gene (permutation)

    Returns:
        int: reversal distance
    """

    if gene1 == gene2:
        return 0

    queue = deque([(gene1, 0)])
    visited = set()
    visited.add(tuple(gene1))

    while queue:
        current_gene, distance = queue.popleft()

        for i in range(len(current_gene)):
            for j in range(i + 2, len(current_gene) + 1):
                new_gene = current_gene[:]
                reversal(new_gene, i, j)
                new_gene_tuple = tuple(new_gene)

                if new_gene_tuple == tuple(gene2):
                    return distance + 1

                if new_gene_tuple not in visited:
                    visited.add(new_gene_tuple)
                    queue.append((new_gene, distance + 1))

    return -1


if __name__ == "__main__":
    test_cases = [
        (
            ["5", "9", "8", "6", "2", "4", "3", "10", "7", "1"],
            ["1", "7", "3", "9", "4", "6", "8", "2", "5", "10"],
        ),
        (
            ["1", "9", "10", "4", "8", "2", "3", "5", "7", "6"],
            ["8", "6", "1", "7", "4", "10", "3", "2", "9", "5"],
        ),
        (
            ["5", "2", "8", "6", "10", "1", "7", "9", "3", "4"],
            ["8", "5", "10", "2", "7", "6", "3", "1", "4", "9"],
        ),
        (
            ["3", "5", "1", "7", "2", "8", "10", "4", "6", "9"],
            ["7", "6", "9", "4", "2", "8", "3", "5", "10", "1"],
        ),
        (
            ["3", "9", "4", "7", "1", "6", "8", "5", "10", "2"],
            ["2", "4", "5", "9", "10", "1", "6", "3", "8", "7"],
        ),
    ]

    for gene1, gene2 in test_cases:
        print(find_reversal_distance(gene1, gene2))
