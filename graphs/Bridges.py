'''
This is an implementation of Tarjan's bridge finding algorithm.
Time O(V+E) | Space O(n)
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #graph DS setup
        self.graph = collections.defaultdict(list)
        
        #undirected graph setup
        for s, d in connections:
            self.graph[s].append(d)
            self.graph[d].append(s)
            
        #bridge DS setup. Time is for lowlink and dicovery
        self.time = 0
        visited = set()
        low = [float("Inf")] * n
        disc = [float("Inf")] * n
        parent = [-1] * n
        
        #the bridges that we keep
        self.results = []
        
        #iterate over each node
        for node in range(n):
            if node not in visited:
                self.findBridge(node, low, parent, visited, disc)
            
        return self.results
        
    
    
    def findBridge(self, node, low, parent, visited, disc):
        #memoize the given node's time and increment time
        visited.add(node)
        low[node] = self.time
        disc[node] = self.time
        self.time += 1
        
        #find lower cost for each adjacent nodes on the graph
        for v in self.graph[node]:
            
            #memoize for each unvisited v
            if v not in visited:
                #memoize parent
                parent[v] = node
                
                #recursive trail for improved time complexity
                self.findBridge(v, low, parent, visited, disc)
                
                #record the minimum lowlink value for the given node
                low[node] = min(low[v], low[node])
                
                '''
                if lowlink of currently iterating node is more 
                than discovery of given node, we've found a bridge
                '''
                if low[v] > disc[node]:
                    self.results.append([node, v])
                    
            elif v != parent[node]:
                low[node] = min(low[node], disc[v])
                