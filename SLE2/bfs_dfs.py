# A-Z Graph

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],

    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],

    'H': ['P', 'Q'],
    'I': ['R', 'S'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],
    'L': ['X', 'Y'],
    'M': ['Z'],

    'N': [],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': []
}


# ---------------- BFS ----------------

def bfs(graph, start, goal):

    queue = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while queue:

        current, path = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbour in graph[current]:

            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# ---------------- DFS ----------------

def dfs(graph, start, goal):

    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:

        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        # reversed so that left-to-right order is followed
        for neighbour in reversed(graph[current]):

            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# ---------------- Run BFS ----------------

bfs_path, bfs_nodes = bfs(graph, 'A', 'Z')

print("BFS")
print("Path:", " -> ".join(bfs_path))
print("Nodes Expanded:", bfs_nodes)


# ---------------- Run DFS ----------------

dfs_path, dfs_nodes = dfs(graph, 'A', 'Z')

print("\nDFS")
print("Path:", " -> ".join(dfs_path))
print("Nodes Expanded:", dfs_nodes)
