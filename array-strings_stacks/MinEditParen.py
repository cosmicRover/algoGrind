'''
This is a twist with the classic stack problem of comparing parans, but this time
we save the indexes instead since we need to edit the string 

Time O(n) | Space O(n)
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        #use a stack to keep track of (
        stack = []
        edit = set()
        
        #since we care about position, we need the index as well
        for i, v in enumerate(s):
            
            #if char is english char, we just continue to next iteration
            if v not in "()":
                continue
            
            #if its's (, we append it
            elif v == "(":
                stack.append(i) #we append position because we can cross ref later
                
            elif v == ")" and not stack:
                edit.add(i) #if we have a ) and stack is empty, this is a candidate for edit
                
            else:
                stack.pop() #we dont need to compare, just pop the stack as we iterate
                
        #for the case when stack isnt empty, we need indexes from stack to be in edit
        if stack:
            for x in stack:
                edit.add(x)
                
        #modify s using edit and compose a new string
        news = []
        for i, v in enumerate(s):
            if i not in edit: #only append to v, if edit index is not the current index
                news.append(v)
                
        #join and return news
        return "".join(news)