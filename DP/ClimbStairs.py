'''
DP slution. You can take single steps from i-1 steps or double steps from i - 2 steps 
Combind, you can take [i-1] + [i-2] steps

Time O(n) | Space O(n)

Can improve space to O(1) using fibbonachi sequence since this problem qualifies
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 1
        
        #init dp table for n+1
        dp = [i for i in range(n+1)]
        
        #start from index 3 and keep adding
        i = 3
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
            
        return dp[n]