"""
Djikstra: finding the shortest path between two nodes in a positive weighted graph.

TIME: O(Elog(V)) SPACE: O(V)

- Once you run djikstra once, you can get shortest path from source to any other node

Two important elements
1. Adjacency List with weights
2. A hashmap recording, Node: [shortest distance from source, previous vertex]
3. Heap/Priority Queue for low cost node
4. Visited set
"""
from collections import defaultdict
from heapq import heapify, heappop, heappush

# undirected graph with 5 weighted edges
graph = [['A','C',1], ['A','B',2],['B','E',5], ['C','D',1], ['D','E',2]]

# Q: find shortest path from A to any other node (B, C, D, E)
source = 'A'
adjList = defaultdict(list)
for a, b, weight in graph:
    adjList[a].append((weight, b))
    adjList[b].append((weight, a))
    
visited = {}

priority_queue = [(0,source)]
heapify(priority_queue)

while priority_queue:
    print(priority_queue, visited)
    
    weight, node = heappop(priority_queue)
    visited[node] = visited.get(node, weight)
    
    for cost, nei in adjList[node]:
        if nei not in visited:
            cost = min(weight + cost, float('inf'))
            heappush(priority_queue, (cost, nei))
            
print(visited['B'])


