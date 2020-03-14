import re

class Solution:
    def myAtoi(self, str: str) -> int:
        
        # '^[+\-]?\d+'
        
        str = str.strip()
        print(str)
        
        str = re.findall('^[+\-]?\d+', str) #finds and removes anything but the starting number sequence
        print(str)
        
        #try and catch block since converting to int may fail
        try:
            val = int(''.join(str))
            MAX = 2147483647
            MIN = -2147483648
            
            if val > MAX: return MAX
            if val < MIN: return MIN
            
            return val
        except:
            return 0