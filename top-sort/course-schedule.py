class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        topological sort approach. build indegree/graph -> build sources -> iterate child of sources
        '''
        
        if numCourses <= 0:
            return False
        
        #prep inDegree and graph
        inDegree = {i:0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)} #same as defaultdict(list)
        
        #fill out inDegree and graph
        for child, parent in prerequisites:
            inDegree[child] += 1
            graph[parent].append(child)
            
        #fill in sources aka inDegree of 0
        sources = []
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
         
        path = []
        
        #go through the source and reduce their children's inDegree
        while sources:
            node = sources.pop(0)
            path.append(node)
            
            for child in graph[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
                    
        # print(path)
                    
        #if there is a cycle, path won't match up with # of nodes
        if len(path) != numCourses:
            return False
        
        return True