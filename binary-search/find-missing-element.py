from collections import Counter

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        Take advantage of the sorted nature and use binary search.
        
        This is quite tricky as it requires to derive a formula to find accumulated missing numbers
        from the sorted array and everything else revolves around it.
        
        as it stands time O(n) finding missing needs to be optimized for logN binary search to shine
        space O(1)
        '''
        
        missing = []
        
        #finds number of elements missing at an index
        #for input [4, 7, 9, 10] missing at 
        #index 0 is 0, index 1 is 2, index 2 is 3, index 4 is 3. missing[i] = missing at index i + missing[i-1]
        
        for index, val in enumerate(nums): #can be optimized with built in functions
            missing.append(nums[index]-nums[0]-index)
            
        #if missing number is out of bounds
        #add max from nums with k and substract the difference from accumulated missing 
        if k > missing[-1]:
            return nums[-1]+(k-missing[-1])
            
        #binary search
        left = 0
        right = len(nums)-1
        
        #our goal is to find the k'th missing
        while left < right:
            mid = (left+right)//2
            
            if missing[mid] < k:
                left = mid +1
            else:
                right = mid
              
        #missing number will be on left-1
        #calcualte the missing number using formula
        return nums[left-1] + k - missing[left-1]