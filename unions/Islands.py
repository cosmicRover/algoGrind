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

'''
Traversing the grid and performing a BFS.
Time O(m*n) | Space O(min(m,n))
'''

class BFSSolution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid: return 0
        
        w = len(grid[0])
        h = len(grid)
        count = 0
        
        #ordinarily, we wouldnt need i, j but since the 1's can be scattered around, we need to make sure that we traverse everything
        for i in range(h):
            for j in range(w):
                
                #if we encounter a 0, we skip to next iteration
                if grid[i][j] == "0": continue
                    
                #setting the current grid[i][j] to 0, using it as visited set
                grid[i][j] = "0"
                
                #init queue and prepare for traversing. q starting point is current i and j
                q = [(i,j)]
                
                #traverse the grid with bfs
                while q:
                    row, col = q.pop(0)
                    
                    #the directions we can go based on row and col
                    moves = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                    
                    for x, y in moves:
                        
                        #check for out of bounds with height and width, and make sure this is a 1 cell
                        if 0<=x<h and 0<=y<w and grid[x][y] == "1":
                            grid[x][y] = "0" #set the cell to visited
                            q.append((x,y))
                        
                count += 1 #when we reach the end of the loop, we have an island
                
        
        return count