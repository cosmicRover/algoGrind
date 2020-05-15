class Solution:
    #this is the key --> 3 cases: if a pal, return 1, ifnot return 2. if no s, return 0
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        if self.isOnePal(s): return 1
        else: return 2
    
    def isOnePal(self, s):
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True