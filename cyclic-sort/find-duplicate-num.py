class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        cyclic sort approach. range is 1 to n, adjust index with - 1

        time O(n) | space O(1)
        '''
        
        i = 0
        
        while i < len(nums):
            newIndex = nums[i]-1
            
            if nums[i] != nums[newIndex]:
                #swap
                nums[i], nums[newIndex] = nums[newIndex], nums[i]
                
            else:
                i += 1
                
        #find the dup;icate
        for i, v in enumerate(nums):
            if i+1 != v:
                return v
            
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        the tortoise and the hare approach that don't require modification of array

        time O(n) | space O(1)
        '''
        
        #point slow and fast to the first element
        slow = fast = nums[0]
        
        #iterate until the entry point of the loop is found
        while True:
            
            #fast is jumping off of the values while slow is moving one at a time
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            #if the are the same, we have an entry point
            if slow == fast:
                break
        
        #reset slow to the begining
        slow = nums[0]
        
        #keep moving both forwrd till they match
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast #or slow