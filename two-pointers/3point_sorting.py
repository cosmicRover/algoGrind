class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        two pointers left -> right
        3 point sorting system
        Time O(n) | Space O(1)
        """
        low = 0
        high = len(nums)-1
        index = 0
        
        '''
        3 point sorting: needs 3 distinct values
        swap vals 0 with low
        leave vals 1 alone
        swap vals 2 with high
        if statements need to be chained, cant increment index when swapping high
        '''
        while index <= high:
            #if found a 0, swap with low
            if nums[index] == 0:
                self.swap(nums, index, low)
                low += 1
                index += 1
                
            #if found 1, leave it alone
            elif nums[index] == 1:
                index += 1
            
            #if found 2, swap with high
            elif nums[index] == 2:
                self.swap(nums, index, high)
                high -= 1
        
        
    def swap(self, arr, left, right):
        arr[left], arr[right] = arr[right], arr[left]
    
    
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
        
#         two pointers left -> right
#         cant use extra space
#         swap with pointers
#         this is not O(n)? | Space O(1)
#         """
#         self.left = 0
#         self.right = self.left
        
#         self.sortHelper(nums, 0)
        
#         self.right = self.left
#         self.sortHelper(nums, 1)
    
#     def sortHelper(self, arr, match):
#         while self.left <= self.right and self.right < len(arr):
#             if arr[self.right] == match:
#                 self.swap(arr)
#                 self.left += 1
            
#             self.right += 1
            
#     def swap(self, arr):
#         arr[self.left], arr[self.right] = arr[self.right], arr[self.left]