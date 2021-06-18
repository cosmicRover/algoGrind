class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        max/min dp +1 approach. get max/min from previous paths -> add current path
        '''
        height = len(matrix)
        width = len(matrix[0])

        #init dp to be +1 bigger
        dp = [[0 for _ in range(width+1)] for _ in range(height+1)]

        longest = 0

        #iterate over the matrix and save on dp
        for row in range(1, height+1):
            for col in range(1, width+1):

                #always one step behind on the input matrix
                if matrix[row-1][col-1] == "1":

                    # instead of adding to current path, save the minimum of three directions + 1
                    dp[row][col] = min(
                        dp[row][col-1], dp[row-1][col], dp[row-1][col-1])+1
                    longest = max(longest, dp[row][col])

        #square the longest value to get the actual size
        return longest**2
