'''
The trick for stones 2 is to calculate every possible +- combinations for each elements
of the given array.
Time O(n^2) | Space O(number of unique values generated in the dict)
'''

class Solution:
    
    def lastStoneWeightII(self, stones: List[int]) -> int:
        w = {0} #main dict, start with 0
        
        #loop through each item in stones + each item in dp dict
        #and calculate +- of each val in dict
        for x in stones:
            t = set()
            
            for i in w:
                t.add(abs(x - i))
                t.add(abs(x + i))
                
            w = t
            print(w)
            
        print(w)
        
        return min(w) if len(w) > 0 else 0