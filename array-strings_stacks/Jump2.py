class Solution:
    
    # Time O(n) space #of max elemnts in between smaller array elements?
    def jump(self, nums: [int]) -> int:
        length = len(nums)
        if length <= 1: return 0 #base case
        
        maxIdx = maxJ = jCount = 0
        
        for i in range(length):
            maxIdx = max(maxIdx, i+nums[i])
            
            #if we have reached the maxJ point, inc jump count and increase max jump ability
            if i == maxJ: 
                jCount += 1
                maxJ = maxIdx
            
            #if max jump ability ever reaches or exceeds the end index, return jump count
            if maxJ >= length - 1:
                return jCount