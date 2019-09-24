#A pq implementation of dijkstra to solve a maze problem
import heapq

class Maze:

    def howManyStepsToEscape(self, maze:[[int]], start:[int], destination:[int]):

        height, width = len(maze), len(maze[0])
        queue = [(0, start[0], start[1])] # init a pq for bfs with starting value distance of 0 since we start from here
        distance = {(start[0], start[1]) : 0}
        
        #define the four + 4 (diagonal) directions and a visisted set to store the visited nodes
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1),  (1, 1), (-1, -1), (-1, 1), (1, -1)) # <--- four diagonal directions
        visited = set()

        while queue:
            #pop an element and assign them to vars
            dist, x, y = heapq.heappop(queue)

            #if we are destination, we returnn the distance we just popped
            if [x, y] == destination: return dist

            # if we had encountered these coordinates before, we move on to the next loop
            if (x, y) in visited:continue
            else: visited.add((x,y))

            # we loop through the 8 directions and append to heap
            for i, j in directions:
                
                #init new x and y (from the popped values) with distance of 0
                newX, newY, newDist = x, y, 0

                #as long as new directions don't go out of bounds and the maze's cell dont contain an 1
                if 0<= newX + i < width and 0 <= newY + j < height and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    newDist += 1

                # if we havent encountered these coordinates before or they have better distance than
                # what we have now, we use their distance and push to our minHeap
                if (newX, newY) not in distance or dist + newDist < distance[(newX, newY)]:
                    distance[(newX, newY)] = dist + newDist
                    heapq.heappush(queue, (dist + newDist, newX, newY))

        return -1


m = Maze()
maze = [
 [0, 0, 0, 0],
 [1, 1, 1, 0],
 [1, 1, 0, 1],
 [0, 0, 0, 1]
]
dest = [0, 0]
start = [3, 2]

print(m.howManyStepsToEscape(maze, start, dest))