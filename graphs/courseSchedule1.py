class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        #create a graph and a visited arry with len of numOfCourses
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # populate the graph
        for pair in prerequisites:
            child, parent = pair
            graph[parent].append(child)
        
        # visit each node and call dfs recursively
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        
        # Mark as being visisted, visit all neighbors and then set node as visited
        # mark as being visited
        visited[i] = -1
        
        # visit all the neighbours recursively
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True

