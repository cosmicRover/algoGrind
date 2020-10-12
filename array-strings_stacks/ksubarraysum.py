'''
Continous subarray sums can be found without generating all the subarray using the running sum concept
The running sum concept keeps track of all the sums as new elements get seen, gets running_sum-k count 
and saves running_sum to the dic for future iterations.

Time O(n) | Space O(n)

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #get running sum and store them
        
        dic = {0:1} #without 0:1 count is always one behind
        rs = 0; count = 0;
        
        for x in nums:
            rs += x
            
            #get diif to reach k
            diff = rs-k
            
            #increment count from diff's value on dic
            count += dic.get(diff, 0) #.get format gets the value or gives a 0
            
            #add 1 and save running sum
            dic[rs] = dic.get(rs, 0) + 1
            
        return count