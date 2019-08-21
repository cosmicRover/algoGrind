# Problem H2
# Solution
# O(N) time | O(1) space


# helper func to determine if a number is sorted
def isOutOfOrder(i:int, num:int, array:[int]) -> bool:
    # special case 0
    if i is 0:
        return True if num > array[i + 1] else False

    # special case for the last index of an array
    if i is len(array) -1:
        return True if num < array[i - 1] else False
    
    #checks to see if num is > left and < right (the sorted path)
    return True if num > array[i + 1] or num < array[i - 1] else False


# finds the index of the min and max unsorted range
def subarrayUnsortedIndicesRange(array:[int]):
    
    # setting min and max values to infinity and -infinity
    # the idea is that any num is less than inf while any num is bigger than -inf
    # this way we can find the min and max of the first values withe ease
    minValue = float("inf")
    maxValue = float("-inf")

    # dor loop to iterate through the array
    for index in range(len(array)):
        num = array[index]

        # if it's out of order find the min and max values. inf and -inf comes in handy here
        if isOutOfOrder(index, num, array):
            minValue = min(minValue, num)
            maxValue = max(maxValue, num)
    
    # if already sorted and no change, just return these
    if minValue is float("inf"):
        return [-1, 1]
    
    # finds the indices of min and max

    # checks from right to left
    # increments
    subLeftIndex = 0
    while minValue >= array[subLeftIndex]:
        subLeftIndex += 1
    
    # checks from left to right
    # decrements
    subRightIndex = len(array) -1
    while maxValue <= array[subRightIndex]:
        subRightIndex -= 1

    # returns the counters
    return [subLeftIndex, subRightIndex]


inputArray:[int] = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
result = subarrayUnsortedIndicesRange(inputArray)
print(result)