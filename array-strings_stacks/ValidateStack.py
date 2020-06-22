'''
Time O(N) | Space O(N)

The trick here is to use a stack to "append" all the pushed values and then "pop"
from the stack as long as the first item on popped match with the last item on pushed.
If they do, also pop the stack.

If the sequences are possible, the stack should be empty.
'''

class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        stack = []
        i = 0
        
        for x in pushed:
            stack.append(x)
            print("appended:- ", x)
            while stack and stack[-1] == popped[i]:
                print(stack[-1], popped[i])
                stack.pop()
                i += 1
                
        return not stack