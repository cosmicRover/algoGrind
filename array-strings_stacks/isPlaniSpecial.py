#just a variation of isPalin

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #this is the tricky part, we must remove all the special chars
        #and then lower case it. isalnum() returns true if not special char
        s = ''.join(e for e in s if e.isalnum()).lower()
        
        #the, the regualr in place check comes
        left = 0
        right = len(s) - 1
        
        while left <right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
        