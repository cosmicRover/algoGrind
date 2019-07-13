def isPlanindrome(word:str) -> bool:

    # in case no value, return False
    if word is None:
        return False

    # convert string to a list
    wordArray = list(word) #O(n)
    
    # init the left and the right pointers
    leftPointer = 0
    rightPointer = len(wordArray) -1

    # iterate through the list till left is > right
    while leftPointer < rightPointer:
        
        # if elements match, inc/dec the pointers
        if wordArray[leftPointer] == wordArray[rightPointer]:
            leftPointer += 1
            rightPointer -= 1
        
        # else just return False
        else:
            return False
    return True



result = isPlanindrome("madam")
print(result)

result = isPlanindrome("mldam")
print(result)