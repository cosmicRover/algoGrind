class Solution:
    def findAllDuplicates(self, nums: List[int]) -> List[int]:
        '''
        cyclic sort approach. nums range from 1 to n. adjust index by - 1
        
        time O(n) | space O(n) if ans counted else O(1)
        '''
        
        i = 0
        
        while i < len(nums):
            #find the adjusted index
            newIndex = nums[i]-1
            
            # keep swapping until it's in the correct index
            if nums[i] != nums[newIndex]:
                nums[i], nums[newIndex] = nums[newIndex], nums[i]
               
            else:
                i += 1
                
        #detect the duplicates aka the ones out of order
        ans = []
        for i, v in enumerate(nums):
            if i + 1 != v:
                ans.append(v)
            
        return ans