class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        this question ISN"T asking to find every word from wordDict
        but rather asking to find if s can be segmented into the words
        from wordDict. DP can be used to work on this problem
        
        this is a dp problem
        time O(n^3) | space O(n+1)
        '''
        dic = set(wordDict)
        
        #
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1, len(dp)): #O(n) time
            
            for j in range(i): #O(n) time
                
                #sub contains all possible contiguous combination up to i
                sub = s[j:i] #O(k) time worst O(n)
                
                #if from s[j:i], j is already found and sub is a word in dic
                if dp[j] and sub in dic:
                    dp[i] = True #set current index i to true
                    break
        
        return dp[-1]