class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        eval using single stack approach.
        each time you encounter a sign, pop two items from stack
        and evalue them using the sign. After that put the item back on the stack.
        The result will be the last item on stack
        
        time O(n) | space O(n)
        
        '''
        
        stack = []
        
        for i in range(len(tokens)):
            #PEMDAS
            #lstrip() removes the +/- sign a number might have so that isdigit() can evaluate
            if tokens[i].lstrip('+-').isdigit() == False: 
                second = stack.pop()
                first = stack.pop()
                
                val = self.calculate(int(first), int(second), tokens[i])
                stack.append(val)
                
            else:
                stack.append(tokens[i])
                
        return int(stack.pop())
                
                
    def calculate(self, first, second, sign):
        if sign == "*":
            return first * second
        if sign == "/":
            return first / second
        if sign == "+":
            return first + second
        if sign == "-":
            return first - second