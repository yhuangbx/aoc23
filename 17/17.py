import sys
from collections import defaultdict

# sys.setrecursionlimit(5000)

D = open(sys.argv[1]).read().strip()
G = [[c for c in r] for r in D.split('\n')]

R = len(G)
C = len(G[0])

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=" ")

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_vertex = 'A'
print("BFS starting from", start_vertex)
bfs(graph, start_vertex)
