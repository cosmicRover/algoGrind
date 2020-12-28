class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        This is a greedy problem but one key item that may not be clear on first glance.
        Yes we have to sort it to get the lowest possible costs for each city but in doing so
        we may neglect the lowest possible cost for the other city thus not reaching the correct answer.
        
        Instead, we can sort for the difference of costs between cityA and cityB x[0] - x[1] in this way,
        the lowest costs for city A will be in 0 to n and lowest for city B will be in n to 2n.
        Only works on two values.
        
        time O(n log n) | space O(1)
        
        '''
        
        #sort by the difference: cityA - cityB
        costs.sort(key = lambda x: x[0]-x[1])
        
        cost = 0
        n = len(costs)//2
        
        #add cost for cityA and cityB
        for i in range(n):
            a = costs[i][0]
            b = costs[i+n][1] #since costs is always even length, we can just jump with addition
            
            cost += (a+b)
            
        return cost