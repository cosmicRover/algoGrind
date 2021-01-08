from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        subsets duplicate pattern. subset index -> copy list -> append[i]

        time O(n * 2^n) | space O(n * 2^n)
        '''
        
        #since output can't contain any duplicate sets, we need slight modifications
        #sort to detect duplicates and employ custom indexes for list
        
        nums.sort()
        
        ans = []
        ans.append([]) #start with empty
        
        subsetStart = 0; subsetEnd = 0; #custom indexes to get around duplicates
        
        for index, num in enumerate(nums):
            #since we need the previous complete subset, we always start listStart at 0
            subsetStart = 0
            
            #detect duplicate, since we sorted, duplicates will be next to each other
            if index > 0 and nums[index] == nums[index-1]:
                #jump to the last newest created subset to avoid duplicates
                subsetStart = subsetEnd + 1
                
            #re-save end
            subsetEnd = len(ans)-1
            
            #copy list and append
            for i in range(subsetStart, subsetEnd+1):
                copy = list(ans[i])
                copy.append(num)
                ans.append(copy)
                
        return ans
        
        
        