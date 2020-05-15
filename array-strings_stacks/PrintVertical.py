'''
Remember to reduce any trailing space using rstrip()
Time O(n) | space O(n)
'''

class Solution:
    def printVertically(self, s: str) -> [str]:
        s = s.split()
        height = 0
        width = len(s)
        
        #get max height
        for x in s:
            height = max(len(x), height)
        
        #define matrix with width and height
        m = [[" " for _ in range(width)] for _ in range(height)]
        
        #populate matrix from s
        for i, v in enumerate(s):
            for i2, v2 in enumerate(v):
                m[i2][i] = v2
        
        #append to s and remove any trailing space using rstrip()
        s = []
        for x in m:
            s.append("".join(x).rstrip())
            
        
        return s
            