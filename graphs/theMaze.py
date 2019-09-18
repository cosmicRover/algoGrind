# imaginne you are a little ball in a 2d maze and you can only go up, downn, left or right. Once you beign to roll, you can't stop
# until you hit a wall. Given a certain maze, would you be able to reach the destination from a given starting point? Assuming the
# grid is unnweighted

# This solution utilizes the BFS tecnique along with direction vectors

from collections import defaultdict


class Maze:
    def hasPath(self, maze: [[int]], start: [int], destination: [int]) -> bool:

        # *** convert to input to a 2d matrix if it wasnt done so already ***
        # convert maze to adjacency list
        # each node is connnected to their, left, right, top and bottom node
        # adjList = defaultdict(dict)

        # #populate the list
        # for row in range(len(maze)):
        #     for item in range(len(maze[row])):
        #         if maze[row][item] == 1:
        #             adjList[row].append(item)
        # print(adjList)

        # init a queue for bfs with height and width
        queue = [start]
        width = len(maze)
        height = len(maze[0])

        # the four directions that the ball can move up, down, left, right
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # iterate through the queue
        while queue:
            # pop the 0th element as x and y coordinates
            # note thant pop(0) is O(n) while deque.popleft() is O(1)

            x, y = queue.pop(0)
            maze[x][y] = 'visited'

            # if the popped item is the destination, then we return
            if x == destination[0] and y == destination[1]:
                print(maze)
                return True

            # iterate through the direction vectors (aka move the ball till we hit a wall)
            for x1, y1 in directions:
                # move it
                row = x + x1
                column = y + y1

                # while we are not outside the maze boundry and we don't hit a wall
                while 0 <= row < width and 0 <= column < height and maze[row][column] != 1:
                    row += x1
                    column += y1

                # once we get out of the loop, we get back to the previous safe spot
                row -= x1
                column -= y1

                # if the path isnt blocked, add it to the queue
                if maze[row][column] == 0:
                    queue.append([row, column])

        print(maze)
        return False


m = Maze()
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = [0, 4]
dest = [4, 4]

m.hasPath(maze, start, dest)
