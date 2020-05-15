# Problem M 22
# Solution

# Time O(n) | Space O(n)
def BalancedBrackets(parens):

    # if is not completely divisible by 0, its not palindrome
    if len(parens) % 2 != 0:
        return False
    
    # stack to keep track of the opening parens
    stack = []
    
    # sets to compare the parens with
    openingParens = set('({[')
    completeParens = set([('(', ')'), ('{', '}'), ('[', ']')])

    # iterate over the parens
    for paren in parens:
        
        # if the current paren is in the opening parens, append to stack
        if paren in openingParens:
            stack.append(paren)

        else:
            # without a opening paren, it can't be a palindrome
            if len(stack) == 0:
                return False
            
            # pop the last open paren
            lastOpen = stack.pop()

            # set lastOpen and current paren to compare against the complete set
            # if not in complete set, return false
            if(lastOpen, paren) not in completeParens:
                return False
                
    # return true if len of stack is 0. It will be 0 if there are no more parens left and its balanced
    return len(stack) == 0

print(BalancedBrackets("([]]{)"))

