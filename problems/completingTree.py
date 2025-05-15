def completeTree(num, edges):
    parent = list(
        range(num + 1)
    )  # Using one extra space to match the 1-based index of nodes

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY  # Union operation

    # Apply union-find to all edges
    for u, v in edges:
        union(u, v)
    # Count distinct sets/roots
    roots = set(find(x) for x in range(1, num + 1))
    return len(roots) - 1  # You need k-1 edges to connect k components


def readFile():
    from tkinter.filedialog import askopenfilename

    filename = askopenfilename()
    with open(filename) as f:
        num = int(f.readline().strip())
        edges = [list(map(int, line.strip().split())) for line in f]
        return num, edges


if __name__ == "__main__":
    num, edges = readFile()
    print(completeTree(num, edges))

    """+ num - len(set().union(*[set(node) for node in smallTrees]))
    """
