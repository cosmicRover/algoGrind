#this is one of the stupidest questions on leetcode...

class Solution:
    #Time (# of time n decerements before no 0 encounters + # of time diff incerments when encountering a 0) | space O(1)
    def getNoZeroIntegers(self, n: int) -> List[int]:
        upper = None
        
        if '0' in str(n):
            upper = self.getNonZeroNum(n)
            diff = n - upper
            return self.balanceZeroOnPair(diff, upper)
        
        else:
            upper = n-1
            upper = self.getNonZeroNum(upper)
            diff = n - upper
            return self.balanceZeroOnPair(diff, upper)
    
    #get n in range
    def getNonZeroNum(self, n):
        while '0' in str(n):
            n -= 1
        return n
    
    #get return values in range
    def balanceZeroOnPair(self, diff, upper):
        while '0' in str(diff) and '0' not in str(upper):
                diff += 1
                upper -= 1
        
        return [diff, upper]