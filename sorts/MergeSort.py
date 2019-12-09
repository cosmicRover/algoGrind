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
    
    #make a copy of the array
    aux_array = array[:]
    
    mergeSortHelper(array, 0, len(array) -1, aux_array)
    
    return array


def mergeSortHelper(main_array, start, end, aux_array):
    if start == end:
        return 

    #get middle and call this func recursively on the both halves
    #but replace the aux array with the main array in the call
    middle = (start + end) >> 1

    mergeSortHelper(aux_array, start, middle, main_array)
    mergeSortHelper(aux_array, middle + 1, end, main_array)

    #call do merge with normal main/aux positions
    doMerge(main_array, start, middle, end, aux_array)

#this func merges the two halves together
def doMerge(main_array, start, middle, end, aux_array):
    #init pointers for the three points of interests
    current_pointer = start
    left_pointer = start
    right_pointer = middle + 1

    #merge loop
    while left_pointer <= middle and right_pointer <= end:

        #if the left value <= right, the current pointer on main array gets it
        #inc left by 1
        if aux_array[left_pointer] <= aux_array[right_pointer]:
            main_array[current_pointer] = aux_array[left_pointer]
            left_pointer += 1

        #otherwise, current on main becomes right
        #inc right by 1
        else:
            main_array[current_pointer] = aux_array[right_pointer]
            right_pointer += 1

        current_pointer += 1

    #the loop to clear out any left over elemnts on left or right half on aux array
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