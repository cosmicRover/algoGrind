# Problem H 20
# Solution
# Time Best: O(nLoh(n)) Worst: )(N^2) | Space O(Log(n))

def swap(x, y, array):
    array[x], array[y] = array[y], array[x]

def quickSort(array):
    quickSortHelper(array, 0, len(array) -1)
    return array

def quickSortHelper(array, startPointer, endPointer):
    # base case 
    if startPointer >= endPointer:
        return

    # declare pivot, left and right pointers
    pivotPointer = startPointer
    leftPointer = startPointer + 1
    rightPointer = endPointer

    # loop based on left and right pointers
    while rightPointer >= leftPointer:
        # if left > pivot and right < pivot swap left and right pointer values
        if array[leftPointer] > array[pivotPointer] and array[rightPointer] < array[pivotPointer]:
            swap(leftPointer, rightPointer, array)
        
        # if left <= pivot, increase left 
        if array[leftPointer] <= array[pivotPointer]:
            leftPointer += 1
        
        # if right >= pivot, decrease right
        if array[rightPointer] >= array[pivotPointer]:
            rightPointer -= 1
    
    # swap pivot with right when the loop ends
    swap(pivotPointer, rightPointer, array)

    # bool test to see which of the subarrays are smaller
    leftSubArrayIsSmaller = rightPointer - 1 - startPointer < endPointer - (rightPointer + 1)

    # if left is smaller than right sub, perform quicksort on left sub first
    # then perform quicksort on right sub
    # left takes start and right -1, while right takes right + 1 and end pointer
    if leftSubArrayIsSmaller:
        quickSortHelper(array, startPointer, rightPointer - 1)
        quickSortHelper(array, rightPointer + 1, endPointer)
    else: # flip it on else case
        quickSortHelper(array, rightPointer + 1, endPointer)
        quickSortHelper(array, startPointer, rightPointer - 1)