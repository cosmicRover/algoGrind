'''
Time O(n) for one pass through the arr | Space O(n) for the mem
'''

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        
        i = 0
        mem = []
        
        while i < len(nums):
            if nums[i] == target:
                mem.append(i)
            
            i += 1
            
        if len(mem) == 0:
            return [-1, -1]
        
        if len(mem) == 1:
            return [mem[0], mem[0]]
        
        if len(mem) >= 2:
            return [mem[0], mem[-1]]