class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # entry point has an obstacle, or the final position is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        # figure out the length and the width of the given input
        length = len(obstacleGrid)
        width = len(obstacleGrid[0])

        # init the 2d matrix according to the length and width
        table = [[0 for x in range(width)] for y in range(length)]

        # fill the top row with 1's if zero encountered on obstacleGrid
        # if not, assign the cell to 1 and break
        for row in range(width):
            if obstacleGrid[0][row] != 1:
                table[0][row] = 1
            elif obstacleGrid[0][row] == 1:
                table[0][row] = 0
                break

        # fill the first column with 1's if zero encountered on obstacleGrid
        # if not, assign the cell to 1 and break
        for column in range(length):
            if obstacleGrid[column][0] != 1:
                table[column][0] = 1
            elif obstacleGrid[column][0] == 1:
                table[column][0] = 0
                break

        # usning two for loops iterate through each cell of the table starting at [1][1]
        # if the same cell on the obstacleGrid[column][row] has a 1, assigns table's cell to 0
        for row in range(1, width):
            for column in range(1, length):

                if obstacleGrid[column][row] == 1:
                    table[column][row] = 0
                else:
                    # the formula: currentCell = current cell's top + left
                    table[column][row] = table[column][row - 1] + \
                        table[column - 1][row]

        print(table)
        # return the very last cell
        return table[-1][-1]
