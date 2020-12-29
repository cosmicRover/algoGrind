class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        use stack to keep track of the last characters and their count
        if the counts match, pop the last item from stack
        '''
        
        stack = [["#", 0]] #dummy starting point. we can also use (s[0], 1) but need to adjust loop
        
        for x in s:
            lastChar = stack[-1][0]
            
            if lastChar == x: #if we see the last char again
                stack[-1][1] += 1 #inc char counter
                
                if stack[-1][1] == k: #if we have k amount of characters
                    stack.pop() # we pop it out
                    
            else:
                stack.append([x, 1]) #otherwise we will append with multiplicity of 1
                
        
        #reconstruct the string from stack
        s = ""
        for char, multiplier in stack:
            s += char*multiplier
            
        return s
