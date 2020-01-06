'''
We transform the given list into a directed graph. Then we bfs 
through the nodes from the starting point and attempt to find
our target.
'''

class Solution:

    # Time O(v+e)? (can someone clarify it please?), space O(len(graph) + len(visited)) -> O(2n) -> O(n)
    def canReach(self, arr: [int], start: int) -> bool:
        length = len(arr)
        
        graph = [set() for _ in range(length)]
        visited = [-1] * length
        
        #populate the graph. Remember that i must be >= 0 and < length to avoid out of bounds.
        for i, v in enumerate(arr):
            if i+v < length and i+v >= 0:
                graph[i].add(i+v)
            if i-v >= 0 and i-v < length:
                graph[i].add(i-v)
        
        #setup starting point
        queue = [graph[start]]
        visited[start] = 1
        
		#bfs on the nodes
        while queue:
            node = queue.pop(0)
            for x in node:
                if arr[x] == 0:
                    return True
                
                if visited[x] != 1:
                    queue.append(graph[x])
                    visited[x] = 1
                    
        else: return False