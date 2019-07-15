# swapping array elements without a temp value in python using two pointers
# works on all types of values.
# Time O(n) | O(1) Space


def inPlaceSwap(list:list) -> list:

    if len(list) == 1:
        return list

    leftPointer = 0
    rightPointer = len(list) - 1

    while leftPointer < rightPointer:

        list[leftPointer], list[rightPointer] = list[rightPointer], list[leftPointer]

        leftPointer += 1 
        rightPointer -= 1

    return list

array = [4, 5, 6, '7', 8]
print(inPlaceSwap(array))
