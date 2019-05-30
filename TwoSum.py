# Problem E1
# solutions

# O(n^2) time | O(1) space
# running through each elements till we hit the target sum
def twoNumberSumLoops(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# O(n) time | O(n) space
# using a dict, storing the elements and then finding a match
def twoNumberSumDict(array, targetSum):
    nums = {} # the empty dict
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums: # if potentil match exists, return it as an array
            return [potentialMatch, num]
        else: # otherwise just store it in the dict
            nums[num] = True 
    return []

# O(nLogn) time | O(1) space
# using two pointers to find the targetSum on a sorted array
def twoNumberSumSort(array, targetSum):
    array.sort() # O(nLogn) comes from here
    
    # assigning the left and right pointers
    left = 0
    right = len(array) - 1

    while left < right: # makes sure pointer positions don't overlap
        currentSum = array[left] + array[right] # gets the sum of both elements
        
        if currentSum == targetSum: # match found
            return [array[left], array[right]]
        elif currentSum < targetSum: # if less, increment left
            left += 1
        elif currentSum > targetSum: # if more, decrement right
            right -= 1
    return []