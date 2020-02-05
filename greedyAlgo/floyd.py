
from collections import Counter
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[float('inf')] * n for _ in range(n)] #nxn matrix
        
        for i in range(n):
            adj[i][i] = 0
        
        for u, v, w in edges: #connecting undirected nodes
            adj[u][v] = w
            adj[v][u] = w
            
        print(adj)
        
        #finding the shortest path from all nodes and paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
                    
        print(adj)
        
        neighbors = Counter()
        for i in range(n):
            for j in range(n):
                if i != j and adj[i][j] <= distanceThreshold: 
                    neighbors[i] += 1
        
        print(neighbors)
        
        best = 0
        for i in range(n):
            if neighbors[i] <= neighbors[best]:
                best = i
        return best