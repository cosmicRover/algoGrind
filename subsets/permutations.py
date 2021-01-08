class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        permutations approach. copy list -> append[i] for every position

        time O(n * n!) | space O(n * n!)

        '''
        
        result = []
        temp = [[]]
        
        #for each num in nums
        for num in nums:
            size = len(temp)
            
            #get the old permutation
            for _ in range(size):
                
                old = temp.pop(0)
                
                #insert num in every position
                for i in range(len(old)+1):
                    copy = list(old)
                    copy.insert(i, num)
                    
                    if len(copy) == len(nums):
                        result.append(copy)
                    else:
                        temp.append(copy)
                        
        
        return result
        