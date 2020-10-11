'''
Can do it in O(n) using the product then divide approach. But there is a new approach
with left and right product array. It can even be O(1) space

Time O(n) | Space O(1) ans dont count
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left right O(1) space approach, keep products in the ans array
        
        ans = [1 for x in nums]
        
        #get left side product and save to ans[i]
        for i in range(len(nums)):
            if i == 0: continue
            ans[i] = nums[i-1] * ans[i-1]
            
        #get the right side product, but right side is a constant
        r = 1
        for i in range(len(nums)-1, -1, -1): #going in reverse
            ans[i] = ans[i] *r # multiply with the product constant
            r *= nums[i] #set the product constant
            
        return ans

        
        #Left/Right product array approach
#         left = [1 for x in nums]; right = [1 for x in nums]
        
#         #get product for left array
#         for i in range(len(nums)):
#             if i == 0: continue
#             left[i] = left[i-1] * nums[i-1]
            
#         print(left)
        
#         #get product for right array
#         for i in range(len(nums)-1, -1, -1):
#             if i == len(nums)-1: continue
#             right[i] = right[i+1] * nums[i+1]
            
#         print(right)
            
#         #when you multiply left[i] with right[i], you get product for nums[i]
#         for i in range(len(nums)):
#             nums[i] = left[i] * right[i]
            
#         return nums
        
        #brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j: continue
        #         ans[i] *= nums[j]
           
        #product method, work for 16/19 test cases
#         ans = [x for x in nums]
        
#         for i in range(len(nums)):
#             if i == 0: continue
#             nums[i] *= nums[i-1]
            
#         print(nums)
            
#         #now we divide last index by i'th index in
#         for i in range(len(ans)):
#             if ans[i] == 0: continue #to avoid dividng by 0
#             ans[i] = int(nums[-1]/ans[i])
            
#         return ans
        
        
