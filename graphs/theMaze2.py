# imaginne you are a little ball in a 2d maze and you can only go up, downn, left or right. Once you beign to roll, you can't stop
# until you hit a wall. Given a certain maze, would you be able to reach the destination from a given starting point? Assuming the
# grid is unnweighted

# This solution utilizes the BFS tecnique along with direction vectors

import heapq


class Maze:
    def shortestDistance(self, maze, start, destination):
        width, height, queue, distannce = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]): 0}
        #the four directions the ball could go
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()  # keep track of all the visited coordinates
        
        while queue:
            #O(1) operation using the libraray
            dist, x, y = heapq.heappop(queue)
            
            # if we had reached the destination, return the accumulated dist
            if [x, y] == destination:
                return dist
            
            # if the x and y is already in visisted, continue to the next loop
            if (x, y) in visited:
                continue  # second line
            else:
                visited.add((x, y))  # third line
            
            for i, j in directions:
                
                #init nnew x and y with prev x, y and distance of 0
                newX, newY, d = x, y, 0
                
                #roll the ball till we hit a 1 and increase the distannce while doing so
                while 0 <= newX + i < width and 0 <= newY + j < height and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                
                # if the distance set doesnnt have newX and newY or has a smaller distance
                if (newX, newY) not in distannce or dist + d < distannce[(newX, newY)]:
                    #add to distance set and add to queue
                    distannce[(newX, newY)] = dist + d
                    heapq.heappush(queue, (dist + d, newX, newY))
        return -1


m = Maze()
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = [0, 4]
dest = [4, 4]

print(m.shortestDistance(maze, start, dest))
