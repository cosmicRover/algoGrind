class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        This is identical to finding island except that we have to find shapes of the islands
        and return only the unique shapes.
        
        To find a shape: find the starting row, col of the shape and substract the newly found row, col as
        you traverse.
        
        time O(row * col) | space O(row * col since we may traverse all at worst)
        
        '''
        return self.findIslands(grid)
    
    def findIslands(self, grid):
        '''
        bfs approach. pop(0) on directions
        '''
        
        height = len(grid)
        width = len(grid[0])
        num = 0
        shapes = set()
        
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0: continue
                
                q = [(row, col)]
                
                #mark row/col as visited
                grid[row][col] = 0
                
                #start of with subtracting origin row, col
                temp = [(row-row, col-col)]
                
                
                while q:
                    x, y = q.pop(0)
                    
                    #directions we can traverse
                    directions = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
                    
                    #traverse the directions and mark them visited
                    for x, y in directions:
                        if 0<=x<height and 0<=y<width and grid[x][y] != 0:
                            q.append((x, y))
                            grid[x][y] = 0
                            
                            #always substract row, col
                            temp.append((x-row, y-col))
                            
                # frozenset lets us use an array as a key for a dictionary
                frozen = frozenset(temp)
                shapes.add(frozen)
                
        return len(shapes)          