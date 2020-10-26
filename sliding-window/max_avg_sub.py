'''
Time O(n) | Space O(1)
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        sliding window approach:
        keep a sum of all the values that were seen, once we hit k, we move
        start to the right by one and also subtract it from the overall sums
        
        s -> s          k
        [x, x, x, x, x, x, x, x]
        '''
        maxSum = float("-inf"); start = 0; sum = 0;
        
        for i in range(len(nums)):
            #pre-calculated the 
            sum+= nums[i]
            
            #we start to calculate max sum
            if i >= k-1:
                maxSum = max(maxSum, sum/k)
                sum -= nums[start]
                start += 1
                
        return maxSum