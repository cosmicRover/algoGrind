'''
The intuition is that if s is a substring of itself, then we can check if it's a substring by making it 2 times
Then we remove the first and last element and check to see if the original s is in the new string.
If found, the it is a substring!
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s: return False
        
        ss = 2 * s
        
        print(ss) #the original
        print(ss[1:-1]) #with the first and last cut out
        
        if s in ss[1:-1]: # if original string is in the ss after the cut, then it's a substring
            return True