# BFS vs DFS Py-Spy Profiling Code

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
    'N': [], 'O': [],
    'P': [], 'Q': [],
    'R': [], 'S': [],
    'T': [], 'U': [],
    'V': [], 'W': [],
    'X': [], 'Y': [],
    'Z': []
}


def bfs(graph, start, goal):

    queue = [(start, [start])]
    visited = set()

    while queue:

        current, path = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbour in graph[current]:

            if neighbour not in visited:
                queue.append(
                    (neighbour, path + [neighbour])
                )

    return None


def dfs(graph, start, goal):

    stack = [(start, [start])]
    visited = set()

    while stack:

        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbour in reversed(graph[current]):

            if neighbour not in visited:
                stack.append(
                    (neighbour, path + [neighbour])
                )

    return None


# Repeat the search many times
for i in range(500000):

    bfs(graph, 'A', 'Z')
    dfs(graph, 'A', 'Z')


print("Profiling completed.")
