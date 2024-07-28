"""
Topological Sort works on DAGs(Directed, Acyclic Graphs)
- There could be multiple topological order

Implementation: 
1. DFS -  a node is visited only after its prerequisites, vertices leading to that node have been visited (post order)
2. Using Khan's algorithm - BFS : nodes with 0 indegree should be visited first

Graph Used
# [A,B] - B depends on A, A needs to be visited first before B

      B
      ^
    /   \
A         D -> E
    \   /
      v
      C
      
Toposort: (1) ABCDE (2) ACBDE     
"""
from collections import defaultdict, deque

graph = [['A','B'],['B','D'], ['A','C'], ['C','D'], ['D','E']]
adjList = defaultdict(list) # node: [prerequites, or vertices leading to the node]

for a, b in graph:
    adjList[b].append(a)
    
# (1) DFS
order = []
visited = set()
def topo_dfs(node):
    if node in visited:
        return
    for dependant in adjList[node]:
        if dependant not in visited:
            topo_dfs(dependant)
    order.append(node)
    visited.add(node)

# FORGET NOT: Iterate through all the nodes and call the dfs
for node in "ABCDE":
    if node not in visited:
        topo_dfs(node)
        
print(order)


# (2) Khan's algorithm - BFS
graph = [['A','B'],['B','D'], ['A','C'], ['C','D'], ['D','E']]
nodes = ['A','B','C','D','E']

topo_order = []
adjList = defaultdict(list) # node: [prerequites, or vertices leading to the node]

indegree = [0] * len(nodes)

for a, b in graph: # prerequite: [to these nodes]
    adjList[a].append(b) 
    indegree[ord(b)-ord('A')] += 1

# fill queue with nodes of indegree 0
queue = deque([nodes[i] for i,n in enumerate(indegree) if n == 0])

while queue:
    node = queue.popleft()
    topo_order.append(node)
    for nei in adjList[node]:
        indegree[ord(nei)-ord('A')] -= 1
        if indegree[ord(nei)-ord('A')] == 0:
            queue.append(nei)
                 
if len(graph) != len(topo_order):
    print("There is a cycle")
else:
    print(topo_order)