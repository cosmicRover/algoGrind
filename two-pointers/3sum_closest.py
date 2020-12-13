class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Two pointer left -> right
        A modified versio of 3sum but with consideration of abs value
        Time O(nlogn + n^2) 
        '''
        
        nums.sort()
        min = float("inf")
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            while left < right:
                s = nums[i]+nums[left]+nums[right]
                diff = target-s #how close we are to the arget
                
                if abs(diff) < abs(min):#use absolute value to work around + and -
                    min = diff
                
                #this is straight from 2sum
                if s < target:
                    left += 1
                else:
                    right -= 1
            
            #if reached the minimum possible, break early
            if min == 0: break
                    
        return target - min #the diff between target - min is the smallest difference