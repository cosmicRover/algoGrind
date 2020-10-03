'''
Time is typical O(log(n)) in avergae case but O(n) in worst case | Space O(1)
modified pivot finding algorithm. It requires to check for duplicates.
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:

        pivot = self.findPivot(nums)
        print(pivot)
        return nums[pivot]
    
    
    def findPivot(self, nums):
        #base check
        left = 0; right = len(nums)-1;
        
        #since it has duplicates, this may not work
        # if arr[left] < arr[right]:
        #     return 0
        
        while left < right:
            mid = left+(right-left)//2
            print(nums[mid], nums[mid+1])
        
            #reducing duplicates when possible before jumping to mid comparison
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            #contains negative nums, so instead of left, we check agains right bound
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
                
        return left #left instead of typical mid 