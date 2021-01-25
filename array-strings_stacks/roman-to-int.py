class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        since if the previous > current char we subtract it, we employ
        it here using  prev pointer.
        
        time O(1) | space O(1)
        '''
        
        
        digits = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000
            }
                        
        _sum = 0
        prev = 0
        
        for c in s[::-1]:
            curr = digits[c]
            
            if prev > curr:
                _sum -= curr
            else:
                _sum += curr
                
            prev = curr
        
        return _sum