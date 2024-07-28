from collections import defaultdict, deque

edgeList = [[1,2],[1,3],[3,4], [3,5],[4,7],[5,6],[7,8]]

adjacencyList = defaultdict(list)
adjacencyMatrix = [[0 for _ in range(9)] for _ in range(9)]


for a, b in edgeList:
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)
    adjacencyMatrix[a][b] = 1
    adjacencyMatrix[b][a] = 1
    
def BFS(start_node, visited):
    queue = deque([start_node])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            print(node)
            visited.add(node)
            for nei in adjacencyList[node]:
                if nei not in visited:
                    queue.append(nei)
                    
                    
def BFS_matrix(i,j, visited):
    queue = deque([(i,j)])
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            print(i,j)
            visited.add((i,j))
            for r, c in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr = i + r
                nc = j + r
                if (nr >= 0 and nr < len(adjacencyMatrix) and
                    nc >= 0 and nc < len(adjacencyMatrix[0]) and
                    adjacencyMatrix[nr][nc] == 1 and 
                    (nr, nc) not in visited):
                    queue.append((nr,nc))
                    