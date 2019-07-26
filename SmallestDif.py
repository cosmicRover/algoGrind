# Problem M 2
# Solution

# Time O(nlog(n) + mlog(m)) | O(1) space
# Sorting the array first and the using two pointers to traverse through the arrays

def smallestDif(array1, array2):

    array1.sort()
    array2.sort()

    arr1Pointer = 0
    arr2Pointer = 0
    smallestDifPair = [float("inf"), float("-inf")]

    while arr1Pointer < len(array1) and arr2Pointer < len(array2):

        if array1[arr1Pointer] == array2[arr2Pointer]:
            smallestDifPair[0], smallestDifPair[1] = array1[arr1Pointer], array2[arr2Pointer]
            return smallestDifPair
        
        if array1[arr1Pointer] > array2[arr2Pointer]:

            currentDif = abs(array1[arr1Pointer] - array2[arr2Pointer])

            if abs(smallestDifPair[0] - smallestDifPair[1]) > currentDif:
                smallestDifPair[0], smallestDifPair[1] = array1[arr1Pointer], array2[arr2Pointer]
            arr2Pointer += 1

        if array1[arr1Pointer] < array2[arr2Pointer]:

            currentDif = abs(array1[arr1Pointer] - array2[arr2Pointer])

            if abs(smallestDifPair[0] - smallestDifPair[1]) > currentDif:
                smallestDifPair[0], smallestDifPair[1] = array1[arr1Pointer], array2[arr2Pointer]
            
            arr1Pointer += 1

    return smallestDifPair


   

arr1 = [-1, 5, 10, 20, 28, 3]
arr2 = [26, 134, 135, 15, 17]
print(smallestDif(arr1, arr2))