#this solution is very space efficient while time complexity is very poor

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        
        nums.sort()
        tups = set() # removes duplicates
        
        for index in range(len(nums) - 2): #-2 because we are looking for 2 accompanying num
            
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                current = nums[index]
                leftNum = nums[left]
                rightNum = nums[right]
                
                if current + leftNum + rightNum < 0:
                    left += 1
                
                if current + leftNum + rightNum > 0:
                    right -= 1
                    
                if current + leftNum + rightNum == 0:
                    tups.add(tuple([current, leftNum, rightNum]))
                    
                    #gotta check for duplicates and keep incrementing left/right till we hit an unique value
                    while left < right and leftNum == nums[left + 1]:
                        left += 1
                
                    while left <right and rightNum == nums[right -1]:
                        right -= 1
                    
                    #after we know the next num is unique, we inc/dec normally
                    left += 1
                    right -= 1
                    
        
        tups = list(tups) # convert to a list
        
        return tups[::-1] # return reversed
