'''
single pass Time O(n) | Space O(1) with the storage of some temp values
'''

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0; right = len(nums) -1
        
        while left < right:
            if nums[left] == 0:
                item = nums.pop(left)
                nums.append(item)
                right -= 1 #we dec right since popping an item will readjust the left nums value
            else:
                left += 1 #we inc left when it's safe to do so