class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # init the 2d matrix with 1's
        table = [[1 for x in range(m)] for y in range(n)]

        # using a double for loop we traverse through the matrix, we also start at [1][1]
        # for each cell we add the top and left value of the column and row <- formula
        for row in range(1, n):

            for column in range(1, m):

                table[row][column] = table[row-1][column] + table[row][column - 1]

        print(table)

        # return the last cell of the table
        return table[-1][-1]
