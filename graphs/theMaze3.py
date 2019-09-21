#very similar to the maze 2 but we break early at line 47

import heapq

class Solution:
    def findShortestWay(self, maze: [[int]], ball: [int], hole: [int]) -> str:
        
        #define the width, height, queue and distance
        width, height = len(maze), len(maze[0])
        queue = [(0, "", ball[0], ball[1])] # define queue with distance, ball x coordinate, ball y coordinate
        distance = {(ball[0], ball[1]) : [0, ""]} # the distance hash will conatin each x, y coordinate and their distance value + pos
        
        #the directions the ball could travel through as envisioned on a graph represented as tuples
        #direction rotated to the right 90 degress
        directions = ((-1, 0, "u"), (1, 0, "d"), (0, 1, "r"), (0, -1, "l"))
        directionsTaken = ""
        visited = set() #keeps track of the visited nodes
        
        #loop through the queue
        while queue:
            #heap queue will always pop the next smallest item
            dist, pattern, x, y = heapq.heappop(queue)
            
            #if we are at the destination, we return
            if [x, y] == hole:
                return pattern
            
            
            if(x, y) in visited:
                continue
            else:
                visited.add((x,y))
                
            
            for xCord, yCord, pos in directions:
                
                #init new x, y coordinates with distance of 0
                newX, newY, d = x, y, 0
                
                #roll the ball till we hit a 1 and or not go outside of the maze
                #also increase the directions while we are at it
                while 0 <= newX + xCord < width and 0 <= newY + yCord < height and maze[newX + xCord][newY + yCord] != 1:
                    newX += xCord
                    newY += yCord
                    d += 1
                    
                    if [newX, newY] == hole:
                        break
                    
                #add to the distance set if newX and newY doesnt exist or exists with a lesser distance value
                if (newX, newY) not in distance or [dist+d, pattern +pos] < distance[(newX, newY)]:
                    #add the distance to the hash
                    distance[(newX, newY)] = [dist + d, pattern+pos]
                    # push to queue
                    heapq.heappush(queue, (dist + d, pattern+pos, newX, newY))
                    
        return "impossible"
            
            
            