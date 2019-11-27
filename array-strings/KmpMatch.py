'''
TODO: Only precompute part is implemented, needs the pattern matching part.
We use KMP to compute the longest prefix that is also the suffix. This comes in very handy
while checking for a pattern within a given string as it helps us not re-do work
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        result = self.kmpPrecompute(s)
        print(result)
    
    def kmpPrecompute(self, s):
        table = [0] * len(s) #the table that will hold pref/suf info
        
        #two pointer approach
        i = 0
        j = 1
        
        while True:
            
            if i == len(s) or j == len(s):
                break
            
            if s[i] != s[j]: #if i and j not a match, just increment j
                j+= 1
            
            elif s[i] == s[j]: #if it's a match, put down i+1 on table
                table[j] = i + 1
                i+=1
                j+=1
                
        return table