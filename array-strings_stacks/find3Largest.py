# Problem E 7
# Solution


# Time O(n) | O(1) space
def findThreelargest(inputArray:list) -> list:

    # stores the 3 largets ints, init as None
    largestNumArray:list = [None, None, None]

    # iterates through the inputArray
    for num in inputArray:
        if largestNumArray[2] is None or num > largestNumArray[2]:
            shiftUpdate(largestNumArray, num, 2)
        elif largestNumArray[1] is None or num > largestNumArray[1]:
            shiftUpdate(largestNumArray, num, 1)
        elif largestNumArray[0] is None or num > largestNumArray[0]:
            shiftUpdate(largestNumArray, num, 0)
    return largestNumArray

# moves around the values according to their given index
def shiftUpdate(array:list, num:int, index:int):
    
    # loop through and move the elemnst
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i + 1]


result = findThreelargest([10, 5, 9, 10, 12])
print(result)


