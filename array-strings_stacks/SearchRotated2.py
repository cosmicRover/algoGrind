'''
Binary search on a rotated array using left mid right as comparison points
Time O(log(n)) in best case but O(n) in worst(when there is a lot of dups)
Space O(1)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initilize two pointers
        begin = 0
        end = len(nums) - 1 
        
        while begin <= end:
            mid = (begin + end)//2
            
            #check all three boundaries just in case
            if nums[mid] == target or nums[begin] == target or nums[end] == target:
                return True
            
            # Fail to estimate which side is sorted, reduce/inc end or begin
            if nums[mid] == nums[end]:
                end -= 1  # In worst case: O(n)
            
            #determine which side is sorted
            #[2,5,6,0,0,1,2] t = 2
            elif nums[mid] > nums[end]: # Left side of mid is sorted
                
                if  target >= nums[begin] and target < nums[mid]: # Target in the left side
                    end = mid - 1 #reduce the right pointer
                else: # in right side
                    begin = mid + 1 #otherwise inc left
            
            else: # Right side is sorted
                
                if  target > nums[mid] and target <= nums[end]: # Target in the right side
                    begin = mid + 1
                else: # in left side
                    end = mid - 1
        
        return False