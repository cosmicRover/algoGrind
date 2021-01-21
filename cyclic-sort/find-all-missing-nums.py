class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        cyclic sort. nums start at 1 up to n. adjust index by -1
        
        time O(n) | sapce O(n) if count missing else O(1)
        '''
        
        i = 0
        
        while i < len(nums):
            newIndex = nums[i]-1
            
            if nums[i] != nums[newIndex]:
                #swap
                nums[i], nums[newIndex] = nums[newIndex], nums[i]
                
            else:
                i += 1
                
        #find missing
        missing = []
        for i, v in enumerate(nums):
            if i+1 != v:
                missing.append(i+1)
                
        return missing
        