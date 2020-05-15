#Given an array nums of length n. All elements appear in pairs except one of them. Find this single element that appears alone.
#Pairs of the same element cannot be adjacent:

# Time O(n) | Space O(1) can do better using binary search O(log(n))
def findOutOfPair(pairArray):

    pointer = 1

    for _ in range(0, len(pairArray) - 2):
        if pairArray[pointer - 1] != pairArray[pointer]:
            print("Found the misMatch %s" %pairArray[pointer -1])
            return
        pointer += 2 


inputArray = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2]
findOutOfPair(inputArray)