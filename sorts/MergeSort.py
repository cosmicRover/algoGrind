'''
Merge sorts are used with the divide and conquer approach. The first approach doesnt mutate the main
input array but rather creates aux arrays and uses them to stitch together a sorted array.
First approach runs at O(n log n) time since there is O(n) work at each level and we keep dividing it.
And the space is O(n log n) as well for the first approach
'''

# def mergeSort(array):
#     #base case, if len is 1 just return array
#     if len(array) == 1:
#         return array

#     middle = len(array) >> 1
#     left_half = array[:middle]
#     right_half = array[middle:]

#     #call mergeSortedArrays with the values of mergeSort recursively
#     return mergeSortedArrays(mergeSort(left_half), mergeSort(right_half))


# def mergeSortedArrays(left_half, right_half):
#     #init an aux array with len of left+right, it will hold the sorted array
#     sortedArray = [None] * (len(left_half) + len(right_half))
    
#     current_pointer = left_pointer = right_pointer = 0

#     while left_pointer < len(left_half) and right_pointer < len(right_half):
        
#         if left_half[left_pointer] <= right_half[right_pointer]:
#             sortedArray[current_pointer] = left_half[left_pointer]
#             left_pointer += 1

#         else:
#             sortedArray[current_pointer] = right_half[right_pointer]
#             right_pointer += 1

#         current_pointer += 1

#     #if we have any remaining numbers on the left half
#     while left_pointer < len(left_half):
#         sortedArray[current_pointer] = left_half[left_pointer]
#         left_pointer += 1
#         current_pointer += 1

#     #similarly, if we have any remaining on the right half
#     while right_pointer < len(right_half):
#         sortedArray[current_pointer] = right_half[right_pointer]
#         right_pointer += 1
#         current_pointer += 1

#     return sortedArray


# input_array = [13, 5, 7, 88, 3, 4, 5, 2112, 43, -78, -4]
# print(mergeSort(input_array))

'''
The second aproach where the space is reduced to O(n)
'''

def mergeSort(array):
    if len(array) == 1: return array
    aux_array = array[:]
    
    mergeSortHelper(array, 0, len(array) -1, aux_array)
    return array


def mergeSortHelper(main_array, start, end, aux_array):
    if start == end:
        return 

    #get middle and the call helper function on the two half
    #while passing aux as the main array
    middle = (start + end) >> 1

    mergeSortHelper(aux_array, start, middle, main_array)
    mergeSortHelper(aux_array, middle + 1, end, main_array)

    doMerge(main_array, start, middle, end, aux_array)

def doMerge(main_array, start, middle, end, aux_array):
    current_pointer = start
    left_pointer = start
    right_pointer = middle + 1

    while left_pointer <= middle and right_pointer <= end:

        if aux_array[left_pointer] <= aux_array[right_pointer]:
            main_array[current_pointer] = aux_array[left_pointer]
            left_pointer += 1

        else:
            main_array[current_pointer] = aux_array[right_pointer]
            right_pointer += 1

        current_pointer += 1

    while left_pointer <= middle:
        main_array[current_pointer] = aux_array[left_pointer]
        left_pointer += 1
        current_pointer += 1

    while right_pointer <= end:
        main_array[current_pointer] = aux_array[right_pointer]
        right_pointer += 1
        current_pointer += 1

input_array = [13, 5, 7, 88, 3, 4, 5, 2112, 43, -78, -4]
print(mergeSort(input_array))