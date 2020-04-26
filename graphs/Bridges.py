'''
This is an implementation of Tarjan's bridge finding algorithm.
Time O(V+E) | Space O(n)
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph = collections.defaultdict(list)
        self.time = 0
        
        for row in connections:
            s, d = row
            self.graph[s].append(d)
            self.graph[d].append(s)
            
        self.bridges = []
        
        visited = [False] * n
        disc = [float("Inf")] * n
        low = [float("Inf")] * n
        parent = [-1] * n
            
        for x in range(n):
            if visited[x] == False:
                self.bridgeFinder(x, visited, parent, low, disc)
                
        print(self.graph)
        print(self.bridges)
        
        return self.bridges
        
        
    def bridgeFinder(self, u, visited, parent, low, disc):
        visited[u] = True
        
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        
        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                self.bridgeFinder(v, visited, parent, low, disc)
                
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    print("found a bridge")
                    self.bridges.append([u, v])
                    
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])