class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        cycle sort approach. range(-inf, +inf) -> range check o<num<len
        
        time O(n) | space O(1)
        '''
        
        i = 0
        while i < len(nums):
            newIndex = nums[i] - 1
            
            #since negative numbers will result in an error, we have a range check. nums[i] >0 and nums[i] < len(nums)
            if 0<nums[i]<=len(nums) and nums[newIndex] != nums[i]:
                
                #swap
                nums[newIndex], nums[i] = nums[i], nums[newIndex]
            else:
                i += 1
                
        #look for first missing
        for i, v in enumerate(nums):
            if i+1 != v:
                return i+1
            
        #if no missing, return len+1
        return len(nums)+1