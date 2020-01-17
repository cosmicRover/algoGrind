'''
Time O(v + e) | space O(dict + graph) -> O(n)
'''

class Solution:
    def bfs(self,node):
        queue= [node]
        
        while(queue):
            _node_=queue.pop(0)
            for neighbor in self.graph[_node_]:
                if self.seen[neighbor] == -1:
                    queue.append(neighbor)
                    self.seen[neighbor] = 1


    def makeConnected(self, n, connections):
        num_cables=len(connections)
        
        if num_cables<n-1: #base case
            return -1
        
        #using self, a var can be tracked globally across methods
        #consider pass the var to methods instead
        self.graph = [[] for _ in range(n)]
        
        #undirected graph
        for i, j in connections:
            self.graph[i].append(j)
            self.graph[j].append(i)
        
        connected=0
        self.seen= [-1] * n
        
        #for each unvisited connections, we perform bfs
        for node in range(n):
            if self.seen[node] == -1 :
                connected += 1 #there is a new connection
                
                self.seen[node] = 1
                self.bfs(node) #bfs will add new visited connections to seen
        
        return connected-1 #why do we return number of solid connection -1? 