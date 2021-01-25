import random

class Solution:

    def __init__(self, w: List[int]):
        '''
        given the weights of indexes o to n-1, return weighted random
        
        - build a running sum for each index of w
        - get the total sum of w
        - find the index to return using sum * random.random()
        - linear/binary search to find the index
        
        not sure why this question is useful 
        
        time O(n) | space O(n)
        
        '''
        self.running_sums = []
        _sum = 0
        
        for weight in w:
            _sum += weight
            self.running_sums.append(_sum)
        
        self.total_sum = _sum
        
            
    def pickIndex(self) -> int:
        #random.random() returns next random floating point in range 0.0 to 1.0
        #this will be the number we return
        target = (self.total_sum * random.random())
        
        #enumerate through the running sum and find the target
        #since we are just searching for a target, we can binary search
        for i, val in enumerate(self.running_sums):
            if target < val:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()