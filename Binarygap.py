# Time O(n) | Space O(1)

def findTheGapOf1(inputValue):
    
    # convert to binary and slice the first 2 chars off
    value = bin(inputValue)
    value = value[2:]

    # init some vars with 0
    previousEncountered = distance = 0
    leftPointer = 0

    # use leftPointer to iterate
    while leftPointer != len(value):

        # if 1 encountered, get the max of currentDistance and left - prevDistance
        if value[leftPointer] == "1":
            
            distance = max(distance, leftPointer - previousEncountered)
            previousEncountered = leftPointer


        leftPointer += 1

    print(distance)



findTheGapOf1(22)
