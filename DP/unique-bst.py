class Solution:
    def numTrees(self, n: int) -> int:
        '''
        dynamic programmig approach. 1d dp table, formula => dp[i]+=dp[j-1]*dp[i-j]
        
        time O(n^2) | sapce O(n)
        '''
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                
                #formula to calculate all possible unique trees
                dp[i] += dp[j-1] * dp[i-j]
                # print("i= ", i, " j= ", j, "| ", dp[i])
                
        return dp[-1]