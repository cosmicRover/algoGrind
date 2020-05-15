'''
The trick with this foresaken problem is to understand that you wdont have to
pop the min element once you store it. Therefore, you can lazy append the min
values as they come in and it will always be at the mstack[-1] index.
Also for popping, you must also pop the mstack if the element happen to
match with regular stack.
Time O(1) | Space O(n)
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.mstack or x <= self.mstack[-1]:
            self.mstack.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mstack[-1]:
            self.mstack.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]