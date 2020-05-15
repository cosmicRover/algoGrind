'''
The calculator problem is all about the delay approach.
For example, we keep adding to num till we hit an operator sign
or we are at the last element. We multiply or divide an element by popping it
from the stack and appending it after multiplying/dividing it

(Without brackets)
Time O(n) Space O(n)
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, "+"
        
        #TODO
        #gotta work out the case for brackets....
        
        stack = self.calculator(s, stack, num, sign)
        sums = sum(stack)
        return sums
    
    
    def calculator(self, s, stack, num, sign):
        for i in range(len(s)):
            
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            if s[i] in "+-/*" or i == len(s) -1: #or i at the last index, gotta append the last num
                if sign == "+":
                    stack.append(num)
                
                elif sign == "-":
                    stack.append(-num)
                    
                elif sign == "*":
                    last = stack.pop()
                    stack.append(last * num)
                
                else:
                    last = stack.pop()
                    stack.append(int(last / num))#floor the value
                
                #neutralize num and assign new sign
                num = 0
                sign = s[i]
        print(stack)  
        return stack
        

sol = Solution()
inputStr = " 2 +   33*        3 / 4 * 9 + 8"

print(sol.calculate(inputStr))