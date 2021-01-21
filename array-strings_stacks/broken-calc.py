class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        '''
        this is a math problem. trying with bfs is too time consuming.
        instead of x reaching y, try y reaching x.
        
        this is a math based intuition, don't know how this helps me to solve other problems
        
        time O(log Y) | space O(1)
        
        '''
        count = 0
        
        while Y > X:
            #if Y is even increment Y
            if Y % 2:
                Y += 1
            
            #otherwise divide by 2
            else:
                Y /= 2
                
            count += 1
            
        #x-y takes care of any difference that may arise and in the case y < x
        return int(count + X-Y) 