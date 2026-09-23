# SLE-2: Empirical Performance Analysis
# Course: 02AML204 - Introduction to Artificial Intelligence
# Comparison: BFS vs DFS

from collections import deque
import timeit


# Grid size
SIZE = 30

START = (0, 0)
GOAL = (SIZE - 1, SIZE - 1)


def get_neighbors(row, col):
    """
    Return valid neighboring cells.

    Order:
    Right, Down, Left, Up
    """

    directions = [
        (0, 1),    # Right
        (1, 0),    # Down
        (0, -1),   # Left
        (-1, 0)    # Up
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
            neighbors.append((new_row, new_col))

    return neighbors


def bfs():
    """
    Breadth-First Search.
    Returns the number of nodes expanded.
    """

    queue = deque([START])
    visited = {START}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL:
            return nodes_expanded

        for neighbor in get_neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return nodes_expanded


def dfs():
    """
    Depth-First Search.
    Returns the number of nodes expanded.
    """

    stack = [START]
    visited = {START}
    nodes_expanded = 0

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current == GOAL:
            return nodes_expanded

        neighbors = get_neighbors(*current)

        # Reverse so that DFS explores
        # Right -> Down -> Left -> Up
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return nodes_expanded


def profile_algorithm(algorithm, runs=1000, repeats=5):
    """
    Measure execution time using timeit.

    Each repeat performs 'runs' searches.
    """

    measurements = timeit.repeat(
        algorithm,
        number=runs,
        repeat=repeats
    )

    average_total_time = sum(measurements) / len(measurements)

    average_time_per_search = (
        average_total_time / runs
    )

    return average_time_per_search * 1000


def main():

    print("=" * 65)
    print("       SLE-2: BFS vs DFS PERFORMANCE ANALYSIS")
    print("=" * 65)

    print(f"\nGrid Size       : {SIZE} x {SIZE}")
    print(f"Start Position  : {START}")
    print(f"Goal Position   : {GOAL}")

    bfs_nodes = bfs()
    dfs_nodes = dfs()

    print("\n--- NODE EXPANSION ---")
    print(f"BFS Nodes Expanded: {bfs_nodes}")
    print(f"DFS Nodes Expanded: {dfs_nodes}")

    runs = 1000
    repeats = 5

    bfs_time = profile_algorithm(
        bfs,
        runs,
        repeats
    )

    dfs_time = profile_algorithm(
        dfs,
        runs,
        repeats
    )

    print("\n--- PROFILING RESULTS ---")
    print(f"Profiling Repeats : {repeats}")
    print(f"Searches per Repeat: {runs}")

    print(f"\nBFS Average Time per Search: {bfs_time:.4f} ms")
    print(f"DFS Average Time per Search: {dfs_time:.4f} ms")

    print("\n--- COMPARISON ---")

    if bfs_time < dfs_time:
        print("BFS took less execution time in this experiment.")
    else:
        print("DFS took less execution time in this experiment.")

    if bfs_nodes < dfs_nodes:
        print("BFS expanded fewer nodes.")
    else:
        print("DFS expanded fewer nodes.")

    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
