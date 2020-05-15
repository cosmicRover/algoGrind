#An anagram is when two strings have the same amount of characters in same/different orders
#Time O(n) | space O(len(english alphaphets))
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        #first, we record the frequency of letters in s using ord() and array to manipulate index
        count = [0] * 26
        
        for x in s:
            count[ord(x) - ord('a')] += 1
            
        #then we check the frequency of t, this time we decrement it.
        adj = 0 #tracks # of adjustments that need to be made
        for x in t:
            count[ord(x) - ord('a')] -= 1
            
            #if the count is ever < 0, then we need an adjustment
            if count[ord(x) - ord('a')] < 0:
                adj += 1
                
        return adj