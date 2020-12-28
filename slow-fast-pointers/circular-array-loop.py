class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        '''
        slow/fast pointer. slow.next -> fast.next.next
        #requirements:
        1) can't reverse direction
        2) if we end up back at where we started, we have a cycle except for 0 values
        
        time O(n^2) for inner and outer loop | space O(1) for the pointers
        
        '''

        if not nums: return
            
        #we want to check for every element, if there is a cycle. Thuse we 
        #have two loops. Outer to set slow/fast and inner to move slow/fast
        for i in range(len(nums)):
            slow = fast = i
            
            #get direction. isForward will be True if nums[i] >= 0
            isForward = nums[i] >= 0
            
            while True:
                #move slow and fast once
                slow = self.movePointer(nums, slow, isForward)
                fast = self.movePointer(nums, fast, isForward)

                #move fast one more time if we are able to
                if fast != -1:
                    fast = self.movePointer(nums, fast, isForward)
                
                #if there can't be a cycle and/or there is one, we immediately break
                if slow == -1 or fast == -1 or slow == fast:
                    break
            
            #checks for cycle after inner loop breaks
            if slow != -1 and fast!= -1 and slow == fast:
                return True
            
        return False
            

    #helper function to jump pointers
    def movePointer(self, nums, index, isForward):
        #check if the direction is changing
        _isForward = nums[index] >= 0
          
        if _isForward != isForward: return -1 #-1 is the error value
        
        #jump the the index. jump = (index + arr[index]) % len(arr) 
        nextIndex = (index + nums[index]) % len(nums)
        
        #if we didn't move, aka have a 0 for value, we can't have a cycle
        if nextIndex == index: return -1
        
        return nextIndex
        