# Problem M11
# Solution

# O(n) time because we pass only once | O(1) space because we only store two vars
def findLargest(arr:[int]) -> int:

    # two vars to keep tarck of max value
    maxEndingHere:int = arr[0]
    subArrayMax:int = arr[0]
    
    # simple loop to iterate through the array
    for value in arr[1:]:
        # maxEndingHere takes the bigger amount between iterated value and iterated value + max's current value
        maxEndingHere = max(value, maxEndingHere + value)

        # subArrayMax holds the max between itself and maxEndingHere
        subArrayMax = max(subArrayMax, maxEndingHere)

    # return the max
    return subArrayMax


inputArray = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
result = findLargest(inputArray)
print("current max is: %s" %result)