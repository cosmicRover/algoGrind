# Time O(n) | Space O(min(n, english_letter_count)) since we store no duplicates
# the space can be at most 26.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        start = 0
        longest = [0, 1] # holds indexes for longest str
        table = {}
        
        for i, l in enumerate(s):
            # if l in table, update start
            # start looks for the maximum starting point without duplicate chars
            if l in table:
                start = max(start, table[l] + 1)
                
            #if string with new start is longer, replace longest
            # len_of_existing < index + 1 - startIndex
            if longest[1] - longest[0] < i + 1 - start:
                longest[0] = start
                longest[1] = i + 1
                
            #add to table/update exiting 
            table[l] = i
            
        st = longest[0]
        e = longest[1]
        print(s[st:e])
        return(e-st)
            