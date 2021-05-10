class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        level order bfs with pre-visit approach. while bfs -> queue node and mark them as visited
        
        time O(row * col) in worst case end up visiting them all | space O(row * col) in worst case queue them at least once
        '''

        height = len(grid)
        width = len(grid[0])

        #keep track of fresh oranges to use later
        fresh = 0

        #queue for rotten orange entry points
        q = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 2:
                    q.append([row, col])

                if grid[row][col] == 1:
                    fresh += 1

        #level order bfs on each rotten oranges
        steps = 0

        while q:
            size = len(q)
            steps += 1

            for _ in range(size):
                # no need to mark visited here since they are already marked with 2
                x, y = q.pop(0)
                directions = [[x, y+1], [x+1, y], [x-1, y], [x, y-1]]

                for row, col in directions:
                    #range and value check
                    if 0 <= row < height and 0 <= col < width and grid[row][col] == 1:
                        #bfs pre-visit approach. mark nodes as visited while appending to q
                        q.append([row, col])
                        grid[row][col] = 2
                        fresh -= 1

        return -1 if fresh != 0 else max(steps-1, 0)
