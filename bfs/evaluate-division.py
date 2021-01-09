class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        This is a graph problem, the values can be used as edge weights. Use regular bfs to travel to target node.
        
        time O(v+e) | space O(e) for results array
        
        '''
        #use defaultdict to store graph with edge weights
        graph = collections.defaultdict(dict)
        
        #build the graph with provided nodes and edge weights
        for nodes, weight in zip(equations, values):
            u, v = nodes[0], nodes[1]
            
            #undirected graph
            graph[u][v] = weight
            graph[v][u] = 1/weight
            
        #traverse the graph using bfs
        results = []
        
        for u, v in queries:
            #invalid node
            if u not in graph or v not in graph:
                results.append(-1.0)
            #a loop
            elif u == v:
                results.append(1.0)
            #go ahead and search 
            else:
                val = self.bfs(u, v, graph)
                results.append(val)
                
        return results
             
    def bfs(self, start, target, graph):
        visited = set()
        q = [(start, 1)]
        
        while q:
            node, weight = q.pop(0)
            
            if node == target:
                return weight
            
            visited.add(node)
            
            for item in graph[node]:
                if item not in visited:
                    #update weight to previous weight * item's weight in graph[node][item]
                    q.append((item, weight*graph[node][item]))
        return -1
            