# Problem E 8
# Solution

# Time O(n^2) | Space O(1)

def bubbleSort(inputArray:[int]) -> [int]:

    isSorted:bool = False

    while (not isSorted):
        
        isSorted = True
        
        for x in range(0, len(inputArray) - 1):
            if inputArray[x] > inputArray[x + 1]:
                inputArray[x], inputArray[x + 1] = inputArray[x + 1], inputArray[x]
                isSorted = False # sets to false every time an element had to be swapped


    return inputArray


array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(array))