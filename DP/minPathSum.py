class Solution(object):
    def minPathSum(self, grid):

        #time O(n*m) | space O(n*m)
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        #get length and width
        length = len(grid)
        width = len(grid[0])

        #init the table
        table = [[0 for x in range(width)] for y in range(length)]

        table[0][0] = grid[0][0]

        # configure the top row and first column
        for row in range(1, width):
            table[0][row] = grid[0][row] + table[0][row-1]

        #configure the first column
        for column in range(1, length):
            table[column][0] = grid[column][0] + table[column - 1][0]

        #fill out the rest of the tables using 2 for loops
        #formula table's cell = min(left_of_cell, up_of_cell) + inputGrid's current cell value
        for row in range(1, width):
            for column in range(1, length):

                table[column][row] = min(
                    table[column - 1][row], table[column][row - 1]) + grid[column][row]

        print(table)
        return table[-1][-1]


'''
Dijkstra approach!
'''

import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        target = (height-1, width-1)
        
        return self.dijkstra(grid, target, height, width)
    
    
    def dijkstra(self, grid, target, height, width):
        #prep with initial cost and the coordinates
        q = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        
        #start visiting
        while q:
            cost, row, col = heapq.heappop(q)
            
            if (row, col) == target:
                return cost
            
            #we can get away with only visiting down and right
            directions = [(row+1, col), (row, col+1)]
            
            #for each direction calculate updated cost and append to heap
            for x, y in directions:
                if 0<=x<height and 0<=y<width and (x,y) not in visited:
                    #add the only directions we are visiting
                    visited.add((x, y))
                    
                    newCost = grid[x][y] + cost
                    heapq.heappush(q, (newCost, x, y))
