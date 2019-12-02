'''
QuickSort implementation
The key strategy is to use a pivot point at the start of an array and use a left/right pointer to compare 
values with the pivot point, then inc/dec the left/right. In the end of the loop swap pivot with the right 
and call the function recursively on the smaller subArray first.

Time: Best case O(n), Worst O(n^2), Avg O(n log n)
Space: O(log(n))
'''

def quickSort(array):
    sort(array, 0, len(array) - 1)
    return array

def sort(array, startIdx, endIdx):
    # base case where the length is 1, we just return
    if startIdx >= endIdx:
        return

    #init pivot, left and right
    pivot = startIdx
    left = pivot + 1
    right = endIdx

    #the comparison loop
    while left <= right:

        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)

        if array[left] <= array[pivot] and array[right] < array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

    #swap pivot with right at the end of the loop, 
    swap(array, pivot, right)
    
    #then call sort recursively on smaller sub-array first, then larger
    val = isLeftSubSmaller(right, startIdx, endIdx)
    if val:
        sort(array, startIdx, right - 1)
        sort(array, right + 1, endIdx)
    else:
        sort(array, right + 1, endIdx)
        sort(array, startIdx, right - 1)
    

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def isLeftSubSmaller(right, startIdx, endIdx):
    #               left                <         right
    return True if right - 1 - startIdx < endIdx - (right + 1) else False


inputArr = [8, 5, 2, 9, 5, 6, 3]
print(quickSort(inputArr))
