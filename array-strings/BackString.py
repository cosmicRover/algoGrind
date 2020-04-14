class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        s = ""
        
        for x in S:
            if x != '#':
                s += x
            
            else:
                s = s[:-1] #override the last character
                
        print(s)
        
        t = ""
                
        for x in T:
            if x != '#':
                t += x
            
            else:
                t = t[:-1]
                
        print(t)
                
        return s == t