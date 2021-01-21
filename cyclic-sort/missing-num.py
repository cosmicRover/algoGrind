class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        cyclic sort approach. swap i with new index.
        
        Since nums start with 0, we don't need to adjust new index
        
        time O(n) | Space O(1)
        '''
        
        n = len(nums)
        
        #perform cyclic sort using index approach
        i = 0
        while i < n:
            index = nums[i]
            
            #keep swapping till in the correct place
            if index < n and nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                
            #otherwise move on to next num
            else:
                i += 1
                
        #check for the missing number
        for i, v in enumerate(nums):
            if i != v:
                return i
        
        #if no missing number, return the length
        return n