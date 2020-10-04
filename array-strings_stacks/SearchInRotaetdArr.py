'''
Binary search on a sorted rotated array using left mid right target comparison.
An alternative to pivot detection algorithm
Time O(log(n)) | Space O(1)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums: return -1
        
        left = 0; right = len(nums) - 1;
        
        while left <= right:
            
            mid = (left+right)//2
            
            if nums[mid] == target: return mid
            
            if nums[mid] > nums[right]: #left might be sorted
                
                #look for target on left
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else: #right might be sorted
                
                #look on the right
                if target > nums[mid] and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid - 1
                    
        return -1



'''
Pivot detection algorithm
Time O(log(n)) | Space O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #linear: bad approach
        # for i, v in enumerate(nums):
        #     if v == target:
        #         return i
        # else: return - 1
        
        if  len(nums) == 1: return 0 if nums[0] == target else -1
        
        #find pivot first, pivot element is largest element 
        pivot = self.findPivot(nums, 0, len(nums)-1)
        print(pivot)
        
        #check if pivot is the target
        if nums[pivot] == target: return pivot
        
        #now search for the target within the boundaries
        if pivot == 0: #if pivot was 0, it's a regular binary search
            return self.binarySearch(nums, 0, len(nums)-1, target)
        
        #check if traget is on the right side of pivot, then pass pivot as left boundary
        if target < nums[0]:
            return self.binarySearch(nums, pivot, len(nums)-1, target)
        
        #for any other cases, search from 0 to pivot point
        else:
            return self.binarySearch(nums, 0, pivot, target)

            
    def binarySearch(self, arr, left, right, t):
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] == t: return mid
            
            if t > arr[mid]:
                left = mid + 1
            elif t < arr[mid]:
                right = mid - 1
        
        return -1
        
    def findPivot(self, arr, left, right):
        if arr[left] < arr[right]:
            return 0 #already sorted 
        
        #start looking for a pivot point
        while left <= right:
            mid = (left+right)//2
            
            #check right+1 for pivot
            if arr[mid] > arr[mid+1]:
                #[... 7, 0, 1]
                return mid+1 #found the pivot
            
            else:
                #readjust left and right to keep searching
                #if mid is less than left boundry, pivot must be on left
                
                #***gotta look to minimize right boundry first
                if arr[mid] < arr[left]:
                    right = mid - 1
                
                #otherwise it must be on right
                else:
                    left = mid + 1