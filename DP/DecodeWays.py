'''
Classic dp problem with the twist that single digits has to be betwwen 1 and 9 and 
double digits has to be between 10 and 26. We save i's value on i+1 and handle the
base/error case. Since we can only gurantee 1 as out put(after handline error case)
we set dp[0:1] as 1 and start iterating on index 2
Time O(n) | Space O(n) can optimize dp two a vars holding cur, prev, and prev - 2 for O(1) space
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        #error case. Anyting begins with 0 is an error
        if s[0] == "0": return 0

        dp = [0 for x in range(len(s)+1)] #init dp table with 0
        dp[0:1] = [1,1] #since we save result of i on i+1, we init dp[0:1] as 1
        
        for i in range(2, len(s) + 1): #starting with index 2, we start calculating previous 2.
            #Even if len(s) is 2: index 2 will trigger resulting in one dight: 1 and two digit: 2
            
            #single digit check
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            
            #two digit check
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            
        print(dp)
        return dp[len(s)] # we can also do dp[-2] but need to be careful on len(s)