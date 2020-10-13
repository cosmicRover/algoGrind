class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        Modification on running sum concept. But since we are looking for productd
        of k, we can check the productability using the reaminader of some upto
        ith index
        '''
        rs = 0
        dic = {0:-1} #saves running_sum and indexes only. We dont consider 0 that's why it's index is -1
        
        
        for i, v in enumerate(nums):
            #add to running sum
            rs += v
            
            #check productability with k, only divide if k isnt 0
            if k != 0:
                rs = rs % k
            
            #check if remainder exists in dic
            if rs in dic:
                #using value from dic find the diif to reach productability
                diff = i-dic[rs]
                
                #check if diff > 1
                if diff > 1:
                    return True
            
            #otherwise save the current rs index
            else:
                dic[rs] = i
                
                
        return False
            
            
            
            
            
            
            
            
            
            