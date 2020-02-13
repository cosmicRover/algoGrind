'''
Time O(n!)??? | Space O(n*n) for dp matrix
'''

class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        
        table = [[0] * length for _ in range(length)]
        
        for j in range(length):
            for i in range(j-1, -1, -1):
                
                #dp core formula
                if s[i] == s[j]:
                    table[i][j] = table[i+1][j-1]
                else:
                    table[i][j] = min(table[i+1][j], table[i][j-1]) + 1
                    
                # print(table)
                
        return table[0][-1] #the min edit is stored on at the last cell of first row [0][-1]
                

'''
dp[i,j] stands for the minimum insertion steps to make s[i:j+1] palindrome.
If s[i] == s[j] then dp[i,j] should be equal to dp[i+1,j-1] as no extra cost needed for a palidrome string to include s[i] on the left and s[j] on the right.
Otherwise, dp[i,j] take an extra 1 cost from the smaller cost between dp[i+1,j] and dp[i,j-1].
Then the recurrence equation would be:
dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1]) + 1

To build a bottom-up iteration, we need to iterate all the combination of (i, j) where i < j.
There is no need to check dp[i,i] which is 0.
Another base case is dp[i,i-1]. This happens only when we are checking a dp[i,i+1] and s[i] == s[i+1]. This can also be set as 0 so dp[i,i+1] will be 0 correctly.
So we can savely initialized the entire dp array to be filled with 0.
'''