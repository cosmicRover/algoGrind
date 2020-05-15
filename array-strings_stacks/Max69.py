class Solution:
    def maximum69Number (self, num: int) -> int:
        s = [x for x in str(num)]
        
        for x in range(len(s)):
            if s[x] == '6':
                s[x] = '9'
                break
                
        s = ''.join(s)
        return int(s)