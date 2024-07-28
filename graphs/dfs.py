from collections import defaultdict, deque

edgeList = [[1,2],[1,3],[3,4], [3,5],[4,7],[5,6],[7,8]]

adjacencyList = defaultdict(list)
adjacencyMatrix = [[0 for _ in range(9)] for _ in range(9)]


for a, b in edgeList:
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)
    adjacencyMatrix[a][b] = 1
    adjacencyMatrix[b][a] = 1


def DFS(start_node, visited):
    # base case
    if not start_node:
        return
    print(start_node)
    visited.add(start_node)
    for neighbour in adjacencyList[start_node]:
        if neighbour not in visited:
            DFS(neighbour, visited)
              
def DFS_matrix(i,j, visited):
    # base case
    if i < 0 or i >= len(adjacencyMatrix) or j < 0 or j >= len(adjacencyMatrix[0]):
        return 
    if adjacencyMatrix[i][j] == 0:
        return
    
    print(i,j)
    visited.add((i,j))
    
    for r, c in [(0,1), (1,0), (0,-1), (-1,0)]:
        nr = r + i
        nc = c + j
        if (nr,nc) not in visited:
            DFS_matrix(nr, nc, visited)
            
            
