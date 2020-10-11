class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        This problem doesnt require calculating all the permutations.
        It only want the 'next lexicographically bigger' value from the given list
        
        Time O(n) | Space O(1)
        """
        #detect a value that is bigger form it's immediate left neighbor
        index = len(nums) - 1
        while index > 0 and nums[index-1] >= nums[index]:
            index -= 1
            
        #if index is at 0, no need to find smaller since it's sorted in ascending, just reverse
        if index==0:
            nums[:]=nums[::-1]
            return
            
        #after we found bigger value, look for a smaller value than index-1 
        j = len(nums) - 1
        while nums[index-1] >= nums[j]:
            j -= 1
            
        #now swap j with index-1
        nums[j], nums[index-1] = nums[index-1], nums[j]
        
        #now reverse nums[index-1:]
        nums[index:] = nums[len(nums)-1: index-1: -1] #reverse from last index to index-1, in reverse order