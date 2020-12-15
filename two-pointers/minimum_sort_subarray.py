class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        two pointers left -> right
        from the left we check if i < i+1
        from the right we check if j < j-1
        Time O(n) | Space O(1)
        '''
        #find out of order from the left
        left = 0
        while left < len(nums)-1 and nums[left] <= nums[left+1]:
            left += 1
            
        if left == len(nums)-1: return 0 #in the case input is sorted
        
        #find out of order from the right
        right = len(nums)-1
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
            
        #find the min and max between left and right
        sub_min = float("inf")
        sub_max = float("-inf")
        for i in range(left, right+1):
            sub_min = min(sub_min, nums[i])
            sub_max = max(sub_max, nums[i])
        
        #decrement left so it may find the lowest possible value in the input
        while left > 0 and nums[left-1] > sub_min:
            left -= 1
           
        #increment right so it finds the highest possible value in the input
        while right < len(nums)-1 and nums[right+1] < sub_max:
            right += 1
            
        return right-left+1
    

#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         '''
#         Brute forcing by sorting a copy of the input
#         and checking against it with the original input
#         '''
#         sortedNums = sorted(nums)
        
#         #pointers to remember first and last match
#         first = None
#         last = float("-inf")
        
#         #compare with the original
#         for index, (plain, sort) in enumerate(zip(nums,sortedNums)):
#             if plain != sort:
#                 if not first:
#                     first = index+1
#                 else:
#                     last = max(last, index+1)
        
#         if first and last != float("-inf"):
#             return last - first+1
        
#         if not first:
#             return 0