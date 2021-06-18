class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        bfs with val inserted as an argument (no dijkstra)
        
        time O(n) might end up visiting all the cells | space O(n) for seen dict
        '''
        if grid[0][0] != 0:
            return -1

        #pre-visit
        height = len(grid)
        width = len(grid[0])

        q = collections.deque()
        q.append([1, 0, 0])  # added the steps as a bfs argument (no dijkstra)
        seen = set()
        seen.add((0, 0))

        while q:
            val, x, y = q.popleft()

            if (x, y) == (height-1, width-1):
                return val

            #8 directions
            directions = [(x+1, y), (x, y+1), (x-1, y), (x, y-1),
                          (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

            for i, j in directions:
                if 0 <= i < height and 0 <= j < width and (i, j) not in seen and grid[i][j] == 0:
                    #pre-visit
                    seen.add((i, j))
                    q.append([val + 1, i, j])

        if (height-1, width-1) not in seen:
            return -1
