
def reverseInt(input):
    
    reversed = 0
    absInput = abs(input)

    while absInput > 0:

        # dvide the absolute value of our input by 10 and get the remainder
        remainder = absInput % 10

        # multiply the previously stored reverse value by 10 and add the remainder
        reversed = reversed * 10 + remainder

        # divide absInput with 10 agin and store only the int
        absInput = absInput // 10

    # checks if the reversed int exceeds the 32 bit int limit 
    if(reversed > (2 ** 31 - 1)):
        return 0

    # multiply reversed with -1 if original itput was negative
    return reversed * -1 if input < 0 else reversed

val = 123213
print(reverseInt(val))