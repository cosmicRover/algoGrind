class Solution:
    def removeDuplicates(self, S: str) -> str:
        '''
        use sack string builder approach. stack = [[char, count]]
        
        time O(n) | space O(n)
        '''
        
        stack = [["#", 0]]
        
        for x in S:
            #if the last char match
            if stack[-1][0] == x:
                stack[-1][1] += 1 #go ahead and inc count
                
                #if the count is at least 2
                if stack[-1][1] > 1:
                    stack.pop() 
            else:
                stack.append([x, 1])
                
        #reconstruct and return a string from stack
        s = ""
        for char, count in stack:
            s += char*count
        return s
        