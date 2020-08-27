'''
This looks simple but the gimmick comes from k being bigger than len(nums)
Time O(N) | Space O(1)
'''

class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        
        #just reverses an array
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    
    def rotate(self, nums: [int], k: int) -> None:
        
        n = len(nums)
        k %= n #modding by n to adjust for the position shifts
        
        #reverse fully first
        self.reverse(nums, 0, n - 1)
        print(nums)
        
        #reverse from the given target
        self.reverse(nums, 0, k - 1)
        print(nums)
        
        #reverse 
        self.reverse(nums, k, n - 1)
        print(nums)