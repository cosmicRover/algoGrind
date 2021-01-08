class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        backtracking traverses a path until it isn't suitable, then
        abandons the path for a new more suitable path
        '''
        self.ans = []
        self.backtrack(graph, 0, [0], len(graph)-1)
        return self.ans
    
    def backtrack(self, graph, node, path, target):
        #define basic step aka when will this algorithm stop
        if node == target:
            self.ans.append(path[:])
            return
        
        #define recursive step aka when it will keep going and/or abandon a path
        for child in graph[node]:
            #keep going
            path.append(child)
            self.backtrack(graph, child, path, target)
            
            #abandon an element on the path
            path.pop()