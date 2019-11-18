'''
Classic stack problem, the trick is to seperate open parens on a stack as we traverse through s
when we encounter an open paren, pop from stack if cehck to see if it's the right type of paren
using a hash table
'''
#Time O(n) Space O(max number_of_open_parens + a little bit for hash)

class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) % 2 != 0: return False
        
        open = set('({[')
        closed = set(']})')
        
        table = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        
        stack = []
        i = 0
        
        for i in range(len(s)):
            
            if s[i] in open:
                stack.append(s[i])
            
            elif s[i] in closed:
                if not stack:
                    return False
                l = stack.pop()
                cl = table[s[i]]
                if l != cl:
                    return False
        
        if not len(stack) and i == len(s)-1:
            return True
        else:
            False
                