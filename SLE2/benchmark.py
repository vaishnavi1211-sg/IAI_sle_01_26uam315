import time

# Graph
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
                queue.append(
                    (neighbour, path + [neighbour])
                )

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

        for neighbour in reversed(graph[current]):

            if neighbour not in visited:
                stack.append(
                    (neighbour, path + [neighbour])
                )

    return None, nodes_expanded


# Number of runs
RUNS = 3


# Three cases
cases = {
    "BEST CASE": "B",
    "AVERAGE CASE": "M",
    "WORST CASE": "Z"
}


# ---------------- BENCHMARK ----------------

for case_name, goal in cases.items():

    print("\n")
    print("=" * 50)
    print(case_name)
    print("Start: A")
    print("Goal :", goal)
    print("=" * 50)

    # ---------- BFS ----------
    bfs_times = []

    for i in range(RUNS):

        start_time = time.perf_counter()

        bfs_path, bfs_nodes = bfs(
            graph, 'A', goal
        )

        end_time = time.perf_counter()

        elapsed = (end_time - start_time) * 1000

        bfs_times.append(elapsed)

    bfs_average = sum(bfs_times) / RUNS


    # ---------- DFS ----------
    dfs_times = []

    for i in range(RUNS):

        start_time = time.perf_counter()

        dfs_path, dfs_nodes = dfs(
            graph, 'A', goal
        )

        end_time = time.perf_counter()

        elapsed = (end_time - start_time) * 1000

        dfs_times.append(elapsed)

    dfs_average = sum(dfs_times) / RUNS


    # ---------- OUTPUT ----------

    print("\nBFS")
    print("-" * 30)

    print("Path:", " -> ".join(bfs_path))
    print("Nodes Expanded:", bfs_nodes)

    for i, t in enumerate(bfs_times, 1):
        print("Run", i, ":", t, "ms")

    print("Average Time:", bfs_average, "ms")


    print("\nDFS")
    print("-" * 30)

    print("Path:", " -> ".join(dfs_path))
    print("Nodes Expanded:", dfs_nodes)

    for i, t in enumerate(dfs_times, 1):
        print("Run", i, ":", t, "ms")

    print("Average Time:", dfs_average, "ms")
