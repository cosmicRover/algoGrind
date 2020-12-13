class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
        two pointer left -> right
        '''
        
        nums.sort()
        left = 0
        right = len(nums)-1
        m = -1
        
        while left < right:
            sum = nums[left]+nums[right]
            
            if sum >= k:
                right -= 1
                
            if sum < k:
                m = max(m, sum)
                left += 1
            
        return m