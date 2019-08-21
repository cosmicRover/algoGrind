# similar method to reverse int 

def isNumPalindrome(inputNum):

    # if it's a negative num, it's not gonna be palindrome at all
    if inputNum < 0:
        return False

    # two vars to hold some values
    reversed = 0
    absInput = abs(inputNum)

    while absInput > 0:
        remainder = absInput % 10
        reversed = reversed * 10 + remainder
        absInput = absInput // 10

    # if the absolute value of the original input matches reversed, then its a palindrome
    if abs(inputNum) == reversed:
        return True
    else:
        return False
    


print(isNumPalindrome(-121))
