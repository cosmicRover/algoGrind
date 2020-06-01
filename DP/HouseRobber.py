'''
Time O(n) | Space O(1)
'''

class Solution:
    def rob(self, nums: [int]) -> int:
        prevMax = 0
        currMax = 0
        
        #compare the previousMax and currentMax. The 2 adjacent constraint will work out
        for x in nums:
            temp = currMax
            currMax = max(prevMax + x, currMax)
            prevMax = temp
            
        return currMax