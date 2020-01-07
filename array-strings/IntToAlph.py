class Solution:
    # time O(n) space O(1)
    def freqAlphabets(self, s: str) -> str:
        
        res = ""
        i = len(s) - 1
        
        while i >= 0:
            if s[i] != '#':
                num = int(s[i]) -1 + ord('a') # the formular to get char code
                res += str(chr(num))
                i -= 1
            
            elif s[i] == '#':
                num = int(s[i-2 : i]) - 1 + ord('a') 
                res += str(chr(num))
                i -= 3
                
        return res[::-1]