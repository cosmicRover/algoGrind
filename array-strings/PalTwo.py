'''
A variation of the palindrome problem.
It is solved here with both left and right inc/dec
'''

class Solution:
    
    def check_palindrome(self, s, direction):
        skip = 0
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                skip += 1
                if direction == 'left':
                    l += 1
                elif direction == 'right':
                    r -= 1
            
            if skip > 1:
                    return False
        
        return True
    
    
    def validPalindrome(self, s: str) -> bool:
        return self.check_palindrome(s, 'right') or self.check_palindrome(s, 'left')