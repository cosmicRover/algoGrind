'''
Find the next biggest element on the array.
Time O(n*len(stack)) | space O(len(stack) + res)
'''

class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        
        res = [0] * len(T) #init with the length of T so we don't worry about 0 later
        stack = []
        
        for i, v in enumerate(T):
            
            #pop the items from stack that have index of smaller iitems
            while stack and T[stack[-1]] < v:
                item = stack.pop()
                res[item] = i - item #calcualte the difference and assign to res
            
            #append the current index neverthless
            stack.append(i)
            
        return res