SLE-2: Empirical Performance Analysis of BFS and DFS
Student Details

Name: Vaishnavi Sudhir Ghodake
PRN: 26UAM315
Course: Introduction to Artificial Intelligence
Course Code: 02AML204
Program: SY B.Tech. CSE (AI & ML)

Experiment

SLE-2 – Profiling Report (Empirical Performance Analysis)

Topic

Empirical Comparison of Breadth First Search (BFS) and Depth First Search (DFS)

1. Objective

The main purpose of this experiment is to experimentally evaluate and compare BFS and DFS based on the following parameters:

Execution time
Number of nodes explored
Performance under different search conditions
Profiling using Py-Spy

Both algorithms are tested using the same graph and search problem to ensure that the comparison is fair.

2. Algorithms Used
Breadth First Search (BFS)

BFS visits the graph one level at a time. It uses a queue to maintain the nodes that need to be explored.

Depth First Search (DFS)

DFS follows one branch as far as possible before returning and exploring another branch. It uses a stack for storing the nodes to be visited.

3. Graph Used

A small graph consisting of nodes from A to Z is considered for the experiment.

The search begins from:

A

Three different goal nodes are considered to represent different search conditions:

Best Case → B
Average Case → M
Worst Case → Z
4. Cases Tested
Case	Start Node	Goal Node
Best Case	A	B
Average Case	A	M
Worst Case	A	Z

For each case, both BFS and DFS were executed three times and their performance was recorded.

5. Performance Metrics

The experiment considers the following performance measures:

Average execution time in milliseconds
Number of nodes expanded during the search

Python's time.perf_counter() function was used to obtain the execution-time measurements.

Py-Spy was also used to perform additional runtime profiling of the Python program.

6. Experimental Results
Case	Algorithm	Nodes Expanded	Average Time (ms)
Best	BFS	2	0.00527
Best	DFS	2	0.00253
Average	BFS	13	0.00833
Average	DFS	22	0.01127
Worst	BFS	26	0.01127
Worst	DFS	23	0.01057
7. Search Paths
Best Case

BFS:

A → B

DFS:

A → B

Average Case

BFS:

A → C → F → M

DFS:

A → C → F → M

Worst Case

BFS:

A → C → F → M → Z

DFS:

A → C → F → M → Z

8. Profiling with Py-Spy

Py-Spy was used as an additional profiling utility to examine how the Python search program behaves during execution.

A profiling output file named:

profile.svg

was created using Py-Spy.

The profiling program repeatedly runs the BFS and DFS searches so that Py-Spy gets enough execution samples to represent the runtime activity.

9. Observations

Both BFS and DFS were evaluated using the same graph and search conditions.

For the best case, both algorithms expanded 2 nodes, since the target node was reached immediately.

For the average case, BFS expanded 13 nodes, whereas DFS expanded 22 nodes.

For the worst case, BFS expanded 26 nodes and DFS expanded 23 nodes.

The measured execution times are very small because the experiment uses a relatively small graph. Hence, the number of nodes expanded is also useful when examining the search behaviour of the two algorithms.

The results show that the performance of BFS and DFS can vary depending on the location of the goal node and the structure of the search graph.

10. Tools Used
Python
time.perf_counter()
Py-Spy
PowerShell
GitHub
11. Files in This Project
SLE2_IAI/
│
├── bfs_dfs.py
├── profile_search.py
├── profile.svg
├── README.md
└── CONTRIBUTION.md
12. Conclusion

BFS and DFS were implemented and evaluated using the same graph under best-case, average-case, and worst-case search conditions. The execution time and number of expanded nodes were recorded for each experiment and used to compare their observed performance.

Py-Spy was additionally used to inspect the runtime behaviour of the search program. The experiment helped demonstrate that actual performance measurements, together with theoretical knowledge, provide a better understanding of how search algorithms behave under different conditions.
