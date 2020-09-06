'''
The trick here is to translate the directionsinto coordinates properly and using a traversal technique
based on the given directions

Time O(m+n) | Space O(visited+ stack) -> O(2n) -> O(n)
'''


class Solution:
    def hasValidPath(self, grid: [[int]]) -> bool:
        h = len(grid)
        w = len(grid[0])
        
        #directions translated from the question
        directions = {
            1: [(0,-1), (0,1)],
            2: [(-1,0), (1,0)],
            3: [(0,-1), (1,0)],
            4: [(0, 1), (1,0)],
            5: [(0,-1), (-1,0)],
            6: [(0, 1), (-1,0)],
        }
        
        s = [(0,0)]
        visited = set()
        
        while s:
            x, y = s.pop()
            
            #check if we reached the last cell
            if x == h-1 and y == w-1: return True
            
            #get the directions and try them out by incrementing with new vars
            for newx, newy in directions[grid[x][y]]:
                x2 = x + newx; y2 = y + newy
                
                #check the boundaries, make sure x1, y1 hasnt been visited, and the opposite of the given x and y are present in directions
                # before trying for a value
                
                if 0 <=x2< h and 0<=y2< w and (x2,y2) not in visited and (-newx, -newy) in directions[grid[x2][y2]]:
                    visited.add((x2,y2)) #memoize the path index only
                    s.append((x2,y2))          
        else:
            return False