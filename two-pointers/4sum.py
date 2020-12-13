class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        encapsulate 2sum within 3sum and 4some loop for first and second value
        then the two sum will provide the other two values for four some
        bigger problem is ksum which isnt detailed here
        
        Time O(n^3) | Space O(n) for the valid quadruplets
        '''
        if not nums: return
        
        nums.sort()
        ans = []
        
        for first in range(len(nums)-3): #for 4Sum
            if first > 0 and nums[first] == nums[first-1]: continue #skip the duplicates when i > 0
            
            for second in range(first+1, len(nums)-2): #for 3Sum
                if second > first + 1 and nums[second] == nums[second-1]: continue #skip the duplicates when j > i+1
                    
                self.twoSum(nums, target, first, second, ans)
        return ans
    
    '''
    standard two sum
    left is after second while right stays the same
    '''
    def twoSum(self, nums, target, first, second, ans):
        left = second + 1
        right = len(nums)-1
        
        while left < right:
            sum = nums[first]+nums[second]+nums[left]+nums[right]
            
            if sum == target:
                ans.append([nums[first], nums[second], nums[left], nums[right]])
                left += 1
                right -= 1
                
                #reduce duplicates
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                while nums[right] == nums[right+1] and left < right:
                    right -= 1
                    
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
        
        