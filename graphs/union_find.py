"""
Best data structure for finding connected components

- Find(x) - find the representative of x each connected component will have a representative
- Union(x, y) - Unify two disconnected components

: Optimized 
    - Unify based on rank
    - Compress path during find
"""

class UnionFind:
    def __init__(self) -> None:
        numOfElements = 5
        parent = [i for i in range(numOfElements + 1)]
        rank = [0] * numOfElements + 1
        
    def find_without_path_compression(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find( self.parent[x] )   
        return self.parent[x]
    
    def union_without_rank(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            self.parent[rooty] = rootx
            
    def union_with_rank(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[x] > self.rank[y]:
                self.parent[rooty] = rootx
            else:
                self.parent[rootx] = rooty
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[rooty] += 1
            
        
    
    
            
            
        
        

