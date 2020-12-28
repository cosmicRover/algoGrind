class Solution:
    def decodeString(self, s: str) -> str:
        '''
        One stack technique
        similar to valid bracket technique, append everything 
        on the stack till you find a closing bracket. that's
        when you starct popping. but in this case, we need
        to watch out for numbers after '['
        
        time O(max(num)^nested_num_values  * max(len(input_string))) | space O(sum of all decoded string length)
        '''
        
        stack = []
        
        #iterate through the string
        for i in range(len(s)):
            #if we encounter "]", must pop from stack
            if s[i] == "]":
                temp = ""
                
                #phase 1, pop from stack until we find an opening bracket '['
                while stack[-1] != "[":
                    item = stack.pop()
                    temp += item
                    
                #pop the opening bracket
                stack.pop()
                
                #phase 2, extract the number using num and base system
                base = 1
                num = 0
                
                #while stack isn't empty and we have a number to pop, we keep the loop going.
                #takes care of multi-digit numbers
                while stack and stack[-1].isdigit():
                    item = stack.pop()
                    num += int(item) * base
                    base *= 10
                    
                #phase 3, append each element of temp num times, going in reverse direction
                while num != 0:
                    for item in temp[::-1]:
                        stack.append(item)
                    num -= 1
            #everything else, append to stack
            else:
                stack.append(s[i])
                
        return "".join(stack)
            