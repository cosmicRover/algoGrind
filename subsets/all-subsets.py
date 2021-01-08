class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        subsets pattern. copy subset -> add[i]
        
        time O(n * 2^n) 2 since every time our subsets double and n is the number of input.
        we construct a new set from the subset to we multiply it with n
        
        space O(n * 2^n) each we have @^n total subsets and each can take n space
        '''
        subsets = []
        
        #start with empty
        subsets.append([])
        
        #for each item on nums, repeat copy list -> add[i]
        for num in nums:
            subSize = len(subsets)
            
            for i in range(subSize):
                #copy subset into a list
                copy = list(subsets[i])
                
                #add[i]
                copy.append(num)
                
                subsets.append(copy)
                
        return subsets