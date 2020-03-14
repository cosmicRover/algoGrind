'''
This solution uses union find to group nodes
Time O(N x M) | Space O(N x M)
'''
class Solution:
    
    def find(self, i):
        if self.graph[i] != i:
            return self.find(self.graph[i])
        return self.graph[i]
    
    #find the roots, and then unionize
    def union(self, i, j):
        iroot, jroot = self.find(i), self.find(j)
        if iroot == jroot: return
        
        self.graph[iroot] = jroot
        self.count -= 1
        
    
    def numIslands(self, grid: [[str]]) -> int:
        if len(grid) == 0: return 0
        
        #find matrix size
        self.length = len(grid); self.width = len(grid[0])
        
        #initial count of 1's on the matrix, we will substract from this
        self.count = sum(grid[i][j] == '1' for i in range(self.length) for j in range(self.width))
        
        #an 1d representation of the matrix for better access
        self.graph = [i for i in range(self.length * self.width)]
        
        for i in range(self.length):
            for j in range(self.width):
                if grid[i][j] == '0': continue
                
                index = i * self.width + j #get to the proper cell of the array based on matrix width
                
                #find and unionize the nodes with their roots
                if j < self.width -1 and grid[i][j+1] == '1':
                    self.union(index, index+1)
                
                if i < self.length -1 and grid[i+1][j] == '1':
                    self.union(index, index+self.width)
            
        return self.count